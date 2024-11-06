FROM minio/minio:RELEASE.2023-03-20T20-16-18Z

ENV MINIO_ACCESS_KEY=minioadmin
ENV MINIO_SECRET_KEY=minioadmin

EXPOSE 9000
EXPOSE 9001

CMD ["minio", "server", "/minio_data", "--console-address", ":9001"]