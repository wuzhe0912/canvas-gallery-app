import Home from '../pages/Home.js';
import NotFound from '../pages/NotFound.js';

const routes = [
  { path: '/', callback: Home },
  { path: '*', callback: NotFound },
];

export default routes;
