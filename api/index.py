from flask import Flask,jsonify
app = Flask(__name__)
ugs = [
    "FloraAgent"
]
@app.route('/')
def hme():
    return jsonify({"Running!"})
@app.route('/loader/colonel')
def home():
    script = r'print("hello world")'
    found = False
    ug = request.headers.get('user-agent')
    for i,v in range(ugs):
        if v == ug:
            found = True
            break 
    if found == True:
        return jsonify(script)
    else:
        return jsonify("game.Players.LocalPlayer:Kick('Your Executor is not supported! Join Colonel Server and contact the Owner')")
