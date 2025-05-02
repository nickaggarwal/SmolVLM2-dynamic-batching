INPUT_SCHEMA = {
    "prompt": {
        'datatype': 'STRING',
        'required': True,
        'shape': [1],
        'example': ["Describe the video"],
    },
    "video_file": {
        'datatype': 'STRING',
        'required': True,
        'shape': [1],
        'example': ["https://file-examples.com/wp-content/storage/2017/04/file_example_MP4_640_3MG.mp4"],
    }
}
BATCH_SIZE = 4
BATCH_WINDOW = 5000
