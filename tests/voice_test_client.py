import asyncio
import websockets


async def test():

    uri = "ws://localhost:8000/voice"

    async with websockets.connect(uri) as ws:

        with open("sample_fixed.wav", "rb") as f:

            while chunk := f.read(4096):

                await ws.send(chunk)

        response = await ws.recv()

        print("Agent response:", response)


asyncio.run(test())