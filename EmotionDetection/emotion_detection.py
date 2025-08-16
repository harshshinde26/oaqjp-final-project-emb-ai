import requests
import json

def emotion_detector(text_to_analyze):
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(URL, json=input_json, headers=header)

    
    print("Raw API Response:", response.text)

    formated_response = json.loads(response.text)

    if response.status_code == 200:
        
        anger_score, disgust_score, fear_score, joy_score, sadness_score = 0, 0, 0, 0, 0
        
        
        for mention in formated_response.get('emotionPredictions', []):
            for mention_info in mention.get('emotionMentions', []):
                anger_score += mention_info.get('emotion', {}).get('anger', 0)
                disgust_score += mention_info.get('emotion', {}).get('disgust', 0)
                fear_score += mention_info.get('emotion', {}).get('fear', 0)
                joy_score += mention_info.get('emotion', {}).get('joy', 0)
                sadness_score += mention_info.get('emotion', {}).get('sadness', 0)

        
        emotions = {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score
        }

        
        dominant_emotion = max(emotions, key=emotions.get)

        
        return {
            **emotions,
            'dominant_emotion': dominant_emotion
        }

    elif response.status_code == 400:
        
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }


if __name__ == "__main__":
    sample_text = "I am so happy today! Everything is going great and I feel amazing."
    
    
    result = emotion_detector(sample_text)

    
    print(json.dumps(result, indent=4))

