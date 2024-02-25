import os
from unicodedata import name
from urllib import response
from google.cloud import texttospeech_v1

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "static-groove-413415-af749aa41fa6.json"
client = texttospeech_v1.TextToSpeechClient()

UNIT = "9"

text = '''<speak>
Cultuur<break time="1000ms"/>Cultuur<break time="1000ms"/><voice name="cmn-CN-Wavenet-D">文化</voice><break time="1000ms"/>
Feest<break time="1000ms"/>Feest<break time="1000ms"/><voice name="cmn-CN-Wavenet-D">节日</voice><break time="1000ms"/>
Muziekfestival<break time="1000ms"/>Muziekfestival<break time="1000ms"/><voice name="cmn-CN-Wavenet-D">音乐节</voice><break time="1000ms"/>
Kunst<break time="1000ms"/>Kunst<break time="1000ms"/><voice name="cmn-CN-Wavenet-D">艺术</voice><break time="1000ms"/>
Tentoonstelling<break time="1000ms"/>Tentoonstelling<break time="1000ms"/><voice name="cmn-CN-Wavenet-D">展览</voice><break time="1000ms"/>
Museum<break time="1000ms"/>Museum<break time="1000ms"/><voice name="cmn-CN-Wavenet-D">博物馆</voice><break time="1000ms"/>
Theater<break time="1000ms"/>Theater<break time="1000ms"/><voice name="cmn-CN-Wavenet-D">剧院</voice><break time="1000ms"/>
Film<break time="1000ms"/>Film<break time="1000ms"/><voice name="cmn-CN-Wavenet-D">电影</voice><break time="1000ms"/>
Reizen<break time="1000ms"/>Reizen<break time="1000ms"/><voice name="cmn-CN-Wavenet-D">旅行</voice><break time="1000ms"/>
Paspoort<break time="1000ms"/>Paspoort<break time="1000ms"/><voice name="cmn-CN-Wavenet-D">护照</voice><break time="1000ms"/>
Visum<break time="1000ms"/>Visum<break time="1000ms"/><voice name="cmn-CN-Wavenet-D">签证</voice><break time="1000ms"/>
Vliegticket<break time="1000ms"/>Vliegticket<break time="1000ms"/><voice name="cmn-CN-Wavenet-D">飞机票</voice><break time="1000ms"/>
Toerist<break time="1000ms"/>Toerist<break time="1000ms"/><voice name="cmn-CN-Wavenet-D">游客</voice><break time="1000ms"/>
Gids<break time="1000ms"/>Gids<break time="1000ms"/><voice name="cmn-CN-Wavenet-D">导游</voice><break time="1000ms"/>
Vakantie<break time="1000ms"/>Vakantie<break time="1000ms"/><voice name="cmn-CN-Wavenet-D">假期</voice><break time="1000ms"/>
Taal<break time="1000ms"/>Taal<break time="1000ms"/><voice name="cmn-CN-Wavenet-D">语言</voice><break time="1000ms"/>
Woordenboek<break time="1000ms"/>Woordenboek<break time="1000ms"/><voice name="cmn-CN-Wavenet-D">词典</voice><break time="1000ms"/>
Vertaler<break time="1000ms"/>Vertaler<break time="1000ms"/><voice name="cmn-CN-Wavenet-D">翻译</voice><break time="1000ms"/>
Cursus<break time="1000ms"/>Cursus<break time="1000ms"/><voice name="cmn-CN-Wavenet-D">课程</voice><break time="1000ms"/>
Leren<break time="1000ms"/>Leren<break time="1000ms"/><voice name="cmn-CN-Wavenet-D">学习</voice><break time="1000ms"/>
Wil je een museum bezoeken?<break time="1000ms"/>Wil je een museum bezoeken?<break time="1000ms"/><voice name="cmn-CN-Wavenet-D">你想去参观博物馆吗？</voice><break time="1000ms"/>
Laten we naar een filmfestival gaan<break time="1000ms"/>Laten we naar een filmfestival gaan<break time="1000ms"/><voice name="cmn-CN-Wavenet-D">让我们去参加电影节</voice><break time="1000ms"/>
Ik wil mijn taalvaardigheid verbeteren<break time="1000ms"/>Ik wil mijn taalvaardigheid verbeteren<break time="1000ms"/><voice name="cmn-CN-Wavenet-D">我想提高我的语言能力</voice><break time="1000ms"/>
Heb je een aanbeveling voor een goed boek?<break time="1000ms"/>Heb je een aanbeveling voor een goed boek?<break time="1000ms"/><voice name="cmn-CN-Wavenet-D">你有好书推荐吗？</voice><break time="1000ms"/>
Ik plan een reis naar het buitenland<break time="1000ms"/>Ik plan een reis naar het buitenland<break time="1000ms"/><voice name="cmn-CN-Wavenet-D">我计划去国外旅行</voice><break time="1000ms"/>
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
