import logging
import cv2

from pymongo.errors import BulkWriteError

# logging.warning('This will get logged to a file')
logging.basicConfig(level=logging.INFO, format='%(name)s - %(levelname)s - %(message)s')

def delivery_report(err, msg):
    if err:
        logging.error("Failed to deliver message: {0}: {1}"
              .format(msg.value(), err.str()))
    else:
        logging.info(f"msg produced. \n"
                    f"Topic: {msg.topic()} \n" +
                    f"Partition: {msg.partition()} \n" +
                    f"Offset: {msg.offset()} \n" +
                    f"Timestamp: {msg.timestamp()} \n")
                    
def serializeImg(img):
    _, img_buffer_arr = cv2.imencode(".jpg", img)
    img_bytes = img_buffer_arr.tobytes()
    return img_bytes
    
def reset_map(_dict):
    for _key in _dict:
        _dict[_key] = []
    return _dict

def create_collections_unique(db, video_names):
    videos_map = {}
    for video in video_names:
        video_collection = db[video]
        video_collection.create_index("frame", unique=True)
        videos_map.update({video: []})
    return videos_map

def insert_data_unique(db, videos_map):
    for video, docs in videos_map.items():
        video_collection = db[video]
        try:
            _result = video_collection.insert_many(docs)
            print('Multiple Documents have been inserted.')
            for doc_id in _result.inserted_ids:
                print(doc_id)
            print()
        except BulkWriteError:
            print("Batch Contains Duplicate")
            for doc in docs:
                if video_collection.find_one({"frame": doc["frame"]}) != None:
                    continue
                video_collection.insert_one(doc)
        except Exception as e:
            print("Error Occured.")
            print(e)
            print(docs)
            pass

