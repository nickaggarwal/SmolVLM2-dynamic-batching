INPUT_SCHEMA = {
    "prompt": {
        'datatype': 'STRING',
        'required': True,
        'shape': [1],
        'example': ["Describe the video"],
    },
    "video_url": {
        'datatype': 'STRING',
        'required': True,
        'shape': [1],
        'example': ["http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ElephantsDream.mp4"],
    }
}
BATCH_SIZE = 4
BATCH_WINDOW = 5000
