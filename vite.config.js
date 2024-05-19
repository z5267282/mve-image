// vite.config.js
import { defineConfig } from "vite";

export default defineConfig({
    server: {
        fs: {
            strict: false,
            allow: ["/mnt/videos"],
        },
    },
});
