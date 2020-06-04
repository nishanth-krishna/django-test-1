import pyttsx3 
import speech_recognition as sr

from twilio.rest import Client

from PyDictionary import PyDictionary




def jarvis_says( talk ):
    converter = pyttsx3.init() 

    converter.setProperty('rate', 200) 

    converter.setProperty('volume', 0.7) 

    voice_id = "com.apple.speech.synthesis.voice.Alex"


    converter.setProperty('voice', voice_id) 

    converter.runAndWait() 


    converter.say( talk ) 
    #converter.say("How can i help you") 

    converter.runAndWait() 




dictionary = PyDictionary()

r = sr.Recognizer()
with sr.Microphone() as source:

    print("Speak Anything :")
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print("You said : {}".format(text))
    except:
        print("Sorry could not recognize what you said")

textme = text
if 'Jarvis' in textme:

    jarvis_says("Hello. How can i help you")

    with sr.Microphone() as source:

        print("Speak Anything :")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print("You said : {}".format(text))
        except:
            print("Sorry could not recognize what you said")

        textmeagain = text
        contacts = {'Krishna':"+919000683024", 'Jyoti':"+919949418372"}

        if 'how are you' in textmeagain:
            jarvis_says("i am fine sir, thank you for asking")

            print("Speak Anything :")
            audio = r.listen(source)
            try:
                text = r.recognize_google(audio)
                print("You said : {}".format(text))
            except:
                print("Sorry could not recognize what you said")

            textmeagain = text

        if 'do you believe in God' in textmeagain:
            jarvis_says("mister nishanth created me, he is my god, so yes, i believe in god")

            print("Speak Anything :")
            audio = r.listen(source)
            try:
                text = r.recognize_google(audio)
                print("You said : {}".format(text))
            except:
                print("Sorry could not recognize what you said")

            textmeagain = text            

        if 'who are you' in textmeagain:
            jarvis_says('i am jarvis, a personal assistant')

            print("Speak Anything :")
            audio = r.listen(source)
            try:
                text = r.recognize_google(audio)
                print("You said : {}".format(text))
            except:
                print("Sorry could not recognize what you said")

            textmeagain = text

        if 'call Krishna' in textmeagain:

                string = 'call Krishna'

                words = string.split()
                name = words[1]

                jarvis_says("Calling Krishna in a moment")


                account_sid = 'ACc7df3cbbd2bf9a13174217041dc2a196'
                auth_token = '0e0586de7930abf31ac7e2b3bd397c08'
                client = Client(account_sid, auth_token)

                call = client.calls.create(
                        twiml='<Response><Say>Hello, this is your smart assistant</Say></Response>',
                        to=contacts[name],
                        from_='+12067361389'
                    )

                print(call.sid)

        if 'call Jyoti' in textmeagain:

                string = 'call Jyoti'

                words = string.split()
                name = words[1]

                jarvis_says("Calling Jyoti in a moment")


                account_sid = 'ACc7df3cbbd2bf9a13174217041dc2a196'
                auth_token = '0e0586de7930abf31ac7e2b3bd397c08'
                client = Client(account_sid, auth_token)

                call = client.calls.create(
                        twiml='<Response><Say>Hi Krishna, this is E.D.I.T.H, your smart assistant</Say></Response>',
                        to=contacts[name],
                        from_='+12067361389'
                    )

                print(call.sid)       

        if 'meaning of' in textmeagain:
            var = textmeagain.split()
            myword = var[2]
            mng = dictionary.meaning(myword)
            for key in mng.keys():
	            k = mng.get(key)
	            val = str((k[0]))

            jarvis_says("the meaning of "+ myword +" is "+ val)
            print("the meaning of "+ myword +" is "+ val)




        
        

                
                






