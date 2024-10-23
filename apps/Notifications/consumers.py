# consumers.py

import json
from channels.generic.websocket import AsyncWebsocketConsumer


class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        if self.scope["user"].is_authenticated:
            self.user = self.scope["user"]
            self.group_name = f"user_{self.user.id}"

            # Add user to their group
            await self.channel_layer.group_add(self.group_name, self.channel_name)
            await self.accept()
        else:
            # Reject the connection if not authenticated
            await self.close()

    async def disconnect(self, close_code):
        # Remove user from group
        await self.channel_layer.group_discard(self.group_name, self.channel_name)

    async def send_notification(self, event):
        # Extract subject and message from the event
        subject = event.get("subject", "No Subject")
        message = event.get("message", "")
        id = event.get("id", "")

        # Send both subject and message as JSON
        await self.send(
            text_data=json.dumps({"subject": subject, "message": message, "id": id})
        )
