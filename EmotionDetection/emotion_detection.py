''' This module contains the functionality to connect to WATSON,
    with the text provided by the client.
'''
import json
import requests

def emotion_detector(text_to_analyze):
    ''' This function sends text to be analyzed by the 
        Emotion Prediction function of the Watson NLP Library.
    '''
    # URL for Watson NLP Library.
    url = 'https://' \
    'sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Headers to access proper model.
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Payload with the text to be analyzed.
    payload = { "raw_document": { "text": text_to_analyze } }

    # Make a POST request to WATSON with payload, and headers.
    response = requests.post(url, headers=headers, json=payload, timeout=5000)

    # Error handling to handle blank entries from users.
    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    # Format response into JSON
    formatted_response = json.loads(response)

    # Set up a blank dictionary for the formatted return response.
    emotion_scores = {}

    # Set up default values for 'dominant_emotion', and score,
    # to calculate which is the dominant emotion.
    dominant_emotion = ''
    dominant_emotion_score = 0

    # Iterate through each emotion, get its prediction,
    # format it, and add it to the 'emotion_scores' dictionary.
    for _ in formatted_response['emotionPredictions'][0]['emotion']:
        emotion_scores[f'{_}_score'] = formatted_response['emotionPredictions'][0]['emotion'][_]

    # Iterate through each emotion in the previous setup emotion scores dictionary.
    for k, v in emotion_scores.items():
        # If the value of the current emotion, is larger then the dominant emotion value
        # replace it as the new dominant emotion.
        if v > dominant_emotion_score:
            dominant_emotion_score = v
            dominant_emotion = k.split('_')[0]

    # Return response as JSON.
    return {
        'anger': emotion_scores['anger_score'],
        'disgust': emotion_scores['disgust_score'],
        'fear': emotion_scores['fear_score'],
        'joy': emotion_scores['joy_score'],
        'sadness': emotion_scores['sadness_score'],
        'dominant_emotion': dominant_emotion
    }
