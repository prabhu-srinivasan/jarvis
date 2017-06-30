import json
import os
import glob
import random

from watson_developer_cloud import (
    LanguageTranslatorV2,
    TextToSpeechV1,
    ToneAnalyzerV3,
    DiscoveryV1
)


#--  Watson service to translate from english to other languages

def translate(text, format):
    u = 'b017786f-ab3c-42bc-828f-aab0e2371a9e'
    p = 'RxVdxvrl42hP'
    if format ==  'text' and text:
        t = LanguageTranslatorV2(username=u, password=p)
        return t.translate(text=text, source='en', target='fr')
    if  format == 'audio' and text:
        path = text_speech(text)
        path = path.split('/static').pop()
        return '/static/jarvis{}?q={}'.format(path, random.random())


#--  Watson service to convert text to Speech

def text_speech(text):
    u = '44a4623d-a370-483a-81ea-9c19d4d75cc7'
    p = 'BbX6WUkbXbGT'
    text_to_speech = TextToSpeechV1(username=u, password=p, x_watson_learning_opt_out=True)  # Optional flag
    filepath =  os.path.join(os.path.dirname(__file__), 'static/audio/output.wav')
    with open(filepath,'wb') as audio_file:
          audio_file.write(text_to_speech.synthesize(text, accept='audio/wav', voice='fr-FR_ReneeVoice'))
    return filepath


#--  Watson Service to  do Tone Analyzer

def tone_analyzer(text):
    u = '71637edf-7d7a-4423-8ce9-d7b3e44e0e02'
    p = 'Fl21oTtxbbfG'
    tone_analyzer = ToneAnalyzerV3(username=u, password=p, version='2016-05-19')
    return tone_analyzer.tone(text)


#-- Watson service to perform query on top of documents

def upload_document_to_collection(file_path):
    collection_id = "0410f7f2-c65d-465f-935d-5b237a03b7dd"
    environment_id = "2534eff3-6e4e-4908-a6e4-dede8e0f92be"
    discovery = DiscoveryV1(
        username="865488e6-c594-46e8-a1e5-1e7b34528c76",
        password="WPMP8jMMBEBk",
        version="2016-05-05"
    )
    with open(file_path) as fileinfo:
        discovery.add_document(
            environment_id,
            collection_id,
            file_info=fileinfo
        )


def query_collection(query):
    collection_id = "3d1f4781-f502-441a-a17a-21e60c8aa2ff"
    environment_id = "b013b430-3922-41a4-8a9b-4610ac233a42"
    discovery = DiscoveryV1(
        username="c75b8256-1d19-4377-941d-bab1df00beb5",
        password="l7g2XTux1GkX",
        version="2016-05-05"
    )
    return discovery.query(environment_id, collection_id, query)
