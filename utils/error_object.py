import json

def error_object(text):
    """
    Encapsulates an error text into an object
    """
    return json.dumps({'error': text})