import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"Content-Type": "application/json",
               "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    data = json.dumps({"raw_document": {"text": text_to_analyze}})

    try:
        response = requests.post(url, headers=headers, data=data)
        if response.status_code == 400:
            return {
                'anger': None,
                'disgust': None,
                'fear': None,
                'joy': None,
                'sadness': None,
                'dominant_emotion': None
            }
        response_json = response.json()
        emotions = response_json['emotionPredictions'][0]['emotion']
        dominant_emotion = max(emotions, key=emotions.get)

        return {
            'anger': emotions['anger'],
            'disgust': emotions['disgust'],
            'fear': emotions['fear'],
            'joy': emotions['joy'],
            'sadness': emotions['sadness'],
            'dominant_emotion': dominant_emotion
        }
    except Exception as e:
        # In case of exception (network error, invalid response), return fallback
        print("Request failed:", e)
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
