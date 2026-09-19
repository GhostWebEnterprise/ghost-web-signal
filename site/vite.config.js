import { defineConfig } from "vite";

export default defineConfig({
  base: "/ghostweb.signal/",
  build: {
    outDir: "dist",
    emptyOutDir: true
  }
});
