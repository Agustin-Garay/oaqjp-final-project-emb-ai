from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("emotionDetector")

@app.route("/")
def render_index_page():
    return render_template('index.html')

@app.route("/emotionDetector")
def emo_detector():
    text_to_analyse = request.args.get("textToAnalyze")
    response = emotion_detector(text_to_analyse)
    anger = str(response["anger"])
    disgust = str(response["disgust"])
    fear = str(response["fear"])
    joy = str(response["joy"])
    sadness = str(response["sadness"])
    dominant = str(response["dominant_emotion"])
    return "For the given statement, the system response is 'anger': {}, 'disgust': {}, 'fear': {}, 'joy': {} and 'sadness': {}. The dominant emotion is {}.".format(anger, disgust, fear, joy, sadness, dominant)

if __name__ == "__main__":
    app.run(port=5000)
