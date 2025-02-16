from flask import Flask,request

app = Flask(__name__)
ugs = ["FloraAgent"]
def readfile(path):
    try:
        with open(path, "r") as f: 
            content = f.read()
            return content
    except FileNotFoundError:
        return None
def safe(user,script):
    if user in ugs:
        return script
    else:
        return "game.Players.LocalPlayer:Kick('Your Executor is not supported! Join Colonel Server and contact the Owner')"
@app.route('/loader/colonel')
def home():
    script = readfile("scripts/loader-colonel.txt")
    ug = request.headers.get('User-Agent')
    return safe(ug, script)
@app.route('/')
def hme():
    return "Running!"
