''' Testing for the Emotion Detection module, to ensure correct functionality.
'''
import unittest
from emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    ''' Testing Class for the Emotion Detection Module.
    '''
    def test_joy(self):
        '''Test Function to determine if the emotion "joy" is working as intended.'''
        dominant_emotion = emotion_detector('I am glad this happened')
        self.assertEqual(dominant_emotion['dominant_emotion'], 'joy')

    def test_anger(self):
        '''Test Function to determine if the emotion "anger" is working as intended.'''
        dominant_emotion = emotion_detector('I am really mad about this')
        self.assertEqual(dominant_emotion['dominant_emotion'], 'anger')

    def test_disgust(self):
        '''Test Function to determine if the emotion "disgust" is working as intended.'''
        dominant_emotion = emotion_detector('I feel disgusted just hearing about this')
        self.assertEqual(dominant_emotion['dominant_emotion'], 'disgust')

    def test_sadness(self):
        '''Test Function to determine if the emotion "sadness" is working as intended.'''
        dominant_emotion = emotion_detector('I am so sad about this')
        self.assertEqual(dominant_emotion['dominant_emotion'], 'sadness')

    def test_fear(self):
        '''Test Function to determine if the emotion "fear" is working as intended.'''
        dominant_emotion = emotion_detector('I am really afraid that this will happen')
        self.assertEqual(dominant_emotion['dominant_emotion'], 'fear')

if __name__ == '__main__':
    unittest.main()
