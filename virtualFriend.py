from http import server
import sys
from turtle import goto
from unittest import result
from urllib import request
import speech_recognition as sr
import pyttsx3
import datetime
import os
import cv2
import time
from requests import get
import wikipedia
import webbrowser
import pywhatkit as kit
import smtplib
import pyjokes
import openai 
import requests
import pyautogui

engine = pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voices',voices[0].id)

def speak(audio):
    engine.say(audio)
    print("virtualFriend: "+audio)
    #it will print what is saying 
    engine.runAndWait()
def takecommand():
    
    r = sr.Recognizer()
    with sr.Microphone() as sourse:
        print("listening...")
        r.pause_threshole=1
        audio = r.listen(sourse,timeout=3,phrase_time_limit=5)
        try:
            print("Recognizing..........")
            query = r.recognize_google(audio,language='eng-in')
            print(f"user said : {query}")
        except Exception as e:
            speak("voice not Recognised repeat again")
            return takecommand()
    return query
def wish():
    t = time.localtime()
    current_time = time.strftime("%H:%M", t)
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning Buddy")
        speak("current time is "+current_time+" am")
    elif hour>=12 and hour<18:
        speak("good afternoon Buddy")
        speak("current time is "+current_time+"pm")
    else:
        speak("good evening Buddy")
        speak("current time is "+current_time+"pm")
    speak(" I am your personal assistant. How can I assist you today?")
    
    speak("waiting for your commant Buddy")
def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("badarinadth@gmail.com", "ygfjpxezburjrgbi") 
    server.sendmail('your mail id: ',to,content )
    server.close()


openai.api_key = os.getenv("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")

def ask_gpt(prompt):
    chat_response = openai.Completion.create(
                engine="text-davinci-003",  # Choose the appropriate engine
                prompt=user_input,
                max_tokens=50  # Adjust the token limit as needed
            )
    return response.choices[0].text.strip()



if __name__=="__main__":
    #speak("hello i am lisining ")
    #takecommand()
    wish()
    while True:
        query=takecommand().lower()
        #logic building fot the task
        
        if "open notepad" in query:
            npad="C:\\Windows\\System32\\notepad.exe"
            os.startfile(npad)

        elif  "open cmd" in query:
            comandpromit="C:\\Users\\keerthisree\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\Command Prompt.lnk"
            os.startfile(comandpromit)
        elif "open whatsapp" in query:
            whatsapp="C:\\Program Files\\WindowsApps\\5319275A.WhatsAppDesktop_2.2222.12.0_x64__cv1g1gvanyjgm\\app\\WhatsApp.exe"
            os.startfile(whatsapp)
        elif "open task manager" in query:
            Taskman="C:\\Windows\\System32\\Taskmgr.exe"
            os.startfile(Taskman)
        elif "open chrome" in query:
            chro="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(chro)
        elif "open visual studios" in query:
            vs="C:\\Users\\ASUS\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(vs)
        elif "open microsoft teams" in query:
            theams="C:\\Users\\ASUS\\AppData\\Local\\Microsoft\\Teams\\current\\Teams.exe"
            os.startfile(theams)
        elif "open kali linux" in query:
            kali="C:\\Program Files\\WindowsApps\\KaliLinux.54290C8133FEE_1.12.0.0_x64__ey8k8hqnwqnmg\\kali.exe"
            os.startfile(kali)
        elif "open ubuntu" in query:
            ubuntu="C:\\Program Files\\WindowsApps\\CanonicalGroupLimited.UbuntuonWindows_2004.2022.1.0_x64__79rhkp1fndgsc\\ubuntu.exe"
            os.startfile(ubuntu)
        elif "open camera" in query:
            speak("to close the camera press the escape key ")
            cv2.namedWindow("camera")
            vc = cv2.VideoCapture(0)
            if vc.isOpened(): # try to get the first frame
                rval, frame = vc.read()
            else:
                rval = False
            while rval:
                cv2.imshow("camera", frame)
                rval, frame = vc.read()
                key = cv2.waitKey(20)
                if key == 27: # exit on ESC
                    break
            vc.release()
            cv2.destroyWindow("camera")
        elif "play music" in query:
            music="C:\\Users\\ASUS\Music\\Video Projects"
            mu=os.listdir(music)
            os.startfile(os.path.join(music,mu[0]))
        elif "ip address" in query:
            ip=get('https://api.ipify.org').text
            speak(f"yout ip address is {ip}")
        elif "wikipedia" in query:
            speak("searching in wikipedia")
            query=query.replace("wikipedia.......","")
            result=wikipedia.summary(query,sentences=2)
            speak("according to wikipedia")
            speak(result)
            print(result)
        elif "open youtube" in query:
            webbrowser.open("www.youtube.com")
        elif "open instagram" in query:
            webbrowser.open("www.instagram.com")
        elif "open facebook" in query:
            webbrowser.open("www.facebook.com")
        elif "open google" in query:
            speak("Buddy,what should i search on google ")
            cm=takecommand().lower()
            webbrowser.open(f"{cm}")
            speak("opening google")
        elif "send a message" in query:
            
            speak("what's the contact name")
            con=takecommand().lower()
            if con=="mom":
                contact="+918341772005"
            elif con=="daddy":
                contact="+919849520615"
            elif con=="nithin":
                contact="+919398346865"
            elif con=="vikram":
                contact="+919010459235"
            elif con=="keerthi":
                contact="+916309532527"
            else:
                contact="+918374122892"
            speak("what's the message")
            mess=takecommand().lower()
            speak(mess+" is the message do you want to send it or edit")
            inp=takecommand().lower()
            hour=int(datetime.datetime.now().hour)
            minu=int((datetime.datetime.now().minute)+1)
            i=0
            while i==0:
                if inp=="send":
                    speak("ok than opening whatsapp ")
                    kit.sendwhatmsg(contact,mess,hour,minu,)
                    break
                
                else:
                    speak("repeat again")
                    mess=takecommand().lower()
                    speak(mess+" is the message do you want to send it or edit")
                    inp=takecommand().lower()
        elif "play song on youtube" in query:
            speak("what sone do you like to play")
            son=takecommand().lower()
            speak(son+" is the song do you want to play or no")
            i=0
            inp=takecommand().lower()
            while i==0:
                if inp=="play":
                    speak("ok than opening youtube ")
                    kit.playonyt(son)
                    break
                
                else:
                    speak("repeat again")
                    son=takecommand().lower()
                    speak(son+" is the song do you want to play or no ?")
                    inp=takecommand().lower()
            kit.playonyt(son)

        elif "send mail"in query:
            try:
                speak("what should i say")
                content=takecommand().lower()
                to="vechasaibadarinadh@gmail.com"
                sendEmail(to,content)
                speak("Email has send ")
            except Exception as e:
                print(e)
                speak("sorry Buddy,i am unable to send the mail")
        
        elif "close notepad" in query:
            speak("okay Buddy,closing notepad")
            os.system("taskkill /f /im notepad.exe /t")
        elif "close cmd" in query:
            speak("okay Buddy,closing cmd")
            os.system("taskkill /f /im cmd.exe /t")

        elif "tell me a joke" in query:
            joke=pyjokes.get_joke()
            speak(joke)

        elif "where am i"in query or "where i am"in query:
            speak("wait Buddy,let me check")
            try:
                ipAdd=request.get('https://api.ipify.org').text
                print(ipAdd)
                url=(f"https://get.geojs.io/v1/ip/geo/{ipAdd}.json")
                geo_requests=request.get(url)
                geo_data=geo_requests.json()
                city=geo_data["city"]
                country=geo_data["country"]
                speak(f"Buddy i am not sure,but i think we are in {city} city of {country} country")
            except Exception as e:
                speak("sorry Buddy,due to some issue i am not able to find where we are")
                pass


        elif "google bird" in query:
            response = get_google_bard_response(query)
            speak(response)

        elif "chat gpt" in query:
            user_input = takecommand().lower()
            if user_input.lower() == "exit":
                print("Personal assistant: Goodbye!")
                break
            assistant_response = ask_gpt(user_input)
            speak("Personal assistant:", assistant_response)


        elif "switch the window" in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")

        elif "move to desktop" in query:
            pyautogui.keyDown("win")
            pyautogui.press("d")
            time.sleep(1)
            pyautogui.keyUp("win")






        



        elif "shut down"in query:
            speak("thanks you Buddy,have a good day")
            sys.exit()
        speak("done Buddy,do you have any other work")

   


        