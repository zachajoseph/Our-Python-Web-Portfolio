import projects  #projects definitions are placed in different file

#Use of flask Here
# https://flask.palletsprojects.com/en/1.1.x/api/
from flask import Flask, render_template
#create a Flask instance
app = Flask(__name__)


#Use of Routes here 
#connects default URL of server to render home.html
@app.route('/')
def home_route():
    return render_template("home.html", projects=projects.setup())


#connects /hello path of server to render apcsp.html
@app.route('/apcsp')
def apguidelines():
    return render_template("apcsp.html", projects=projects.setup())


#connects /dnhscsp path of server to render dnhscsp.html
@app.route('/delnorteapcompsci')
def dnhscsp():
    return render_template("dnhscsp.html", projects=projects.setup())

@app.route('/home')
def home():
    return render_template("home.html", projects=projects.setup())

@app.route('/pairshare')
def pairshare():
    return render_template("pairshare.html", projects=projects.setup())

if __name__ == "__main__":
    #runs the application on the repl development server
    app.run(port='3000', host='0.0.0.0')
