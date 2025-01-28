from flask import Flask, request, jsonify
from flask_cors import CORS
from transcription.py import transcribe_audio
from feedback.py import get_feedback
from pdf_generator.py import generate_pdf

app = Flask(__name__)
CORS(app)

@app.route("/transcribe", methods=["POST"])
def transcribe():
    # Get the uploaded audio file
    audio_file = request.files["audio"].filename
    transcript = transcribe_audio(audio_file)
    feedback = get_feedback(transcript)
    return jsonify({"transcript": transcript, "feedback": feedback})

@app.route("/generate-pdf", methods=["POST"])
def pdf_route():
    # Generate a PDF using provided feedback
    feedback = request.json["feedback"]
    file_name = generate_pdf(feedback)
    return jsonify({"pdf_file": file_name})

if __name__ == "__main__":
    app.run(debug=True)