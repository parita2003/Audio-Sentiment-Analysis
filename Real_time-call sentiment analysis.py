
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import speech_recognition as sr
r=sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)
    print("Got it! Now to recognize it...")

try :
  print("printing : ")
  text=r.recognize_google(audio,language='en-US')
  print("your message : {}".format(text))
except Exception as e:
  print("Error : {}".format(e))

sentence=[str(text)]
analyser=SentimentIntensityAnalyzer()
sentiment=analyser.polarity_scores(sentence)
print("sentiment score  : ",sentiment)