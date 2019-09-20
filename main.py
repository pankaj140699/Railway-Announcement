import os #operating system module it is built in module so dont need to install by pip
import pandas as pand
from pydub import AudioSegment
from gtts import gTTS
import xlrd
#pip install pyaudio
#pip install pydub
#pip install pandas
#pip insatll gTTS
#pip install xlrd
def generateSkeleton():
    #read railway.mp3
    audio=AudioSegment.from_mp3('railway.mp3')
    #1genereate yatrigan kripaya dyan de
    start=87000 # in millisecond
    finish=90200 # in miilisecond
    audioProcessed=audio[start:finish]
    audioProcessed.export('1_hindi.mp3',format='mp3')
    #2. from
    #3. se chlkar
    start=91000
    finish=92000
    audioProcessed=audio[start:finish]
    audioProcessed.export('3_hindi.mp3',format='mp3')
    #4. via
    #5. ke raste
    start=94000
    finish=95000
    audioProcessed=audio[start:finish]
    audioProcessed.export('5_hindi.mp3',format='mp3')    
    #6.to
    #7. ko jane wali gaadi sankhya
    start=3400
    finish=6600
    audioProcessed=audio[start:finish]
    audioProcessed.export('7_hindi.mp3',format='mp3')
    #8. tarin no
    #9. train name
    #10. platform no 
    start=13000
    finish=16000
    audioProcessed=audio[start:finish]
    audioProcessed.export('10_hindi.mp3',format='mp3')
    #11. platform no
    #12. par aa rhi hai
    start=16500
    finish=20000
    audioProcessed=audio[start:finish]
    audioProcessed.export('12_hindi.mp3',format='mp3')
def textToSpeech(text,filename):
    mytext=str(text) # our text can be int so we convert to string
    language='hi' # hi for hindi
    myobj=gTTS(text=mytext,lang=language,slow=False)
    myobj.save(filename)

def mergeAudios(audios): # take list as input
    combined=AudioSegment.empty() # initially our combined mp3 is empty
    for i in audios:
        combined+=AudioSegment.from_mp3(i)
    return combined
def generateAnnoucement(filename):
    df=pand.read_excel(filename)
    print(df)
    for index,item in df.iterrows(): # iter df with respect to row
        #2.
        textToSpeech(item['from'],'2_hindi.mp3')
        #4.
        textToSpeech(item['via'],'4_hindi.mp3')
        #6.
        textToSpeech(item['to'],'6_hindi.mp3')
        #8.
        textToSpeech(item['train_no'],'8_hindi.mp3')
        #9.
        textToSpeech(item['train_name'],'9_hindi.mp3')
        #11.
        textToSpeech(item['platform'],'11_hindi.mp3')
        audios=[f"{i}_hindi.mp3" for i in range(1,13)]
        annoucement=mergeAudios(audios) #merge audios and reurn pydub object
        annoucement.export(f'annoucement_{index+1}.mp3',format='mp3') # index start from 0

print('Generating skeleton....')
generateSkeleton()
print('generating annoucement...')
generateAnnoucement('annoucement.xlsx')