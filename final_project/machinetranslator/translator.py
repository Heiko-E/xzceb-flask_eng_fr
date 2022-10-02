import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
VERSION='2022-10-02'

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='{VERSION}',
    authenticator=authenticator
)
language_translator.set_service_url(url)
language_translator.set_disable_ssl_verification(True)


def english_to_french(english_text):
    """
    Function to translate from english to french
    """
    translation = language_translator.translate(
        text=english_text,model_id='en-fr').get_result()
    french_text=json.dumps(translation, indent=2, ensure_ascii=False)
    return french_text

def french_to_english(french_text):
    """
    Function to translate from french to english
    """
    translation = language_translator.translate(
        text=french_text,model_id='fr-en').get_result()
    english_text=json.dumps(translation, indent=2, ensure_ascii=False)
    return english_text
