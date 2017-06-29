from watson_developer_cloud import ToneAnalyzerV3, LanguageTranslatorV2


# BEGIN of python-dotenv section
from os.path import join, dirname
from dotenv import load_dotenv
import os, sys
# END of python-dotenv section

if __name__ == '__main__':
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

def get_translate():
    return render_template('translate.html', tones=[])

def translate(text, format):
    u = os.environ.get("TRANS_USERNAME")
    p = os.environ.get("TRANS_PASSWORD")
    text = text
    if format ==  'text':
        src=  'en'
        tgt= 'es'
        t = LanguageTranslatorV2(username=u, password=p)
        transtext = t.translate(text=text, source=src, target=tgt)
        return transtext
    else :
        aud = text_speech(text)
        return aud


#--  Watson service to convert text to Speech

def text_speech(text):
    u = os.envion.get("TS_USERNAME")
    p = os.envion.get("TS_PASSWORD")
    transtext = text

    return aud


#--  Watson Service to  do Tone Analyzer

def Analtone(text):
    u=os.environ.get("TONE_USERNAME")
    p=os.environ.get("TONE_PASSWORD")

    tone_analyzer = ToneAnalyzerV3(username=u,password=p,version='2016-05-19')
    toneresp = tone_analyzer.tone(text)

    return toneresp
