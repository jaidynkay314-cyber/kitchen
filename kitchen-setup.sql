-- Kitchen: shared week plan and shopping list. Paste into Supabase > SQL Editor > New query, then Run.
-- Uses the same Supabase project as Solo Lifting. Safe to run more than once.
create table if not exists kitchen_items (
  hh text not null,              -- household code (from the invite link)
  kind text not null,            -- plan, tick or extra
  id text not null,
  body jsonb,                    -- null means deleted
  updated_at timestamptz not null default now(),
  primary key (hh, kind, id)
);
create index if not exists kitchen_items_hh_updated on kitchen_items (hh, updated_at);

create or replace function touch_updated_at() returns trigger language plpgsql as $$
begin new.updated_at = now(); return new; end $$;
drop trigger if exists kitchen_items_touch on kitchen_items;
create trigger kitchen_items_touch before insert or update on kitchen_items for each row execute function touch_updated_at();

-- No direct access to the table: row level security on with no policies.
-- The app reads and writes only through these two functions, and only for a household code it already knows.
alter table kitchen_items enable row level security;

create or replace function kitchen_pull(p_hh text, p_since timestamptz)
returns setof kitchen_items language sql security definer set search_path = public as $$
  select * from kitchen_items
  where hh = p_hh and length(p_hh) >= 12 and (p_since is null or updated_at >= p_since)
  order by updated_at, kind, id limit 500
$$;

create or replace function kitchen_push(p_hh text, p_rows jsonb)
returns void language plpgsql security definer set search_path = public as $$
begin
  if length(p_hh) < 12 then raise exception 'bad household code'; end if;
  insert into kitchen_items (hh, kind, id, body)
  select p_hh, r->>'kind', r->>'id', r->'body' from jsonb_array_elements(p_rows) r
  where r->>'kind' in ('plan', 'tick', 'extra') and length(r->>'id') between 1 and 200
  on conflict (hh, kind, id) do update set body = excluded.body;
end $$;

revoke all on function kitchen_pull(text, timestamptz) from public;
revoke all on function kitchen_push(text, jsonb) from public;
grant execute on function kitchen_pull(text, timestamptz) to anon, authenticated;
grant execute on function kitchen_push(text, jsonb) to anon, authenticated;
