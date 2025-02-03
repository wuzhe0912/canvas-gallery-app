const router = {
  routes: {},
  register(path, callback) {
    this.routes[path] = callback;
  },
  init() {
    window.addEventListener('hashchange', this.handleRouteChange.bind(this));
    window.addEventListener('load', this.handleRouteChange.bind(this));
  },
  handleRouteChange() {
    const path = location.hash.slice(1) || '/';
    const route = this.routes[path] || this.routes['*'];
    if (typeof route === 'function') {
      route();
    } else {
      console.log(`No route defined for ${path}`);
    }
  },
  navigate(path) {
    location.hash = path;
  },
};

export default router;
