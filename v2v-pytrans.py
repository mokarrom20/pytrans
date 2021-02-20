########################################MADE BY Mokarrom Hossain [i think]

#PEWPEW
#Project name: v2v-Pytrans
#Description : Please install these following modules and while running please use microphone

####modules
#googletrans for translating
#gTTS for text to speech
#pyaudio for audio management
#playsound for playing audio
#speech recognition for speech input

from googletrans import Translator
from gtts import gTTS
import playsound
import speech_recognition as sr


#YESSSSSSSS!!!!!!!!! PEWPEW

def trn(frm,intext,des):
    #frm = from lang | intext = the text to translate | des = destination lang :)
    outext = Translator().translate(intext, src = frm, dest = des).text
    return outext

def texttospeech(text, lang):
    #code to speak
    tts = gTTS(text = text , lang = lang)
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)

def speechtotext(lang):
    #Code to recognize speech
    rec = sr.Recognizer()
    rec.energy_threshold = 4000
    with sr.Microphone() as source :
        audio = rec.listen(source)
        told = ""
        try :
            told = rec.recognize_google(audio , language = lang)
            print("\nTranslating : "+ told)
        except Exception as ex :
            print("Problem" + str(ex))
    return told

def main():
    #selecting language
    print("Arabic : ar \nBangla : bn \nEnglish : en \nFrench : fr \nHindi : hi")
    frmlang = input("Translate from : " + str())
    tolang = input("Translate to : " + str())
    
    texttotrans = speechtotext(frmlang)
    
    #the main transform
    translated = trn(frmlang,texttotrans, tolang)
    texttospeech(translated, tolang)
    print("Translation : " + translated)

main() #calling main func
