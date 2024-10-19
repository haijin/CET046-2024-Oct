from flask import Flask
from flask import render_template, request

app = Flask(__name__)

@app.route("/", methods =["GET", 'POST'])
def index():
    return(render_template("index.html"))

@app.route("/prediciton_DBS",methods =["GET", 'POST'])
def prediciton_DBS():
    return(render_template("prediciton_DBS.html"))
    #q = float(request.form.get("q"))
    #return(render_template("prediciton_DBS.html" ,r=(-50.6*q)+90.2))

if __name__ == "__main__":
    app.run()

