from flask import Blueprint, render_template, request, Flask
import os, requests, json
from os.path import join, dirname

# Env 
from dotenv import load_dotenv

# Whisper AI speech to text 
import whisper 

"""
Create an instance of Blueprint (class) named bp. 
"pages" is the name of blueprint. 
"""
bp = Blueprint("pages", __name__)



######################## RECORD OR UPLOAD ########################
@bp.route("/", methods = ["GET", "POST"])
def home():
    # dotenv_path = join(dirname(__file__), '.env')
    # load_dotenv(dotenv_path)
    # OPENROUTER_API_KEY = os.environ.get("OPENROUTER_API_KEY")

    # response = requests.post(
    #     url="https://openrouter.ai/api/v1/chat/completions",
    #     headers={
    #         "Authorization": f"Bearer {OPENROUTER_API_KEY}",
    #     },
    #     data=json.dumps({
    #         "model": "microsoft/phi-3-mini-128k-instruct:free", 
    #         "messages": [
    #         { "role": "user", "content": "What is the meaning of life?" }
    #         ]
    #     })
    # )

    # response_dict = json.loads(response.text)
    # choices_dict = response_dict.get("choices")[0]
    # message_dict = choices_dict.get("message")
    # role = message_dict.get("assistant")
    # content = message_dict.get("content")
    # return render_template("pages/home.html", role=role, content=content)
    return render_template("pages/home.html", warning="")

def is_allowed_file(file):
    return file.filename.endswith('.mp3')

def transcribe(audio):
    transcribe_model = whisper.load_model("base")
    transcribe_result = transcribe_model.transcribe(audio)
    transcription = transcribe_result["text"]
    return transcription

@bp.route("/upload", methods = ['POST'])
def upload(): 
    UPLOAD_FOLDER = '/user-uploads/'
    if request.method == 'POST':
        audio = request.files['audio-file']
        if audio and is_allowed_file(audio):
            filepath = "user-uploads/" + audio.filename
            audio.save(filepath)
            transcription = transcribe(filepath)
            return render_template("pages/transcribe.html", transcription=transcription)
        else:
            return render_template("pages/home.html", warning="Please select an .mp3 file.")



@bp.route("/past")
def past():
    return render_template("pages/past.html")