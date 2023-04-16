import requests
import os

# server url
URL = "http://18.221.59.4:5000/predict"


# audio file we'd like to send for predicting keyword
FILE_PATH = "piano.wav"


if __name__ == "__main__":
    print("HERE")
    # open files
    file = open(FILE_PATH, "rb")
    print("HERE 2")
    # package stuff to send and perform POST request
    values = {"file": (FILE_PATH, file, "audio/wav")}
    print("HERE 3")
    response = requests.post(URL, files=values)
    print("RESPONSE")
    output_path = os.path.join('response.mid')
    with open(output_path, 'wb') as f:
        f.write(response.content)
    print(f'MIDI file saved as {output_path}')
    print("POSTED")
    # print("Predicted MIDI: {}".format(data["keyword"]))
