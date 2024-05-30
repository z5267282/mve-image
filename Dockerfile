FROM alpine:latest

WORKDIR /app
COPY . .

RUN apk add --update npm dash python3 py3-websockets && \
    npm install && \
    # pip3 install -r requirements.txt && \
    chmod +x start-container.sh

ENTRYPOINT ["/app/start-container.sh"]
