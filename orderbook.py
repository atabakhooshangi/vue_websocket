sells = [
    {'order_id': 12, 'user_id': 12, 'price': '3750', 'size': '2.00', 'funds': '0.00', 'side': 'sell', 'type': 'limit',
     'time_in_force': 'GTC'},
    {'order_id': 13, 'user_id': 13, 'price': '3724', 'size': '1.00', 'funds': '0.00', 'side': 'sell', 'type': 'limit',
     'time_in_force': 'GTC'},
    {'order_id': 18, 'user_id': 18, 'price': '3710', 'size': '2.00', 'funds': '0.00', 'side': 'sell', 'type': 'limit',
     'time_in_force': 'GTC'},
    {'order_id': 19, 'user_id': 19, 'price': '3708', 'size': '2.00', 'funds': '0.00', 'side': 'sell', 'type': 'limit',
     'time_in_force': 'GTC'},
    {'order_id': 11, 'user_id': 11, 'price': '3708', 'size': '4.00', 'funds': '0.00', 'side': 'sell', 'type': 'limit',
     'time_in_force': 'GTC'},
    {'order_id': 15, 'user_id': 15, 'price': '3697', 'size': '1.00', 'funds': '0.00', 'side': 'sell', 'type': 'limit',
     'time_in_force': 'GTC'},
    {'order_id': 21, 'user_id': 21, 'price': '3684', 'size': '4.00', 'funds': '0.00', 'side': 'sell', 'type': 'limit',
     'time_in_force': 'GTC'},
    {'order_id': 14, 'user_id': 14, 'price': '3682', 'size': '3.00', 'funds': '0.00', 'side': 'sell', 'type': 'limit',
     'time_in_force': 'GTC'},
    {'order_id': 17, 'user_id': 17, 'price': '3664', 'size': '4.00', 'funds': '0.00', 'side': 'sell', 'type': 'limit',
     'time_in_force': 'GTC'},
    {'order_id': 16, 'user_id': 16, 'price': '3664', 'size': '4.00', 'funds': '0.00', 'side': 'sell', 'type': 'limit',
     'time_in_force': 'GTC'},
    {'order_id': 20, 'user_id': 20, 'price': '3651', 'size': '4.00', 'funds': '0.00', 'side': 'sell', 'type': 'limit',
     'time_in_force': 'GTC'}]

buys = [{'order_id': 1, 'user_id': 1, 'price': '3598', 'size': '1.00', 'funds': '0.00', 'side': 'buy', 'type': 'limit',
         'time_in_force': 'GTC'},
        {'order_id': 2, 'user_id': 2, 'price': '3597', 'size': '5.00', 'funds': '0.00', 'side': 'buy', 'type': 'limit',
         'time_in_force': 'GTC'},
        {'order_id': 3, 'user_id': 3, 'price': '3549', 'size': '5.00', 'funds': '0.00', 'side': 'buy', 'type': 'limit',
         'time_in_force': 'GTC'},
        {'order_id': 6, 'user_id': 6, 'price': '3534', 'size': '3.00', 'funds': '0.00', 'side': 'buy', 'type': 'limit',
         'time_in_force': 'GTC'},
        {'order_id': 8, 'user_id': 8, 'price': '3525', 'size': '1.00', 'funds': '0.00', 'side': 'buy', 'type': 'limit',
         'time_in_force': 'GTC'},
        {'order_id': 4, 'user_id': 4, 'price': '3521', 'size': '3.00', 'funds': '0.00', 'side': 'buy', 'type': 'limit',
         'time_in_force': 'GTC'},
        {'order_id': 10, 'user_id': 10, 'price': '3517', 'size': '2.00', 'funds': '0.00', 'side': 'buy',
         'type': 'limit', 'time_in_force': 'GTC'},
        {'order_id': 5, 'user_id': 5, 'price': '3517', 'size': '2.00', 'funds': '0.00', 'side': 'buy', 'type': 'limit',
         'time_in_force': 'GTC'},
        {'order_id': 7, 'user_id': 7, 'price': '3511', 'size': '4.00', 'funds': '0.00', 'side': 'buy', 'type': 'limit',
         'time_in_force': 'GTC'},
        {'order_id': 9, 'user_id': 9, 'price': '3507', 'size': '3.00', 'funds': '0.00', 'side': 'buy', 'type': 'limit',
         'time_in_force': 'GTC'}]

import asyncio
import websockets
import json

# Replace with your Kafka topic and server details
KAFKA_TOPIC = 'your_topic'
KAFKA_SERVER = 'localhost:9092'


async def send_message_to_websocket(message):
    async with websockets.connect('ws://localhost:8765') as websocket:
        await websocket.send(message)
        print(await websocket.recv())


def consume_kafka_messages():
    data = json.dumps({"bids": buys, "asks": sells})

    asyncio.run(send_message_to_websocket(data))


if __name__ == "__main__":
    consume_kafka_messages()
