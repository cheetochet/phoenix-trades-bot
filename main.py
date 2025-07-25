from flask import Flask, jsonify
import os
import json 
import websocket

app = Flask(__name__)

def send_json_request(ws, req):
    ws.send(json.dumps(req))

def receive_json_response(ws):
    response = ws.recv()
    if response:
        return json.loads(response)

@app.route('/')
def index():
    ws = websocket.WebSocket()
    ws.connect("wss://gateway.discord.gg/?v=6&encording=json")
    heartbeat_interval = receive_json_response(ws)["d"]["heartbeat_interval"]

    token = "NzgxMzU3ODM5NjA4MTg0ODcy.Gcjxee.RThNACg3y3T-zVTyVtImZCjJePHO5imFwLGOJM"
    payload = {
        "op": 2,
        "d": {
            "token": token,
            "intents": 513,
            "properties": {
                "$os": "linux",
                "browser": "chrome", 
                "device": "pc"
            }
        }
    }
    send_json_request(ws, payload)

    count = 0
    while True:
        count = count + 1
        if count > 10:
            break
        event=receive_json_response(ws)
        try:
            return(jsonify(event))
        except:
            return jsonify({"failed failed": "chetan🚅"})
            break
        
    return jsonify({"Choo Choo": "Welcome to your Flask app chetan🚅"})


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
