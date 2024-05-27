from channels.generic.websocket import AsyncWebsocketConsumer
import json
import base64


class AudioPlayerConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Accept the WebSocket connection
        print('WebSocket connection established.')
        await self.accept()

    async def disconnect(self, close_code):
        # Clean up any resources if needed
        print('WebSocket connection closed.')
        pass

    async def receive(self, text_data):
        try:
            data = json.loads(text_data)
            if data.get('command') == 'start_audio_transfer':
                audio_file_path = r'D:\_\work\DjangoProject\spotiguy\media\audio\ringtone.mp3'  # Update with your audio file path
                await self.send_audio_file(audio_file_path)
        except json.JSONDecodeError as e:
            print(e.msg)
            await self.send(text_data=json.dumps({'error': 'Invalid JSON'}))

    async def send_audio_file(self, file_path):
        chunk_size = 4096  # Adjust the chunk size as needed
        try:
            with open(file_path, 'rb') as audio_file:
                while chunk := audio_file.read(chunk_size):
                    encoded_chunk = base64.b64encode(chunk).decode('utf-8')
                    await self.send(
                        text_data=json.dumps({'chunk': encoded_chunk}))
            # Send end-of-audio marker
            await self.send(
                text_data=json.dumps({'end': 'END_OF_AUDIO_MARKER'}))
        except FileNotFoundError:
            await self.send(
                text_data=json.dumps({'error': 'Audio file not found'}))

    # async def receive(self, text_data=None, bytes_data=None):
    #     # Parse incoming JSON message
    #     data = json.loads(text_data)
    #     # Handle different types of messages
    #     message_type = data.get('type')
    #     if message_type == 'play':
    #         await self.send_audio_file(r'D:\_\work\DjangoProject\spotiguy\media\audio\ringtone.mp3')
    #         print("Let's play")
    #         # Logic for starting playback
    #         await self.channel_layer.group_send(
    #             'audio_player_group',
    #             {'type': 'playback.started'}
    #         )
    #     elif message_type == 'pause':
    #         # Logic for pausing playback
    #         pass
    #     # Add more cases for other message types
    #     elif message_type == 'start_audio_transfer':
    #         audio_file_path = r'D:\_\work\DjangoProject\spotiguy\media\audio\Queen – ringtone.mp3'  # Path to your audio file
    #         await self.send_audio_file(audio_file_path)
    #
    # async def send_audio_file(self, file_path):
    #     chunk_size = 1024  # Adjust the chunk size as needed
    #     with open(file_path, 'rb') as audio_file:
    #         while True:
    #             chunk = audio_file.read(chunk_size)
    #             if not chunk:
    #                 break
    #             encoded_chunk = base64.b64encode(chunk).decode('utf-8')
    #             await self.send(text_data=encoded_chunk)
    #     await self.send(text_data='END_OF_AUDIO_MARKER')
