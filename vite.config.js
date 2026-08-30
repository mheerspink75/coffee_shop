import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

export default defineConfig({
  plugins: [react()],
  base: process.env.GITHUB_PAGES ? '/coffee_shop/' : '/',
  optimizeDeps: {
    esbuildOptions: { target: 'esnext' },
    exclude: ['@pyscript/core'],
  },
  build: {
    target: 'esnext',
    rollupOptions: {
      external: (id) =>
        id.includes('3rd-party') ||
        id.startsWith('codemirror') ||
        id.startsWith('@codemirror') ||
        id === 'string-width',
    },
  },
});
