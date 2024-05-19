// vite.config.js
import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

export default defineConfig({
    server: {
        fs: {
            strict: false,
            allow: ["/mnt/videos"],
        },
    },
});
