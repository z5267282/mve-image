FROM python:3.9-slim


WORKDIR /app
COPY . .

RUN apt-get update && \
    apt-get install -y curl ffmpeg npm && \
    apt-get clean && \
    chmod +x start-container.sh

ENTRYPOINT ["/app/start-container.sh"]
