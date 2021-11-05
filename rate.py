import requests
class rate():
    def __init__(self):
        self.bitcoin=0
        self.ethereum=0
        self.bitcoin_buy=0
        self.bitcoin_sell=0
        self.bitcoin_buy1=0
        self.bitcoin_sell1=0
        self.ethereum_buy=0
        self.ethereum_sell=0
        self.ethereum_buy1=0
        self.ethereum_sell1=0
        self.bitcoin_winner=""
        self.ethereum_winner=""
    
    def bitcoin_rates_from_data1(self):
        response_bitcoin = requests.get('https://api.coinbase.com/v2/prices/BTC-USD/spot')
        data_bitcoin = response_bitcoin.json()
        self.bitcoin_buy=self.string_to_float(data_bitcoin["data"]["amount"])
        self.bitcoin_sell=self.string_to_float(data_bitcoin["data"]["amount"])

    def etheruem_rates_from_data1(self):
        response_etheruem = requests.get('https://api.coinbase.com/v2/prices/ETH-USD/spot')
        data_etheruem = response_etheruem.json()
        self.ethereum_buy=self.string_to_float(data_etheruem["data"]["amount"])
        self.ethereum_sell=self.string_to_float(data_etheruem["data"]["amount"])

    def bitcoin_rates_from_data2(self):
        response_bitcoin1 = requests.get('https://api.kucoin.com/api/v1/market/stats?symbol=BTC-USDT')
        data_bitcoin1 = response_bitcoin1.json()
        self.bitcoin_buy1=self.string_to_float(data_bitcoin1["data"]["buy"])
        self.bitcoin_sell1=self.string_to_float(data_bitcoin1["data"]["sell"])

    def etheruem_rates_from_data2(self):
        response_etheruem1 = requests.get('https://api.kucoin.com/api/v1/market/stats?symbol=ETH-USDT')
        data_etheruem1 = response_etheruem1.json()
        self.ethereum_buy1=self.string_to_float(data_etheruem1["data"]["buy"])
        self.ethereum_sell1=self.string_to_float(data_etheruem1["data"]["sell"])

    def string_to_float(self,s):
        s=s.replace(',','')
        format_float = "{:.2f}".format(float(s))
        return float(format_float)


    def bitcoin_rate_comparison(self):
        if self.bitcoin_buy < self.bitcoin_buy1:
            buy_win="Coinbase"
            buy_value=self.bitcoin_buy
        else:
            buy_win="KuCoin"
            buy_value=self.bitcoin_buy1 

        if self.bitcoin_sell > self.bitcoin_sell1:
            sell_win="Coinbase"
            sell_value=self.bitcoin_sell
        else:
            sell_win="KuCoin"
            sell_value=self.bitcoin_sell1 
        
        buy="Buy the bitcoin from "+str(buy_win)+" ,with the value "+str(buy_value)
        sell=" and sell the bitcoin to "+str(sell_win)+", for the value "+str(sell_value) 
        self.bitcoin_winner=buy+sell
    def ethereum_rate_comparison(self):
        if self.ethereum_buy < self.ethereum_buy1:
            buy_win="Coinbase"
            buy_value=self.ethereum_buy
        else:
            buy_win="KuCoin"
            buy_value=self.ethereum_buy1 

        if self.ethereum_sell > self.ethereum_sell1:
            sell_win="Coinbase"
            sell_value=self.ethereum_sell1
        else:
            sell_win="KuCoin"
            sell_value=self.ethereum_sell1 
        
        buy="Buy the etheruem from "+str(buy_win)+" ,with the value "+str(buy_value)
        sell=" and sell the etheruem to "+str(sell_win)+", for the value "+str(sell_value) 
        self.ethereum_winner=buy+sell