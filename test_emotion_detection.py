import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_joy(self):
        text = "I am glad this happened."
        result_1 = emotion_detector(text)
        self.assertEqual(result_1['dominant_emotion'], 'joy')

    def test_emotion_anger(self):
        text = "I am really mad about this."
        result_2 = emotion_detector(text)
        self.assertEqual(result_2['dominant_emotion'], 'anger')

    def test_emotion_disgust(self):
        text = "I feel disgusted just hearing about this."
        result_3 = emotion_detector(text)
        self.assertEqual(result_3['dominant_emotion'], 'disgust')

    def test_emotion_sadness(self):
        text = "I am so sad about this."
        result_4 = emotion_detector(text)
        self.assertEqual(result_4['dominant_emotion'], 'sadness')

    def test_emotion_fear(self):
        text = "I am really afraid that this will happen."
        result_5 = emotion_detector(text)
        self.assertEqual(result_5['dominant_emotion'], 'fear')

if __name__ == '__main__':
    unittest.main()
