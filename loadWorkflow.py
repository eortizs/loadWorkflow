import json
import websocket
import requests

def on_message(ws, message):
    print(message)

def on_error(ws, error):
    print(error)

def on_close(ws):
    print("Conexión cerrada")

def on_open(ws):
    url = "https://peopleconnect.com.mx/gecko/files/tools/workflow.json" 
    response = requests.get(url)
    if response.status_code == 200:
        workflow_data = response.json()
        ws.send(json.dumps({"type": "start", "data": workflow_data}))
    else:
        print(f"Error al descargar el archivo JSON: {response.status_code}")

if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("ws://127.0.0.1:8188/ws",
                              on_message=on_message,
                              on_error=on_error,
                              on_close=on_close)
    ws.on_open = on_open
    ws.run_forever()
