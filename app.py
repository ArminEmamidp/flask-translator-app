from flask import Flask, render_template, request
from googletrans import Translator


app = Flask(__name__)
translator = Translator()


@app.route('/', methods=['POST', 'GET'])
def translator_page():
    if request.method == 'POST':
        try:
            text_to_translate = request.form['text_to_translate'].lower()
            selected_language = request.form['select_language']
            translated_text = translator.translate(text=text_to_translate, dest=selected_language)
            text = translated_text.text
        except:
            text = ''
        return render_template('main.html', translation_result=text)
    else:
        return render_template('main.html')



if __name__ == '__main__':
    app.run(debug=True, port=8000)