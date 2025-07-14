# Import required libraries
from flask import Flask, render_template, request
# Import the emotion_detetor function from the package created:
from EmotionDetection.emotion_detection import emotion_detector

# Initiate the flask app
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():
    """This code receives the text from the HTML web interface and
    runs emotion detector over it using emotion_detector() function. 
    The output returned shows the label and its confidence score for
    the provided text.
    """
    # Retrieve the text to analyze form the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the emotion detector functiont to store the response
    response = emotion_detector(text_to_analyze)

    # Extract 
    return response



@app.route("/")
def render_index_page():
    """This function initiated the rendering of the main applicatoin
    page over that Flask channel """
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)