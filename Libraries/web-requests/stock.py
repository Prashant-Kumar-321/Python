from stock_client import StockClient
import sys

# Handling command line arguments
user_choice = None

if (len(sys.argv) <= 1): 
    sys.exit('Too few arguments')

else: 
    if user_choice == '1': 
        if len(sys.argv) < 3: 
            sys.exit('second argument not provided')
        query = sys.argv[2]

    elif user_choice != '2': 
        sys.exit('Not valid arguments')


def main():
    client = StockClient()

    if user_choice == '1': 
        data = client.get_stocks(14, query, ['Name','MarketCap', 'CurrentPrice', 'BookValue', 'FaceValue', 'StockPE'])
        client.display_stocks(data)
    else: 
        stock = client.get_random_stock()
        client.display_random_stock(stock)


if __name__ == "__main__": 
    main()



