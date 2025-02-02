const routes = [
  {
    path: '/',
    callback: () => {
      const app = document.querySelector('#app');
      app.innerHTML = `
        <nav>
          <a href="#/">Home</a> |
          <a href="#/about">About</a>
        </nav>
        <h1>Welcome to Home</h1>
      `;
    },
  },
  {
    path: '/about',
    callback: () => {
      document.querySelector('#app').innerHTML = `
        <nav>
          <a href="#/">Home</a> |
          <a href="#/about">About</a>
        </nav>
        <h1>About</h1>
        <p>This is the content of the About page.</p>
      `;
    },
  },
  {
    path: '*',
    callback: () => {
      document.querySelector('#app').innerHTML = `
        <nav>
          <a href="#/">Home</a> |
          <a href="#/about">About</a>
        </nav>
        <h1>404 - Page not found</h1>
        <p>Sorry, the page you are looking for does not exist.</p>
      `;
    },
  },
];

export default routes;
