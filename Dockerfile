FROM alpine:latest

WORKDIR /app
COPY . .

RUN apk add --update npm dash python3 && \
    npm install && \
    chmod +x start-container.sh

ENTRYPOINT ["/app/start-container.sh"]
