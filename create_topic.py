from confluent_kafka.admin import AdminClient, NewTopic

n_repicas = 1
n_partitions = 3

admin_client = AdminClient({
    "bootstrap.servers": "localhost:9092"
})

topic_list = []
topic_list.append(NewTopic("multi-video-stream", n_partitions, n_repicas))
fs = admin_client.create_topics(topic_list)

for topic, f in fs.items():
    try:
        f.result()  # The result itself is None
        print("Topic {} created".format(topic))
    except Exception as e:
        print("Failed to create topic {}: {}".format(topic, e))