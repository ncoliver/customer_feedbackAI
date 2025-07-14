import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyze } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    response = requests.post(url, json=myobj, headers=header)
    formatted_response = json.loads(response.text)
    
    emotion_labels = ['anger', 'disgust', 'joy', 'fear', 'sadness', 'dominant']
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    emotion_scores = {}

    for label in emotion_labels:
        if label != 'dominant':
            score = emotions[label]
            emotion_scores[label] = score
        else:
            dominant_emotion = max(emotion_scores, key=emotion_scores.get)
            emotion_scores['dominant'] = dominant_emotion

        
    return f"""
    For the given statement, the system response is 
    'anger': {emotion_scores['anger']},
    'disgust': {emotion_scores['disgust']}, 
    'fear': {emotion_scores['fear']}, 
    'joy': {emotion_scores['joy']}, 
    'sadness': {emotion_scores['sadness']}. 
    The dominant emotion is {emotion_scores['dominant']}.
    """
