# Distributed Multi-video processing pipeline with Python and Confluent Kafka

![Imgur](https://i.imgur.com/2VLII4L.png)

Stream and process multiple videos in near real time using Kafka. The video frames are processed and a machine learning model does inference on them and the results are stored in a mongodb database.
### Install Dependencies
```
pip install -r requirements.txt
```
### Run the Application
Before Running, you have to start MongoDB and Kafka Server Instance.
#### Run Producer Application
```
python producer_app.py
```
#### Run Consumer Application
```
python consumer_app.py
```
### Associated Article
you can go through the [medium article](https://medium.com/@ms.neerajkrishna/kafka-in-action-building-a-distributed-multi-video-processing-pipeline-with-python-and-confluent-9f133858f5a0) for more details
