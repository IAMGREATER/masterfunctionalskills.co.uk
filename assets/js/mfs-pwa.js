/**
 * Master Functional Skills - Progressive Web App (PWA) Engine
 * Dynamically resolves SW scope (supporting custom domains & GitHub Pages subpaths),
 * provides offline caching lifecycle, and powers one-tap app installation.
 */
(function() {
  'use strict';

  // 1. Resolve Base Path dynamically
  var pathname = window.location.pathname;
  var basePath = '/';
  if (pathname.includes('/masterfunctionalskills.co.uk')) {
    basePath = '/masterfunctionalskills.co.uk/';
  }

  // 2. Service Worker Registration
  if ('serviceWorker' in navigator) {
    window.addEventListener('load', function() {
      navigator.serviceWorker.register(basePath + 'sw.js', { scope: basePath })
        .then(function(reg) {
          // Check for worker updates
          reg.addEventListener('updatefound', function() {
            var newWorker = reg.installing;
            if (newWorker) {
              newWorker.addEventListener('statechange', function() {
                if (newWorker.state === 'installed' && navigator.serviceWorker.controller) {
                  // New content is available in background
                  console.log('[MFS PWA] New update cached. Reload to view latest.');
                }
              });
            }
          });
        })
        .catch(function(err) {
          console.warn('[MFS PWA] SW registration failed:', err);
        });
    });
  }

  // 3. Install App Prompt Management
  var deferredInstallPrompt = null;
  window.addEventListener('beforeinstallprompt', function(e) {
    // Prevent the mini-infobar from appearing on mobile
    e.preventDefault();
    deferredInstallPrompt = e;
    window.__mfsInstallPrompt = e;

    // Show Install button in drawer if available
    var installContainer = document.getElementById('mfsDrawerInstallBox');
    if (installContainer) {
      installContainer.style.display = 'block';
    }
  });

  // Global helper to trigger install prompt
  window.__mfsTriggerInstall = function() {
    if (deferredInstallPrompt) {
      deferredInstallPrompt.prompt();
      deferredInstallPrompt.userChoice.then(function(choiceResult) {
        if (choiceResult.outcome === 'accepted') {
          console.log('[MFS PWA] User accepted app installation');
        }
        deferredInstallPrompt = null;
        var installContainer = document.getElementById('mfsDrawerInstallBox');
        if (installContainer) {
          installContainer.style.display = 'none';
        }
      });
    }
  };

  window.addEventListener('appinstalled', function() {
    console.log('[MFS PWA] App installed successfully');
    deferredInstallPrompt = null;
    var installContainer = document.getElementById('mfsDrawerInstallBox');
    if (installContainer) {
      installContainer.style.display = 'none';
    }
  });
})();
