import mysql.connector

BYBIT_DATABSASE = 'BTC_candle_history'
BINANCE_DATABASE = 'binance_BTC_kline'

def target():
    "Fill each variable with your data base information"
    database = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = '1234',
        database = BINANCE_DATABASE
    )
    return database
