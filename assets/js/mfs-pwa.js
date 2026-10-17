/**
 * Master Functional Skills - Service Worker Registration
 */
if ('serviceWorker' in navigator) {
  window.addEventListener('load', () => {
    navigator.serviceWorker.register('/sw.js')
      .then((reg) => {
        // SW registered successfully
      })
      .catch((err) => {
        console.warn('MFS SW registration failed:', err);
      });
  });
}
