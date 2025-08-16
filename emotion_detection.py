
import requests  # Import the requests library to handle HTTP requests

def emotion_detector(text_to_analyse):  # Define a function named  that takes a string input (text_to_analyse)
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict' # URL of the emotion detection service
    myobj = { "raw_document": { "text": text_to_analyse } }  # Create a dictionary with the text to be analyzed
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}  # Set the headers required for the API request
    response = requests.post(url, json = myobj, headers=header)  # Send a POST request to the API with the text and headers
    # Parsing the JSON response from the API
    formatted_response = json.loads(response.text)
    # Extracting from the response
    anger_score = formatted_response['anger']['anger_score']
    disgust_score = formatted_response['disgust']['disgust_score']
    fear_score = formatted_response['fear']['fear_score']
    joy_score = formatted_response['joy']['joy_score']
    sadness_score = formatted_response['sadness']['sadness_score']
    dominant_emotion = formatted_response['joy']['dominant_emotion']
    # Returning a dictionary containing results
    return {'label': label, 'score': score}