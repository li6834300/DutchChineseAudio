import os
from unicodedata import name
from urllib import response
from google.cloud import texttospeech_v1

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "static-groove-413415-af749aa41fa6.json"
client = texttospeech_v1.TextToSpeechClient()

UNIT = "3"

text = '''<speak>
Opstaan<break time="1000ms"/>Opstaan<break time="1000ms"/><voice name="cmn-CN-Wavenet-D">起床</voice><break time="1000ms"/>
Slapen<break time="1000ms"/>Slapen<break time="1000ms"/><voice name="cmn-CN-Wavenet-D">睡觉</voice><break time="1000ms"/>
Eten<break time="1000ms"/>Eten<break time="1000ms"/><voice name="cmn-CN-Wavenet-D">吃饭</voice><break time="1000ms"/>
Lezen<break time="1000ms"/>Lezen<break time="1000ms"/><voice name="cmn-CN-Wavenet-D">读书</voice><break time="1000ms"/>
Schrijven<break time="1000ms"/>Schrijven<break time="1000ms"/><voice name="cmn-CN-Wavenet-D">写字</voice><break time="1000ms"/>
Tekenen<break time="1000ms"/>Tekenen<break time="1000ms"/><voice name="cmn-CN-Wavenet-D">画画</voice><break time="1000ms"/>
Spelen<break time="1000ms"/>Spelen<break time="1000ms"/><voice name="cmn-CN-Wavenet-D">玩</voice><break time="1000ms"/>
Werken<break time="1000ms"/>Werken<break time="1000ms"/><voice name="cmn-CN-Wavenet-D">工作</voice><break time="1000ms"/>
Lachen<break time="1000ms"/>Lachen<break time="1000ms"/><voice name="cmn-CN-Wavenet-D">笑</voice><break time="1000ms"/>
Huil<break time="1000ms"/>Huil<break time="1000ms"/><voice name="cmn-CN-Wavenet-D">哭</voice><break time="1000ms"/>
Stoel<break time="1000ms"/>Stoel<break time="1000ms"/><voice name="cmn-CN-Wavenet-D">椅子</voice><break time="1000ms"/>
Tafel<break time="1000ms"/>Tafel<break time="1000ms"/><voice name="cmn-CN-Wavenet-D">桌子</voice><break time="1000ms"/>
Bed<break time="1000ms"/>Bed<break time="1000ms"/><voice name="cmn-CN-Wavenet-D">床</voice><break time="1000ms"/>
Boek<break time="1000ms"/>Boek<break time="1000ms"/><voice name="cmn-CN-Wavenet-D">书</voice><break time="1000ms"/>
Pen<break time="1000ms"/>Pen<break time="1000ms"/><voice name="cmn-CN-Wavenet-D">笔</voice><break time="1000ms"/>
Papier<break time="1000ms"/>Papier<break time="1000ms"/><voice name="cmn-CN-Wavenet-D">纸</voice><break time="1000ms"/>
Deur<break time="1000ms"/>Deur<break time="1000ms"/><voice name="cmn-CN-Wavenet-D">门</voice><break time="1000ms"/>
Raam<break time="1000ms"/>Raam<break time="1000ms"/><voice name="cmn-CN-Wavenet-D">窗户</voice><break time="1000ms"/>
Sleutel<break time="1000ms"/>Sleutel<break time="1000ms"/><voice name="cmn-CN-Wavenet-D">钥匙</voice><break time="1000ms"/>
Tas<break time="1000ms"/>Tas<break time="1000ms"/><voice name="cmn-CN-Wavenet-D">包</voice><break time="1000ms"/>
Ik ben blij<break time="1000ms"/>Ik ben blij<break time="1000ms"/><voice name="cmn-CN-Wavenet-D">我很高兴</voice><break time="1000ms"/>
Ik ben verdrietig<break time="1000ms"/>Ik ben verdrietig<break time="1000ms"/><voice name="cmn-CN-Wavenet-D">我很伤心</voice><break time="1000ms"/>
Ik ben moe<break time="1000ms"/>Ik ben moe<break time="1000ms"/><voice name="cmn-CN-Wavenet-D">我很累</voice><break time="1000ms"/>
Ik heb honger<break time="1000ms"/>Ik heb honger<break time="1000ms"/><voice name="cmn-CN-Wavenet-D">我饿了</voice><break time="1000ms"/>
Ik heb dorst<break time="1000ms"/>Ik heb dorst<break time="1000ms"/><voice name="cmn-CN-Wavenet-D">我渴了</voice><break time="1000ms"/>
Ik ga slapen<break time="1000ms"/>Ik ga slapen<break time="1000ms"/><voice name="cmn-CN-Wavenet-D">我要睡觉了</voice><break time="1000ms"/>
Tijd voor school<break time="1000ms"/>Tijd voor school<break time="1000ms"/><voice name="cmn-CN-Wavenet-D">上学时间</voice><break time="1000ms"/>
Wat doen we vandaag?<break time="1000ms"/>Wat doen we vandaag?<break time="1000ms"/><voice name="cmn-CN-Wavenet-D">我们今天做什么？</voice><break time="1000ms"/>
Kun je me helpen?<break time="1000ms"/>Kun je me helpen?<break time="1000ms"/><voice name="cmn-CN-Wavenet-D">你能帮我吗？</voice><break time="1000ms"/>
Het is speeltijd<break time="1000ms"/>Het is speeltijd<break time="1000ms"/><voice name="cmn-CN-Wavenet-D">是玩耍时间</voice><break time="1000ms"/>
</speak>'''

synthsis_input = texttospeech_v1.SynthesisInput(ssml=text)

voice1 = texttospeech_v1.VoiceSelectionParams (
    language_code = 'nl-NL',
    name = 'nl-NL-Wavenet-E',
)

audio_config = texttospeech_v1.AudioConfig(
    audio_encoding = texttospeech_v1.AudioEncoding.MP3
)

response1 = client.synthesize_speech(
    input=synthsis_input,
    voice=voice1,
    audio_config=audio_config
)


with open('audio_UNIT'+UNIT + '.mp3', 'wb', ) as output:
    output.write(response1.audio_content)
