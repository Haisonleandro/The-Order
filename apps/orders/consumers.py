import json
from channels.generic.websocket import WebsocketConsumer

class PedidoConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
    
    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        pedido_data = json.loads(text_data)
        self.send(text_data=json.dumps({
            'message': pedido_data['message']
        }))
