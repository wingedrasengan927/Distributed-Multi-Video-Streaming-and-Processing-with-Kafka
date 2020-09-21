config = {
    'bootstrap.servers': '127.0.0.1:9092',
    'group.id': 'kafka-multi-video-stream',
    'enable.auto.commit': False,
    'default.topic.config': {'auto.offset.reset': 'earliest'}
}