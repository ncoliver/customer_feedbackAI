from EmotionDetection.emotion_detection import *
import unittest

class TestEmotionDetector(unittest.TestCase):
    
    def test_emotion_detector(self):
        emotion_dict = emotion_detector("I am glad this happened")
        dominant_result = max(emotion_dict, key=emotion_dict.get)
        self.assertEqual(dominant_result, 'joy')

        emotion_dict = emotion_detector("I am really mad about this")
        dominant_result = max(emotion_dict, key=emotion_dict.get)
        self.assertEqual(dominant_result, 'anger')

        emotion_dict = emotion_detector("I feel disgusted just hearing about this")
        dominant_result = max(emotion_dict, key=emotion_dict.get)
        self.assertEqual(dominant_result, 'disgust')

        emotion_dict = emotion_detector("I am so sad about this")
        dominant_result = max(emotion_dict, key=emotion_dict.get)
        self.assertEqual(dominant_result, 'sadness')

        emotion_dict = emotion_detector("I am really afraid that this will happen")
        dominant_result = max(emotion_dict, key=emotion_dict.get)
        self.assertEqual(dominant_result, 'fear')

unittest.main()

        