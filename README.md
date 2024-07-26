# Smart Audio Transcription and Editing Tool
## Introduction
This project combines audio transcription and smart editing into a convenient end-to-end user tool. The smart editing feature parses the transcription, adds appropriate paragraph breaks and corrects grammatical / sentence errors. Users are able to manually edit the text to their liking at any stage of processing. 
It uses the following models: 
* Transcription: OpenAI's Whisper model
* Post-transcription smart editing: Microsoft's Phi-3 Mini 128K Instruct OpenRouter.AI API 

## Installation
1. Clone the repository.
2. Install python3 and pip.
3. Inside the project root folder, run `python -m venv venv` to create a virtual environment.
4. Activate the virtual environment: run `source ./venv/bin/activate`.
5. Inside the project root folder, run `pip install -r requirements.txt` to install the necessary packages.
6. To download the Whisper model, run `pip install --upgrade --no-deps --force-reinstall git+https://github.com/openai/whisper.git`. Follow the instructions on https://github.com/openai/whisper for more information.

## Running the web app 
1. Run `python -m flask --app tool run --port 8000`
2. Open the web app on `localhost:8000` in your Chrome browser. 
