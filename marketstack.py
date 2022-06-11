#imports
import os
import requests
import json

API_KEY = os.environ.get("MARKETSTACK_KEY")
BASE_URL = 'http://api.marketstack.com/v1'

def get_stock_price(stock_symbol):
    params = {
        'access_key': '3d418be13622ed6e347ab549bfce8401'
    }
    end_point = ''.join([BASE_URL,"/tickers/",stock_symbol,"/intraday/latest"])
    api_result = requests.get(end_point, params)
    json_result = json.loads(api_result.text)
    return{
        "last_price": json_result["last"]
    }







# MARKETSTACK_KEY=3d418be13622ed6e347ab549bfce8401