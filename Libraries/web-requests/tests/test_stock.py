import sys 
import os 

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from stock import build_url

def test_build_url(): 
    assert build_url('stocks') == 'https://api.freeapi.app/api/v1/public/stocks?'

    assert build_url('stocks', {
        "page": 1,
        "limit": 1,
        "inc": 'Symbol,Name,MarketCap,CurrentPrice',
        "query": 'tata'
    }) == 'https://api.freeapi.app/api/v1/public/stocks?page=1&limit=1&inc=Symbol%2CName%2CMarketCap%2CCurrentPrice&query=tata'

    assert build_url('books', {
        'page': 2,
        'limit': 10,
        'inc': 'Name,CurrentPrice',
        'query': 'sbi'
    }) == 'https://api.freeapi.app/api/v1/public/books?page=2&limit=10&inc=Name%2CCurrentPrice&query=sbi'

    assert build_url('') == 'https://api.freeapi.app/api/v1/public/?'