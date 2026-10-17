const CACHE_NAME = 'mfs-cache-v20261017g';

const RELATIVE_ASSETS = [
  '',
  'index.html',
  'courses.html',
  'worksheets.html',
  'past-papers.html',
  'functional-skills-past-papers.html',
  'revision-cards.html',
  'shop.html',
  'assets/css/mfs-theme.css',
  'assets/css/mfs-mobile.css',
  'assets/css/mfs-revision.css',
  'assets/css/mfs-video-modal.css',
  'assets/js/mfs-mobile.js',
  'assets/js/mfs-tint.js',
  'assets/js/mfs-pwa.js',
  'assets/img/favicon-192x192.png',
  'assets/img/favicon-512x512.png',
  'assets/img/favicon.svg',
  'assets/img/favicon.ico',
  'manifest.json'
];

self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => {
      // Resolve asset paths against the service worker's actual scope
      const precacheUrls = RELATIVE_ASSETS.map((asset) => {
        return new URL(asset, self.registration.scope).href;
      });
      return cache.addAll(precacheUrls).catch((err) => {
        console.warn('[MFS SW] Precache non-critical notice:', err);
      });
    }).then(() => self.skipWaiting())
  );
});

self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then((cacheNames) => {
      return Promise.all(
        cacheNames
          .filter((name) => name !== CACHE_NAME)
          .map((name) => caches.delete(name))
      );
    }).then(() => self.clients.claim())
  );
});

self.addEventListener('fetch', (event) => {
  const request = event.request;
  if (request.method !== 'GET') return;

  const url = new URL(request.url);

  // Exclude external third-party tracking, YouTube embeds, and media streams
  if (url.origin !== self.location.origin) {
    // For external CDNs like font-awesome or google fonts, try cache first
    if (url.hostname.includes('cdnjs.cloudflare.com') || url.hostname.includes('fonts.googleapis.com') || url.hostname.includes('fonts.gstatic.com')) {
      event.respondWith(
        caches.match(request).then((cachedResponse) => {
          if (cachedResponse) return cachedResponse;
          return fetch(request).then((networkResponse) => {
            if (networkResponse && networkResponse.status === 200) {
              const responseClone = networkResponse.clone();
              caches.open(CACHE_NAME).then((cache) => cache.put(request, responseClone));
            }
            return networkResponse;
          }).catch(() => null);
        })
      );
    }
    return;
  }

  // HTML navigation requests: Network-First with Cache Fallback
  if (request.mode === 'navigate' || request.headers.get('accept')?.includes('text/html')) {
    event.respondWith(
      fetch(request)
        .then((networkResponse) => {
          if (networkResponse && networkResponse.status === 200) {
            const responseClone = networkResponse.clone();
            caches.open(CACHE_NAME).then((cache) => cache.put(request, responseClone));
          }
          return networkResponse;
        })
        .catch(() => {
          return caches.match(request).then((cachedResponse) => {
            if (cachedResponse) return cachedResponse;
            // Fallback to home/index if offline and page not cached
            const fallbackUrl = new URL('index.html', self.registration.scope).href;
            return caches.match(fallbackUrl);
          });
        })
    );
    return;
  }

  // Static Assets (CSS, JS, Images): Cache-First with Network Fallback
  event.respondWith(
    caches.match(request).then((cachedResponse) => {
      if (cachedResponse) {
        // Fetch in background to update cache (stale-while-revalidate for local assets)
        fetch(request).then((networkResponse) => {
          if (networkResponse && networkResponse.status === 200) {
            caches.open(CACHE_NAME).then((cache) => cache.put(request, networkResponse));
          }
        }).catch(() => {});
        return cachedResponse;
      }

      return fetch(request).then((networkResponse) => {
        if (networkResponse && networkResponse.status === 200 && networkResponse.type === 'basic') {
          // Do not cache oversized PDF files (> 10MB) in service worker cache
          const contentLength = networkResponse.headers.get('content-length');
          if (!contentLength || parseInt(contentLength, 10) < 10 * 1024 * 1024) {
            const responseClone = networkResponse.clone();
            caches.open(CACHE_NAME).then((cache) => cache.put(request, responseClone));
          }
        }
        return networkResponse;
      });
    })
  );
});
