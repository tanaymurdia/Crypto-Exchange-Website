from flask import Flask, render_template, request, redirect, jsonify
from json import dump
from rate import rate

app = Flask(__name__)

import logging

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

game = None

'''
Implement '/' endpoint
Method Type: GET
return: template index.html with exchange
Initial Webpage where gameboard is initialized
'''


@app.route('/', methods=['GET'])
def index_page():
    cur_rates=rate()
    cur_rates.bitcoin_rates_from_data1()
    cur_rates.etheruem_rates_from_data1()
    cur_rates.bitcoin_rates_from_data2()
    cur_rates.etheruem_rates_from_data2()
    cur_rates.bitcoin_rate_comparison()
    cur_rates.ethereum_rate_comparison()
    return render_template('index.html'
        ,bitcoin_buy=str(cur_rates.bitcoin_buy)
        ,bitcoin_buy1=str(cur_rates.bitcoin_buy1)
        ,bitcoin_sell=str(cur_rates.bitcoin_sell)
        ,bitcoin_sell1=str(cur_rates.bitcoin_sell1)
        ,ethereum_buy=str(cur_rates.ethereum_buy)
        ,ethereum_buy1=str(cur_rates.ethereum_buy1)
        ,ethereum_sell=str(cur_rates.ethereum_sell)
        ,ethereum_sell1=str(cur_rates.ethereum_sell1)
        ,bitcoin_winner=cur_rates.bitcoin_winner
        ,ethereum_winner=cur_rates.ethereum_winner)


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1')
