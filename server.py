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

    
    if not response:
        return "Invalid input! Try again"
    
    try:
        dominant_emotion = max(response, key=response.get)
    except (ValueError, TypeError):
            return "Invalid input! Could not determine dominant emotion."
    
    if dominant_emotion:
        output = {}
        for emotion, score in response.items():
            output[emotion] = score

        output["dominant_emotion"] = str(dominant_emotion)
        output_response = f"""
        For the given statement, the system response is:\n
        'anger': {output['anger']}\n
        'disgust': {output['disgust']},\n
        'fear': {output['fear']},\n
        'joy': {output['joy']},\n
        'sadness': {output['sadness']},\n
        'dominant_emotion': <strong>{output['dominant_emotion']}</strong>
        """
        return output_response
            
    else:
        return "Invalid input"
        

@app.route("/")
def render_index_page():
    """This function initiated the rendering of the main applicatoin
    page over that Flask channel """
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)