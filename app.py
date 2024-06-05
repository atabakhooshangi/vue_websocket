import streamlit as st
import pandas as pd
import asyncio
import websockets
import json
import threading

st.set_page_config(page_title="Real-Time Order Book", layout="wide")

st.markdown("""
    <style>
    .dataframe tbody tr:nth-child(even) {
        background-color: #333333;
    }
    .dataframe thead {
        background-color: #222222;
    }
    .dataframe thead th {
        color: white;
    }
    .dataframe tbody tr:hover {
        background-color: #444444;
    }
    .price {
        color: #FF4136;  /* Red color for asks */
    }
    .amount {
        color: #01FF70;  /* Green color for bids */
    }
    </style>
    """, unsafe_allow_html=True)

st.title("Real-Time Order Book")

bids_placeholder = st.empty()
asks_placeholder = st.empty()

order_book = {"bids": [], "asks": []}

def update_order_book(bids, asks):
    bids_df = pd.DataFrame(bids, columns=["price", "size"])
    asks_df = pd.DataFrame(asks, columns=["price", "size"])

    # Format the dataframes
    bids_df['price'] = bids_df['price'].apply(lambda x: f'<span class="price">{x}</span>')
    asks_df['price'] = asks_df['price'].apply(lambda x: f'<span class="price">{x}</span>')

    bids_df['size'] = bids_df['size'].apply(lambda x: f'<span class="amount">{x}</span>')
    asks_df['size'] = asks_df['size'].apply(lambda x: f'<span class="amount">{x}</span>')

    # Display dataframes
    bids_placeholder.markdown(bids_df.to_html(escape=False, index=False), unsafe_allow_html=True)
    asks_placeholder.markdown(asks_df.to_html(escape=False, index=False), unsafe_allow_html=True)

async def websocket_listener():
    async with websockets.connect('ws://localhost:8765') as websocket:
        while True:
            message = await websocket.recv()
            data = json.loads(message)
            update_order_book(data["bids"], data["asks"])

def start_websocket_listener():
    asyncio.run(websocket_listener())

# Run WebSocket listener in a separate thread
websocket_thread = threading.Thread(target=start_websocket_listener)
websocket_thread.start()
