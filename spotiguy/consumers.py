from channels.generic.websocket import AsyncWebsocketConsumer
import json
import base64


class AudioPlayerConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print('connected')
        await self.accept()

    async def disconnect(self, close_code):
        print('disconnected')

    async def receive(self, text_data):
        print(f'receiving: {text_data}')
        if text_data == 'start_audio_transfer':
            audio_file_path = r'D:\_\work\DjangoProject\spotiguy\media\audio\ringtone.mp3'  # Update with your audio file path
            await self.send_audio_file(audio_file_path)

    async def send_audio_file(self, file_path):
        chunk_size = 4096  # Adjust the chunk size as needed
        try:
            with open(file_path, 'rb') as audio_file:
                while chunk := audio_file.read(chunk_size):
                    print(f'sending: {chunk}')
                    await self.send(bytes_data=chunk)
            # Send end-of-audio marker
            await self.send(text_data='END_OF_AUDIO_MARKER')
            print('Send EOA')
        except FileNotFoundError:
            print('FNF')
            await self.send(text_data='Audio file not found')
        except BaseException as e:
            print('wtf!', e)