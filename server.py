"""Flask Server App."""
from flask import Flask, render_template, request
from EmotionDetection import emotion_detection

app = Flask(__name__)

@app.route('/emotionDetector')
def emotion_detector():
    """flask routing"""
    if 'textToAnalyze' not in request.args:
        return render_template('index.html')

    text = request.args.get('textToAnalyze')
    result = emotion_detection.emotion_detector(text)
    if result['dominant_emotion'] is None:
        return "Invalid text! Please try again!."

    return f"For the given statement, the system response is 'anger': {result['anger']}, \
            'disgust': {result['disgust']}, 'fear': {result['fear']}, 'joy': {result['joy']} and \
            'sadness': {result['sadness']}. The dominant emotion is {result['dominant_emotion']}."

if __name__ == '__main__':
    app.run()
