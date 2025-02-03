import { renderInApp } from '../utils/renderer.js';

const demoList = [
  {
    id: 1,
    title: 'Particle System',
    description: 'Interactive particle system with mouse tracking',
    difficulty: 'Intermediate',
    path: '/particle',
  },
  {
    id: 2,
    title: 'Fractal Tree',
    description: 'Recursive fractal tree animation',
    difficulty: 'Beginner',
    path: '/fractal',
  },
  {
    id: 3,
    title: 'Rain Effect',
    description: 'Realistic rain animation with splash effects',
    difficulty: 'Advanced',
    path: '/rain',
  },
];

const createGalleryCard = (demo) => `
  <div class="gallery-card glass" onclick="window.location.hash='${demo.path}'">
    <div class="card-content">
      <div>
        <h2 class="card-title">${demo.title}</h2>
        <p class="card-description">${demo.description}</p>
      </div>
      <div class="card-footer">
        Difficulty: ${demo.difficulty}
      </div>
    </div>
  </div>
`;

const Home = () => {
  renderInApp(`
    <div class="container mx-auto px-4 py-8">
      <h1 class="text-4xl text-white mb-8 text-center">Canvas Gallery</h1>
      <div class="gallery-grid">
        ${demoList.map((demo) => createGalleryCard(demo)).join('')}
      </div>
    </div>
  `);
};

export default Home;
