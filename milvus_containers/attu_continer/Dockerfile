FROM zilliz/attu:v2.3.6
RUN apt-get update && apt-get install -y curl
WORKDIR /app

ENV MILVUS_URL=http://standalone:19530
ENV HOST_URL=http://127.0.0.1:8000
ENV NODE_VERSION=18.19.0
ENV YARN_VERSION=1.22.19

EXPOSE 3000

ENTRYPOINT ["docker-entrypoint.sh", "/bin/bash", "-c", "/app/build/env.sh && yarn start:prod"]