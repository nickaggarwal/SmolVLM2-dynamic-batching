INPUT_SCHEMA = {
    "prompt": {
        'datatype': 'STRING',
        'required': True,
        'shape': [1, 1],
        'example': [["There is a fine house in the forest"]],
    }
}
BATCH_SIZE = 4
BATCH_WINDOW = 5000
