from flask import Flask,request

app = Flask(__name__)
ugs = ["FloraAgent"]
def safe(user,script):
    if user in ugs:
        return script
    else:
        return "game.Players.LocalPlayer:Kick('Your Executor is not supported! Join Colonel Server and contact the Owner')"
@app.route('/loader/colonel')
def home():
    script = 'print("hello world")'
    ug = request.headers.get('User-Agent')
    return safe(ug, script)
@app.route('/')
def hme():
    return "Running!"
