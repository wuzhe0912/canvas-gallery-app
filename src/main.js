import './style.css';
import router from './router/router.js';
import routes from './router/routes.js';

// register all routes
routes.forEach(({ path, callback }) => {
  router.register(path, callback);
});

// init router：set hashchange and load event listener
router.init();
