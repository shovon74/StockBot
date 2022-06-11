from flask import Flask
from flask import request
from twilio.rest import Client
from marketstack import get_stock_price
import os
app = Flask(__name__)

ACCOUNT_ID = os.environ.get('TWILIO_ACCOUNT')
ACCOUNT_TOKEN = os.environ.get('TWILIO_TOKEN')
client = Client(ACCOUNT_ID,ACCOUNT_TOKEN)
TWILIO_NUMBER = 'whatsapp:+14155238886'

def send_msg(msg, recipient):
    client.messages.create(
        from_=TWILIO_NUMBER,
        body=msg,
        to=recipient

    )

def process_msg(msg):
    response = ""
    if msg == "Hi":
        response = "Hello, Welcome to the stock bot!"
        response += "Type Sym:<stock_symbol> to know the price of the stock."
    elif 'Sym:' in msg:
        data = msg.split(":")
        stock_symbol = data[1]
        stock_price = get_stock_price(stock_symbol)
        last_price = stock_price['last_price']
        last_price_str = str(last_price)
        response = "The stock price of " + stock_symbol + " is: $" + last_price_str
    else:
        response = "Please type hi to get started"
    return response

@app.route("/webhook", methods=["POST"])
def webhook():
    # import pdb
    # pdb.set_trace()
    f = request.form
    msg = f['Body']
    sender = f['From']
    response = process_msg(msg)
    send_msg(response, sender)
    return "OK", 200


#0 get account id and tiken frim twlio and set in env
#1 import client from twilio
#2 initialise client
#3 write a function to process message
#4 write a function to send message
#5 generate a response
#6 check response in whatsapp


# Sid: ACfce171749de24b888eccba1b005fe9a8
# Auth token:
# TWILIO_ACCOUNT, TWILIO_TOKEN