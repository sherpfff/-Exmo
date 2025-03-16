import asyncio
import websockets
import json

class DataCollector:
    def __init__(self, ws_url: str, pair: str):
        self.ws_url = ws_url
        self.pair = pair
        self.data = []

    async def connect(self):
        async with websockets.connect(self.ws_url) as websocket:
            subscribe_message = {
                "method": "subscribe",
                "params": {"channel": f"ticker.{self.pair}"},
                "id": 1
            }
            await websocket.send(json.dumps(subscribe_message))
            while True:
                response = await websocket.recv()
                data = json.loads(response)
                if 'result' in data and 'last' in data['result']:
                    self.data.append(data['result'])
                    print(f"Получены данные: {data['result']}")

    def get_latest_data(self):
        return self.data[-1] if self.data else None