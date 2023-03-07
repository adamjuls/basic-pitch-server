from flask import Flask, request, send_file
import os
from basic_pitch.inference import predict_and_save
from basic_pitch import ICASSP_2022_MODEL_PATH

# instantiate flask
app = Flask(__name__)

@app.route("/predict", methods=["POST"])
def predict():
    """Endpoint to predict audio to midi
    :return (midi): This endpoint returns a midi file with the following format:
    """

    # get file from POST request and save it
    audio_file = request.files["file"]
    file_name = "audio.wav"
    audio_file.save(file_name)
    midi_file_name = file_name[:-4]
    audio_path_list = [file_name]

    # If midi_output/ + midi_file_name + _basic_pitch.mid exists, delete it
    if os.path.exists("midi_output/" + midi_file_name + "_basic_pitch.mid"):
        os.remove("midi_output/" + midi_file_name + "_basic_pitch.mid")

    predict_and_save(
        audio_path_list,
        "midi_output",
        True,
        False,
        False,
        False,
    )
	
    midi_file_name = file_name[:-4]
    os.remove(file_name)
    return send_file("midi_output/" + midi_file_name + "_basic_pitch.mid", as_attachment=True)
    
    

    


if __name__ == "__main__":
    app.run(debug=False)