import asyncio;
import websockets;
from calculator import main

# 클라이언트 접속이 되면 호출된다.
async def accept(websocket, path):
  while True:
    # 클라이언트로부터 메시지를 대기한다.
    data = await websocket.recv()
    print("receive : " + data)

    # 함수 위치

    data = main(data)


    print(data)



    # await websocket.send("echo : " + data)
    await websocket.send(data)
 
# 웹 소켓 서버 생성.호스트는 localhost에 port는 9998로 생성한다. 
start_server = websockets.serve(accept, "localhost", 9998)
#비동기
asyncio.get_event_loop().run_until_complete(start_server);
asyncio.get_event_loop().run_forever();

