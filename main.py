#https://docs.replit.com/hosting/deploying-http-servers
from flask import Flask, render_template, request
import parser
import json

app = Flask(__name__)

@app.route('/')
def index():
  #https://stackoverflow.com/questions/24892035/how-can-i-get-the-named-parameters-from-a-url-using-flask
  text = request.args.get('text')
  inst = parser.TextProcess()
  return json.dumps(dict(inst.findZipf(text)))


app.run(host='0.0.0.0', port=8080)