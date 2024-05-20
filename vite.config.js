// vite.config.js
import { defineConfig } from "vite";

export default defineConfig({
    server: {
        fs: {
            strict: false,
            allow: ["/Users/sunny/Desktop/videos"],
        },
    },
});
