from flask import Flask, render_template, jsonify, request, make_response, redirect, url_for
from db import insert_db, read_db, init_db, get_lang_db, change_lang_db
import os
import six
from google.cloud import translate_v2 as translate

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r"serviceAccountToken.json" # /etc/secrets/serviceAccountToken.json

app = Flask(__name__)

translate_client = translate.Client()


# translate text into target language using google translate api
def translate_text(target, text):
    # target must be an ISO 639-1 language code
    # https://g.co/cloud/translate/v2/translate-reference#supported_languages
    if isinstance(text, six.binary_type):
        text = text.decode("utf-8")

    result = translate_client.translate(text, target_language=target)
    return result
    # print(u"Text: {}".format(result["input"]))
    # print(u"Translation: {}".format(result["translatedText"]))
    # print(u"Detected source language: {}".format(result["detectedSourceLanguage"]))


def list_languages():
    return translate_client.get_languages()

@app.route('/translate_and_store', methods=['POST'])
def translate_and_store():
    text = request.json['content']
    translation = translate_text(get_language(), text)['translatedText']
    insert_db(translation)
    return {}

@app.route('/get_text', methods=['GET'])
def get_text():
    texts = read_db()
    text = texts[0]['content'] if len(texts) > 0 else 'Listening...'
    message = {'displayText': text}
    return jsonify(message)

def get_language():
    lang = get_lang_db()
    language = lang[0]['language'] if len(lang) > 0 else 'en'
    return language

@app.route('/change_language', methods=['POST'])
def change_language():
    language = request.json['language']
    change_lang_db(language)
    return {}

# speaker display
@app.route('/')
@app.route('/speak')
def record():
    html = render_template('record.html')
    response = make_response(html)
    return response

# google glass transcription display
@app.route('/view')
def display():
    html = render_template('display.html')
    response = make_response(html)
    return response

# google glass change display language
@app.route('/change_view_language')
def language():
    html = render_template('language.html')
    response = make_response(html)
    return response


if __name__ == '__main__':
    init_db()
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=True)