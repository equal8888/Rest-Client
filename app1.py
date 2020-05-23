#!/usr/bin/env python
from flask import Flask, request, render_template
from flask_basicauth import BasicAuth
import json

app = Flask(__name__)
basic_auth = BasicAuth(app)

# Main page
@app.route('/')
def static1():
    return render_template('jsonpagestatic.html')

@app.route('/json01', methods=['GET','POST'])
@basic_auth.required
def json01():
    if request.method == 'GET' and "application/json" in request.headers["Content-Type"]:
       filehandlerR = open('data.txt', 'r+')

       if filehandlerR.mode == 'r+':
           contents = filehandlerR.readlines()
           convertstr01 = ''.join(contents)
           filehandlerR.close()

       return convertstr01


    if request.method == "POST" and "application/json" in request.headers["Content-Type"]:

# test str
#       req_data = '{"data01": "Hi there !"}'

# ----------------- not sure about this -----------------
       req_data = request.get_json()                    #
       jsonstr = json.dumps(req_data)                   #
# -------------------------------------------------------

       filehandlerW = open('data.txt', 'w+')

       if filehandlerW.mode == 'w+':
           filehandlerW.write(jsonstr)
       filehandlerW.close()

# ----------------- generate random  -----------------

       response = app.response_class(
       response='{"data01": "flask: ok"}',
       mimetype='application/json',
       )

       return response

if __name__ == '__main__':
    app.config['BASIC_AUTH_USERNAME'] = 'admin'
    app.config['BASIC_AUTH_PASSWORD'] = 'admin'
    app.run(debug=True, port=8888, host='0.0.0.0')
