#from django.http import HttpResponse
from django.template import loader
from email import message
from django.shortcuts import render
from django.http import HttpResponse
import datetime as dt
from . import models
import cv2
import numpy as np
from tensorflow import keras
#import keyboard
import openai
import time
from django.shortcuts import render
import numpy
from django.http import HttpResponse
from scipy import stats
#import googletrans
db={}
# Create your views here.
import cv2
import numpy as np
from statistics import mode
import time

# Load the emotion recognition model
emotion_model = keras.models.load_model("app/emotion_recognition_model.h5")

# Define the emotions list corresponding to model output classes
emotions = ["angry", "disgust", "fear", "happy", "sad", "surprise", "neutral"]

# Function to detect and recognize emotions from frames
def detect_emotion(frame):
    # Convert grayscale frame to RGB (replicate the single channel three times)
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_GRAY2RGB)

    # Preprocess the frame
    resized_frame = cv2.resize(frame_rgb, (48, 48))
    input_frame = np.expand_dims(resized_frame, axis=0)
    input_frame = input_frame.astype("float32") / 255.0

    # Predict the emotion
    predictions = emotion_model.predict(input_frame)
    predicted_class = np.argmax(predictions[0])
    predicted_emotion = emotions[predicted_class]

    return predicted_emotion

def emotion(request):
    camera = cv2.VideoCapture(0)

    while True:
        ret, frame = camera.read()
        if not ret:
            break

        # Convert the frame to grayscale
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces in the frame
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        # If faces are detected, detect emotions
        if len(faces) > 0:
            lst = []
            # For each detected face, recognize emotions
            for (x, y, w, h) in faces:
                face_roi = gray_frame[y:y+h, x:x+w]
                predicted_emotion = detect_emotion(face_roi)
                lst.append(str(predicted_emotion))

                # Draw a rectangle around the detected face
                cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

            np_emotions = np.array(lst)
            predicted_emotion = mode(np_emotions).mode[0]

            camera.release()
            cv2.destroyAllWindows()

            return str(predicted_emotion)

        # Display the frame
        cv2.imshow("Emotion Recognition", frame)

        # Press 'q' to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    camera.release()
    cv2.destroyAllWindows()
openai.api_key = "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"
def get_response(request,chat_text):
    # Assuming 'emotion' is a function that extracts emotion from the request
    emot=emotion(request)
    
    # Use openai.ChatCompletion.create for chat models
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-1106",
        messages=[
            {"role": "system", "content": "I am " + emot + " " + chat_text}
        ],
        temperature=0.7,
        max_tokens=100,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
    
    return str(response['choices'][0]['message']['content'])
def chat(request):
    
    user_input=request.GET['chat']
    response = get_response(request,user_input)
    print(response)
    res=response.replace(" ","_")
    print(res)
    return render(request,'chatter.html',context={
        'res':res,
        'lang':request.GET['destlangu']
    })
def members(request,id):
  return render(request,'chatter.html')
