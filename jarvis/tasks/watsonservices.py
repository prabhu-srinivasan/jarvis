from watson_developer_cloud import ToneAnalyzerV3, LanguageTranslatorV2,TextToSpeechV1


# BEGIN of python-dotenv section
from dotenv import load_dotenv
import os
import sys
import json
# END of python-dotenv section


# BEGIN of python-dotenv section
dotenv_path = join(dirname(__file__), '.env')
if (not os.path.isfile(dotenv_path)):
    sys.stderr.write("ERROR: you are trying to run this script locally,"\
                     " you need to set your credentials in file {}\n".format(dotenv_path))
    sys.exit(1)
else:
    load_dotenv(dotenv_path)
# END of python-dotenv section


#--  Watson service to translate from english to other languages

def translate(text, format):
    u = os.environ.get("TRANS_USERNAME")
    p = os.environ.get("TRANS_PASSWORD")
    text = text
    if format ==  'text':
        t = LanguageTranslatorV2(username=u, password=p)
        return json.dumps(t.translate(text=text, source='en', target='es'))
    if  format ==  'audio':
        return  text_speech(text)


#--  Watson service to convert text to Speech

def text_speech(text):
    u = os.envion.get("TS_USERNAME")
    p = os.envion.get("TS_PASSWORD")
    text_to_speech = TextToSpeechV1(username=u,password=p,x_watson_learning_opt_out=True)  # Optional flag
    filepath =  os.join(os.dirname(os.dirname(__file__)), 'static/audio/output.wav')
    with open(filepath,'wb') as audio_file:
          audio_file.write(text_to_speech.synthesize(text, accept='audio/wav',voice="en-US_AllisonVoice"))
    return filepath


#--  Watson Service to  do Tone Analyzer

def tone_analyzer(text):
    u=os.environ.get("TONE_USERNAME")
    p=os.environ.get("TONE_PASSWORD")
    tone_analyzer = ToneAnalyzerV3(username=u,password=p,version='2016-05-19')
    return json.dumps(tone_analyzer.tone(text))
