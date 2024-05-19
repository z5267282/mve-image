FROM alpine:latest

WORKDIR /app
COPY . .
COPY src/backup.jsx src/App.jsx
EXPOSE 5000

RUN apk add --update npm dash && \
    npm install && \
    chmod +x start-container.sh

ENTRYPOINT ["/app/start-container.sh"]
