''' This module contains the server and routes, to run the NLP - Emotion Detection.
    When this module is ran it starts the server, and enables connectivity to WATSON for the NLP.
    The flask application is deployed on localhost:5000
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection App")

@app.route('/')
def render_index():
    '''Route to render the main index.html webpage.'''
    return render_template("index.html")

@app.route('/emotionDetector')
def emotion_detection():
    ''' Route to send text to be analyzed, by the Emotion Detection.
        If text is empty, or there is no dominant emotion, we return an error.
    '''
    text_to_analyze = request.args.get('textToAnalyze')
    emotion_dict = emotion_detector(text_to_analyze)

    if emotion_dict['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    return f"For the given statement, the system response is 'anger': {emotion_dict['anger']} , \
        'disgust': {emotion_dict['disgust']}, 'fear': {emotion_dict['fear']}, \
            'joy': {emotion_dict['joy']} and 'sadness': {emotion_dict['sadness']}. \
                The dominant emotion is {emotion_dict['dominant_emotion']}."

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 5000, debug=True)
