// Kitchen offline cache. Bump VERSION each release. Data files are network-first so new recipes show on launch.
const VERSION = "kitchen-v1.4";
const SHELL = ["./", "index.html", "manifest.webmanifest", "icon-192.png", "icon-512.png"];
const DATA = ["data/recipes.js", "data/foods.js"];
self.addEventListener("install", e => e.waitUntil(caches.open(VERSION).then(c => c.addAll([...SHELL, ...DATA])).then(() => self.skipWaiting())));
self.addEventListener("activate", e => e.waitUntil(caches.keys().then(ks => Promise.all(ks.filter(k => k !== VERSION).map(k => caches.delete(k)))).then(() => self.clients.claim())));
self.addEventListener("fetch", e => {
  const u = new URL(e.request.url);
  if (e.request.method !== "GET" || u.origin !== location.origin) return;
  const isData = u.pathname.includes("/data/") || e.request.mode === "navigate";
  if (isData) e.respondWith(fetch(e.request, { cache: "no-store" }).then(r => { const c = r.clone(); caches.open(VERSION).then(x => x.put(e.request, c)); return r; }).catch(() => caches.match(e.request, { ignoreSearch: true })));
  else e.respondWith(caches.match(e.request).then(r => r || fetch(e.request)));
});
