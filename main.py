import os
import pandas as pd
from pydub import AudioSegment
from gtts import gTTS

def textToSpeech_hindi(text,filename):
    mytext = str(text)
    language = 'hi'
    myobj = gTTS(text=mytext,lang = language,slow=False)
    myobj.save(filename)

def textToSpeech_English(text,filename):
    mytext = str(text)
    language = 'en'
    myobj = gTTS(text=mytext,lang = language,slow=False)
    myobj.save(filename)

def mergeAudios(audios):
    combined = AudioSegment.empty()
    for audio in audios:
        combined += AudioSegment.from_mp3(audio)
    return combined

def generateSkeletonHindi():
    audio = AudioSegment.from_mp3('railway.mp3')

    # Slicing the audio

    # 1. Kripiya Dhyan dijiye
    start = 88000
    finish = 90200
    audioProcessed = audio[start:finish]
    audioProcessed.export("1_hindi.mp3",format="mp3")

    # 2. From city

    # 3. Se chalkar
    start = 91000
    finish = 92200
    audioProcessed = audio[start:finish]
    audioProcessed.export("3_hindi.mp3",format="mp3")

    # 4. via-city

    # 5. ke raaste
    start = 94000
    finish = 95000
    audioProcessed = audio[start:finish]
    audioProcessed.export("5_hindi.mp3", format="mp3")

    # 6. to-city

    # 7. Generate ko jaane wali gaadi sakhya
    start = 96000
    finish = 98900
    audioProcessed = audio[start:finish]
    audioProcessed.export("7_hindi.mp3", format="mp3")

    # 8. train no and name

    # 9. Generate kuch hi samay mei platform sankhya
    start = 105500
    finish = 108200
    audioProcessed = audio[start:finish]
    audioProcessed.export("9_hindi.mp3", format="mp3")

    # 10. platform number

    # 11. Generate par aa rahi hai
    start = 109000
    finish = 112250
    audioProcessed = audio[start:finish]
    audioProcessed.export("11_hindi.mp3", format="mp3")


def generateSkeletonEnglish():
    audio = AudioSegment.from_mp3('railway.mp3')

    # Slicing the audio

    # 1. May I have ur attention please
    start = 64900
    finish = 69900
    audioProcessed = audio[start:finish]
    audioProcessed.export("1_English.mp3",format="mp3")

    # 2. train number

    # 3. from
    start = 76000
    finish = 77000
    audioProcessed = audio[start:finish]
    audioProcessed.export("3_English.mp3",format="mp3")

    # 4. city name
    # 5. to
    # 6. cityname 

    # 7. via 
    start = 80000
    finish = 80900
    audioProcessed = audio[start:finish]
    audioProcessed.export("7_English.mp3", format="mp3")

    # 8. city name

    # 9. arriving on platform number 
    start = 82500
    finish = 86500
    audioProcessed = audio[start:finish]
    audioProcessed.export("9_English.mp3", format="mp3")

    # 10. platform number

def generateAnnouncementHindi(filename):
    df = pd.read_excel(filename)
    
    for index, item in df.iterrows():
        #2
        textToSpeech_hindi(item['from'],'2_hindi.mp3')

        # 4
        textToSpeech_hindi(item['via'], '4_hindi.mp3')

        # 6 
        textToSpeech_hindi(item['to'], '6_hindi.mp3')

        # 8
        textToSpeech_hindi(item['train_no'] + " " + item['train_name'], '8_hindi.mp3')

        # 10
        textToSpeech_hindi(item['platform'], '10_hindi.mp3')

        audios = [f"{i}_hindi.mp3" for i in range(1,12)]
        announcement = mergeAudios(audios) 
        announcement.export(f"annoucement_{item['train_no']}_{index+1}.mp3",format="mp3")

def generateAnnouncementEnglish(filename):
    df = pd.read_excel(filename)
    
    for index, item in df.iterrows():
        #2 
        textToSpeech_English(item['train_no'],'2_English.mp3')

        #4
        textToSpeech_English(item['from'],'4_English.mp3')

        #5
        textToSpeech_English('to','5_English.mp3')

        #6
        textToSpeech_English(item['to'],'6_English.mp3')

        #8
        textToSpeech_English(item['via'],'8_English.mp3')

        #10
        textToSpeech_English(item['platform'],'10_English.mp3')

        audios = [f"{i}_English.mp3" for i in range(1,11)]
        announcement = mergeAudios(audios) 
        announcement.export(f"annoucement_{item['train_no']}_{index+1}_English.mp3",format="mp3")


if __name__ == '__main__':
    print("Generating Skeleton....")
    generateSkeletonHindi()
    generateSkeletonEnglish()
    print("Now Generating Announcement...")
    generateAnnouncementHindi("announce_hindi.xlsx")
    generateAnnouncementEnglish("announce_hindi.xlsx")
