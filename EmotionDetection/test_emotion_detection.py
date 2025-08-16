import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionPredictor(unittest.TestCase):

    def test_joy_emotion(self):
        test_text = "I am glad this happened"
        result = emotion_detector(test_text)
        # Check whether the dominant emotion is 'joy'
        self.assertEqual(result['dominant_emotion'], 'joy')

    def test_anger_emotion(self):
        test_text = "I am really mad about this"
        result = emotion_detector(test_text)
        # Check whether the dominant emotion is 'anger'
        self.assertEqual(result['dominant_emotion'], 'anger')

    def test_disgust_emotion(self):
        test_text = "I feel disgusted just hearing about this"
        result = emotion_detector(test_text)
        # Check whether the dominant emotion is 'disgust'
        self.assertEqual(result['dominant_emotion'], 'disgust')

    def test_sadness_emotion(self):
        test_text = "I am so sad about this"
        result = emotion_detector(test_text)
        # Check whether the dominant emotion is 'sadness'
        self.assertEqual(result['dominant_emotion'], 'sadness')

    def test_fear_emotion(self):
        test_text = "I am really afraid that this will happen"
        result = emotion_detector(test_text)
        # Check whether the dominant emotion is 'fear'
        self.assertEqual(result['dominant_emotion'], 'fear')

if __name__ == "__main__":
    unittest.main()
