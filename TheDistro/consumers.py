from django.contrib.auth import get_user_model

from channels.generic.websocket import AsyncWebsocketConsumer

from . import utils

import json

#from . import utils

class TheDistroConsumer(AsyncWebsocketConsumer):
    
    """
    Called before websocket handshakes
    """
    
    async def connect(self, **kwargs):
        
        # add user to the room
        #This ensures that the user receives messages while he is connected
        #or after reconnectiong due to network loss
        await self.channel_layer.group_add(
            'Data',
            self.channel_name
        )

        # Accept the connection
        await self.accept()

    # Store which rooms the user has joined on this connection

    async def disconnect(self, close_code):
        
        # Leave room group
        await self.channel_layer.group_discard(
            'Data',
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        
        data = json.loads(text_data)
        
        print(data['query'])
                
        # Send message to room
        await self.channel_layer.group_send(

            'Data',

            {
                'type': 'data_retrieve',
                'data': utils.get_data(data['query'])
            }
        )

    
    # Handles Chat messages
    async def data_retrieve(self, event):
        # Send message to WebSocket
        await self.send(text_data=json.dumps(event))

    # Handle Specific messages event E.g , Message sent/ Read
    async def message_event(self, event):
        # Send message to WebSocket
        await self.send(text_data=json.dumps(event))

    async def fetch_message_event(self, event):
        # Send message to WebSocket
        await self.send(text_data=json.dumps(event))

    # Handles user is typing
    async def is_typing(self, event):
        # Send message to WebSocket
        await self.send(text_data=json.dumps(event))

    # Handles status change
    async def status_event(self, event):
        # Send message to WebSocket
        await self.send(text_data=json.dumps(event))

    # Handles attachment
    async def attachment_event(self, event):
        # Send message to WebSocket
        await self.send(text_data=json.dumps(event))

