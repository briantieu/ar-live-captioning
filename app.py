from flask import Flask, render_template, request, make_response, redirect, url_for
from db import insert_db, read_db, init_db
import os
import sqlite3

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r"/etc/secrets/serviceAccountToken.json"
# print(os.getenv('GOOGLE_APPLICATION_CREDENTIALS'))

app = Flask(__name__)

def translate_text(target, text):
    """Translates text into the target language.

    Target must be an ISO 639-1 language code.
    See https://g.co/cloud/translate/v2/translate-reference#supported_languages
    """
    import six
    from google.cloud import translate_v2 as translate

    translate_client = translate.Client()

    if isinstance(text, six.binary_type):
        text = text.decode("utf-8")

    # Text can also be a sequence of strings, in which case this method
    # will return a sequence of results for each text.
    result = translate_client.translate(text, target_language=target)
    return result
    # print(u"Text: {}".format(result["input"]))
    # print(u"Translation: {}".format(result["translatedText"]))
    # print(u"Detected source language: {}".format(result["detectedSourceLanguage"]))

# two decorators, same function
@app.route('/insertdb', methods=['POST'])
def insertdb():
    text = request.json['content']
    translation = translate_text('es', text)['translatedText']
    insert_db(translation)
    # print(translation)
    # insert_db(text)
    return {}

@app.route('/')
def record():
    text = 'Speak now'
    title = 'default'

    html = render_template('record.html', text=text, title=title)
    response = make_response(html)
    return response


@app.route('/display.html')
def display():
    texts = read_db()
    text = texts[0]['content'] if len(texts) > 0 else 'Listening....'

    return render_template('display.html', text=text)

if __name__ == '__main__':
    init_db()
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.config['GOOGLE_APPLICATION_CREDENTIALS'] = 'C:\\Users\\brian\\OneDrive\\Desktop\\ar-live-captioning\\glass-live-captioning-68055e88006f.json'
    app.run(debug=True)