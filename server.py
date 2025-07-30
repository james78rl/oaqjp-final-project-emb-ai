"""
Flask web application for emotion detection using Watson NLP API.
"""

from flask import Flask, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector", methods=["POST"])
def detect_emotion():
    """
    Endpoint that receives a POST request with input text,
    performs emotion detection, and returns a formatted response.
    """
    text_to_analyze = request.form.get("text")

    if not text_to_analyze:
        return "Invalid text! Please try again!", 400

    result = emotion_detector(text_to_analyze)

    if result["dominant_emotion"] is None:
        return "Invalid text! Please try again!", 400

    formatted_response = (
        f"For the given statement, the system response is 'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, 'fear': {result['fear']}, "
        f"'joy': {result['joy']} and 'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )
    return formatted_response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
