import os
from unicodedata import name
from urllib import response
from google.cloud import texttospeech_v1

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "static-groove-413415-af749aa41fa6.json"
client = texttospeech_v1.TextToSpeechLongAudioSynthesizeClient()
project_id = 'static-groove-413415'
location = 'eu'
UNIT = "1"
output_gcs_uri = 'gs://my_t2v/my_t2v'

text = '''<speak>
Broer<break time="1000ms"/>Broer<break time="1000ms"/><voice name="cmn-CN-Wavenet-D">兄弟</voice><break time="1000ms"/>
Zus<break time="1000ms"/>Zus<break time="1000ms"/><voice name="cmn-CN-Wavenet-D">姐妹</voice><break time="1000ms"/>
Vriend<break time="1000ms"/>Vriend<break time="1000ms"/><voice name="cmn-CN-Wavenet-D">朋友</voice><break time="1000ms"/>
School<break time="1000ms"/>School<break time="1000ms"/><voice name="cmn-CN-Wavenet-D">学校</voice><break time="1000ms"/>
Boek<break time="1000ms"/>Boek<break time="1000ms"/><voice name="cmn-CN-Wavenet-D">书</voice><break time="1000ms"/>
Bal<break time="1000ms"/>Bal<break time="1000ms"/><voice name="cmn-CN-Wavenet-D">球</voice><break time="1000ms"/>
Kat<break time="1000ms"/>Kat<break time="1000ms"/><voice name="cmn-CN-Wavenet-D">猫</voice><break time="1000ms"/>
Hond<break time="1000ms"/>Hond<break time="1000ms"/><voice name="cmn-CN-Wavenet-D">狗</voice><break time="1000ms"/>
Huis<break time="1000ms"/>Huis<break time="1000ms"/><voice name="cmn-CN-Wavenet-D">家</voice><break time="1000ms"/>
Zon<break time="1000ms"/>Zon<break time="1000ms"/><voice name="cmn-CN-Wavenet-D">太阳</voice><break time="1000ms"/>
Maan<break time="1000ms"/>Maan<break time="1000ms"/><voice name="cmn-CN-Wavenet-D">月亮</voice><break time="1000ms"/>
Ster<break time="1000ms"/>Ster<break time="1000ms"/><voice name="cmn-CN-Wavenet-D">星星</voice><break time="1000ms"/>
Boom<break time="1000ms"/>Boom<break time="1000ms"/><voice name="cmn-CN-Wavenet-D">树</voice><break time="1000ms"/>
Bloem<break time="1000ms"/>Bloem<break time="1000ms"/><voice name="cmn-CN-Wavenet-D">花</voice><break time="1000ms"/>
Water<break time="1000ms"/>Water<break time="1000ms"/><voice name="cmn-CN-Wavenet-D">水</voice><break time="1000ms"/>
Eten<break time="1000ms"/>Eten<break time="1000ms"/><voice name="cmn-CN-Wavenet-D">吃</voice><break time="1000ms"/>
Drinken<break time="1000ms"/>Drinken<break time="1000ms"/><voice name="cmn-CN-Wavenet-D">喝</voice><break time="1000ms"/>
Spelen<break time="1000ms"/>Spelen<break time="1000ms"/><voice name="cmn-CN-Wavenet-D">玩</voice><break time="1000ms"/>
Lopen<break time="1000ms"/>Lopen<break time="1000ms"/><voice name="cmn-CN-Wavenet-D">走</voice><break time="1000ms"/>
Springen<break time="1000ms"/>Springen<break time="1000ms"/><voice name="cmn-CN-Wavenet-D">跳</voice><break time="1000ms"/>
Groot<break time="1000ms"/>Groot<break time="1000ms"/><voice name="cmn-CN-Wavenet-D">大</voice><break time="1000ms"/>
Klein<break time="1000ms"/>Klein<break time="1000ms"/><voice name="cmn-CN-Wavenet-D">小</voice><break time="1000ms"/>
Langzaam<break time="1000ms"/>Langzaam<break time="1000ms"/><voice name="cmn-CN-Wavenet-D">慢</voice><break time="1000ms"/>
Snel<break time="1000ms"/>Snel<break time="1000ms"/><voice name="cmn-CN-Wavenet-D">快</voice><break time="1000ms"/>
Warm<break time="1000ms"/>Warm<break time="1000ms"/><voice name="cmn-CN-Wavenet-D">暖</voice><break time="1000ms"/>
Koud<break time="1000ms"/>Koud<break time="1000ms"/><voice name="cmn-CN-Wavenet-D">冷</voice><break time="1000ms"/>
Mooi<break time="1000ms"/>Mooi<break time="1000ms"/><voice name="cmn-CN-Wavenet-D">美丽</voice><break time="1000ms"/>
Leuk<break time="1000ms"/>Leuk<break time="1000ms"/><voice name="cmn-CN-Wavenet-D">有趣</voice><break time="1000ms"/>
Vandaag<break time="1000ms"/>Vandaag<break time="1000ms"/><voice name="cmn-CN-Wavenet-D">今天</voice><break time="1000ms"/>
Morgen<break time="1000ms"/>Morgen<break time="1000ms"/><voice name="cmn-CN-Wavenet-D">明天</voice><break time="1000ms"/>
Appel<break time="1000ms"/>Appel<break time="1000ms"/><voice name="cmn-CN-Wavenet-D">苹果</voice><break time="1000ms"/>
Banaan<break time="1000ms"/>Banaan<break time="1000ms"/><voice name="cmn-CN-Wavenet-D">香蕉</voice><break time="1000ms"/>
Auto<break time="1000ms"/>Auto<break time="1000ms"/><voice name="cmn-CN-Wavenet-D">汽车</voice><break time="1000ms"/>
Fiets<break time="1000ms"/>Fiets<break time="1000ms"/><voice name="cmn-CN-Wavenet-D">自行车</voice><break time="1000ms"/>
Stoel<break time="1000ms"/>Stoel<break time="1000ms"/><voice name="cmn-CN-Wavenet-D">椅子</voice><break time="1000ms"/>
Tafel<break time="1000ms"/>Tafel<break time="1000ms"/><voice name="cmn-CN-Wavenet-D">桌子</voice><break time="1000ms"/>
Bed<break time="1000ms"/>Bed<break time="1000ms"/><voice name="cmn-CN-Wavenet-D">床</voice><break time="1000ms"/>
Klok<break time="1000ms"/>Klok<break time="1000ms"/><voice name="cmn-CN-Wavenet-D">钟</voice><break time="1000ms"/>
Jas<break time="1000ms"/>Jas<break time="1000ms"/><voice name="cmn-CN-Wavenet-D">外套</voice><break time="1000ms"/>
Schoenen<break time="1000ms"/>Schoenen<break time="1000ms"/><voice name="cmn-CN-Wavenet-D">鞋子</voice><break time="1000ms"/>
Ik heb honger<break time="1000ms"/>Ik heb honger<break time="1000ms"/><voice name="cmn-CN-Wavenet-D">我饿了</voice><break time="1000ms"/>
Ik heb dorst<break time="1000ms"/>Ik heb dorst<break time="1000ms"/><voice name="cmn-CN-Wavenet-D">我渴了</voice><break time="1000ms"/>
Ik ben moe<break time="1000ms"/>Ik ben moe<break time="1000ms"/><voice name="cmn-CN-Wavenet-D">我累了</voice><break time="1000ms"/>
Mag ik dit hebben?<break time="1000ms"/>Mag ik dit hebben?<break time="1000ms"/><voice name="cmn-CN-Wavenet-D">我可以拿这个吗？</voice><break time="1000ms"/>
Ik hou van jou<break time="1000ms"/>Ik hou van jou<break time="1000ms"/><voice name="cmn-CN-Wavenet-D">我爱你</voice><break time="1000ms"/>
Waar is de wc?<break time="1000ms"/>Waar is de wc?<break time="1000ms"/><voice name="cmn-CN-Wavenet-D">厕所在哪里？</voice><break time="1000ms"/>
Ik wil spelen<break time="1000ms"/>Ik wil spelen<break time="1000ms"/><voice name="cmn-CN-Wavenet-D">我想玩</voice><break time="1000ms"/>
Hoe laat is het?<break time="1000ms"/>Hoe laat is het?<break time="1000ms"/><voice name="cmn-CN-Wavenet-D">现在几点了？</voice><break time="1000ms"/>
Kan ik helpen?<break time="1000ms"/>Kan ik helpen?<break time="1000ms"/><voice name="cmn-CN-Wavenet-D">我可以帮忙吗？</voice><break time="1000ms"/>
Wat is jouw naam?<break time="1000ms"/>Wat is jouw naam?<break time="1000ms"/><voice name="cmn-CN-Wavenet-D">你叫什么名字？</voice><break time="1000ms"/>

</speak>'''

synthsis_input = texttospeech_v1.SynthesisInput(ssml=text)

voice1 = texttospeech_v1.VoiceSelectionParams (
    language_code = 'nl-NL',
    name = 'nl-NL-Wavenet-E',
)

audio_config = texttospeech_v1.AudioConfig(
    audio_encoding = texttospeech_v1.AudioEncoding.LINEAR16
)
parent = f"projects/{project_id}/locations/{location}"

request = texttospeech_v1.SynthesizeLongAudioRequest(
    parent = parent,
    input=synthsis_input,
    audio_config=audio_config,
    voice=voice1,
    output_gcs_uri=output_gcs_uri,
)

response1 = client.synthesize_long_audio(
    request=request
)


with open('audio_UNIT'+UNIT + '.mp3', 'wb', ) as output:
    output.write(response1.audio_content)
