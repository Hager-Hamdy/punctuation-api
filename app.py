#from deepmultilingualpunctuation import PunctuationModel
from flask import Flask, request, json, jsonify

from rpunct import RestorePuncts
# The default language is 'english'
rpunct = RestorePuncts()

@app.route('/test', methods=['GET'])
def test():
    result = rpunct.punctuate("""in 2018 cornell researchers built a high-powered detector that in combination with an algorithm-driven process called ptychography set a world record
    by tripling the resolution of a state-of-the-art electron microscope as successful as it was that approach had a weakness it only worked with ultrathin samples that were
    a few atoms thick anything thicker would cause the electrons to scatter in ways that could not be disentangled now a team again led by david muller the samuel b eckert
    professor of engineering has bested its own record by a factor of two with an electron microscope pixel array detector empad that incorporates even more sophisticated
    3d reconstruction algorithms the resolution is so fine-tuned the only blurring that remains is the thermal jiggling of the atoms themselves""")
    return result

app = Flask(__name__)
#model_punctuation = PunctuationModel(model="oliverguhr/fullstop-punctuation-multilang-large")

#post request body-> {"text":"text you need to punctuate"}
#@app.route('/api/punctuate-text', methods=['GET', 'POST'])
#def punctuate():
#    json_data = json.loads(request.data)
#    return jsonify({"result": punctuate_text(json_data['text'])})

#def punctuate_text(text):
#  return model_punctuation.restore_punctuation(text)

if __name__ == "__main__":
  app.run(port=8005, host='0.0.0.0', debug=True)
