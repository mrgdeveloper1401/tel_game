FROM tel_game:1.0.0

WORKDIR /app

COPY . .

RUN adduser -D -H tel_game && \
    chmod +x ./scripts/* && \
    chown -R tel_game:tel_game /app

EXPOSE 8000

ENTRYPOINT ["sh", "-c", "/app/scripts/dj_start.sh"]