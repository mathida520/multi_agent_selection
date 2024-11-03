FROM quay.io/coreos/etcd:v3.5.5

ENV ETCD_AUTO_COMPACTION_MODE=revision
ENV ETCD_AUTO_COMPACTION_RETENTION=1000
ENV ETCD_QUOTA_BACKEND_BYTES=4294967296
ENV ETCD_SNAPSHOT_COUNT=50000

# EXPOSE 2379

CMD ["etcd", "-advertise-client-urls=http://127.0.0.1:2379", "-listen-client-urls", "http://0.0.0.0:2379", "--data-dir", "/etcd"]