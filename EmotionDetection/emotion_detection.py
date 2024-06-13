import requests
import json
def emotion_detector(text_to_analyse):
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    HEADERS = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    json_input = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(URL,headers=HEADERS,data=json.dumps(json_input))
    if (response.status_code == 400):
        return {'anger': None,
                'disgust': None,
                'fear':None,
                'joy':None,
                'sandess':None,
                'dominant_emotion':None}
    
    emotions = json.loads(response.text)
    emotions = emotions['emotionPredictions']
    emotions = emotions[0]
    emotions = emotions['emotion']
    dominant_emotion = ''
    dominant_score = 0
    for emotion, score in emotions.items():
        if score > dominant_score:
            dominant_score = score
            dominant_emotion = emotion
    emotions['dominant_emotion'] = dominant_emotion
    return emotions