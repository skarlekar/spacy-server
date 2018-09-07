from flask import Flask
from flask_restful import Api, Resource, reqparse
import json
import spacy

app = Flask(__name__)
api = Api(app)

nlp = nlp = spacy.load('en_core_web_sm')

class Sentencer(Resource):
    def post(self):
        parser = reqparse.RequestParser()
	parser.add_argument("input")
	args = parser.parse_args()
	text = args["input"]
	print("Input: {}".format(text))
        doc = nlp(text)
        sentences = list(doc.sents)
	body = {"input": text}
    	body["sentences"] = []
    	for sent in sentences:
            print(sent.text)
            body["sentences"].append(sent.text)
	return body, 200	

api.add_resource(Sentencer, "/parse")
app.run(host='0.0.0.0',port=8080,debug=True)

