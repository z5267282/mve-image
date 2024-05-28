FROM alpine:latest

WORKDIR /app
COPY . .

RUN apk add --update npm dash && \
    npm install && \
    chmod +x start-container.sh

ENTRYPOINT ["/app/start-container.sh"]
