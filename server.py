import asyncio
from websockets.asyncio.server import serve

HOST =  "0.0.0.0"
PORT = 8765

async def handle_client(websocket):
    async for message in websocket:
        await websocket.send(message)

async def main():
    server = await serve(handle_client, HOST, PORT)
    print(f"server started at {HOST}:{PORT}")
    await  server.serve_forever()

if __name__ ==  "__main__":
    asyncio.run(main())
