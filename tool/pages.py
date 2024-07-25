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

######################## TRANSCRIBE ########################
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
            # transcription = transcribe(filepath).strip()
            return render_template("pages/transcribe.html", transcription="Hello, I'm going to be showing you how you can control students' individual access to a particular quiz using the teacher portal. So from your teacher portal, go to your classroom, click on the quizzes tab, and you can select what quiz you want to manage access to. So for instance, this one, select the start time, and the end time, which is set at default to one hour. Click on save first, and then you can select the students whom you want to manage access to. So for instance, all three students, we can unlock the quiz for them. And now this quiz is accessible to these three unlock students during this time period. You can also select whether you want to show the grades and or the correct answers after the quiz is submitted. And there we have it.")
        else:
            return render_template("pages/home.html", warning="Please select an .mp3 file.")


######################## EDITING ########################
@bp.route("/edit", methods = ['GET', 'POST'])
def edit(): 
    if 'next' in request.form:
        transcript_res = request.form["transcriptionResults"]
        return render_template("pages/edit.html", transcript_res=transcript_res)
    else: 
        return ('', 204) # return the HTTP 'empty response' response, 204 No Content
    
@bp.route("/edit-results", methods = ['GET', 'POST'])
def editResults(): 
    if 'editSubmit' in request.form: 
        if request.form.get('para') and request.form.get('error'):
            return 'both'
        elif request.form.get('para'):
            return 'para'
        elif request.form.get('error'):
            return 'error'
        else:
            return 'nothing selected'
    else:
        return ('', 204)

@bp.route("/past")
def past():
    return render_template("pages/past.html")