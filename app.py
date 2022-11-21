from flask import Flask, render_template, request, make_response
from db import insert_db, read_db
import sqlite3
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
@app.route('/post', methods=['POST'])
def post():
    text = request.json['content']
    translation = translate_text('zh', text)['translatedText']
    insert_db(translation)
    print(translation)
    return

@app.route('/')
def record():
    text = 'Speak now'
    title = 'default'

    html = render_template('record.html', text=text, title=title)
    response = make_response(html)
    return response


@app.route('/display.html')
def display():
  return render_template('display.html', text=read_db()[0]['content'])

if __name__ == '__main__':
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=True)