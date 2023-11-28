import os
import random
from flask import Flask, render_template, request, redirect, url_for, send_file

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    message = ''

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username == "Patrick" and password == "Buyain":
            return redirect(url_for('home'))
        elif username == "Elisha" and password == "Abed":
            return redirect(url_for('home'))
        else:
            message = "No user found."

    return render_template('index.html', message = message, play_audio=True)

@app.route('/audio')
def get_random_audio():
    audio_folder = 'audio_database'
    audio_files = os.listdir(audio_folder)
    randomly_selected_audio = random.choice(audio_files)
    return send_file(os.path.join(audio_folder, randomly_selected_audio), as_attachment=True)

@app.route('/home')
def home():
    return render_template('home.html')

if __name__ == "__main__":
    app.run(debug=True)

#after audio initially played, will have another 3 second timer then play the audio again. Afterwards play another 3 second beep
#then redirect to captcha answer form.