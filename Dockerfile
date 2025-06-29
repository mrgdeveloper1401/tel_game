FROM tel_game:2.0.0

WORKDIR /app

COPY . .

RUN adduser -D -H tel_game && \
    pip install colorlog && \
    pip install psycopg2-binary && \
    chmod +x ./scripts/* && \
    chown -R tel_game:tel_game /app

EXPOSE 8000

ENTRYPOINT ["sh", "-c", "/app/scripts/dj_start.sh"]