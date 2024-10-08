'''Executing Emotion Detector application on localhost and display response
'''
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector
app = Flask("Emotion Detection")

@app.route("/")
def index_page():
    '''display default webpage
    '''
    return render_template('index.html')

@app.route("/emotionDetector")
def emoti_detector():
    '''This function takes input text and analyzes its emotion value and displays dominant emotion
    '''
    result_text  = request.args.get('textToAnalyze')
    result = emotion_detector(result_text)
    if result['dominant_emotion'] is None:
        return "Invalid text! Please try again."
    return f"""For the given statement, the system response is 'anger': {result['anger']},
    disgust': {result['disgust']}, 'fear': {result['fear']}, 'joy': {result['joy']},
    'sadness': {result['sadness']}. The dominant emotion is {result['dominant_emotion']}"""

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
    