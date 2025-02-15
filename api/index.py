from flask import Flask,jsonify
app = Flask(__name__)
ugs = ["FloraAgent"]
def safe(user,script):
    if user in ugs:
        return jsonify(script)
    else:
        return jsonify("game.Players.LocalPlayer:Kick('Your Executor is not supported! Join Colonel Server and contact the Owner')")
@app.route('/')
def hme():
    return jsonify("Running!")
@app.route('/loader/colonel')
def home():
    script = 'print("hello world")'
    ug = request.headers.get('User-Agent')
    return safe(ug,script)
