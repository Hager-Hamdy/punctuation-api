from deepmultilingualpunctuation import PunctuationModel
from flask import Flask, request, json, jsonify

app = Flask(__name__)
model_punctuation = PunctuationModel(model="oliverguhr/fullstop-punctuation-multilang-large")

#post request body-> {"text":"text you need to punctuate"}
@app.route('/api/punctuate-text', methods=['GET', 'POST'])
def punctuate():
    json_data = json.loads(request.data)
    return jsonify({"result": punctuate_text(json_data['text'])})

def punctuate_text(text):
  return model_punctuation.restore_punctuation(text)

if __name__ == "__main__":
  app.run(port=8005, host='0.0.0.0', debug=True)
