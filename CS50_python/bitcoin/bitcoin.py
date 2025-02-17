'''
Expects the user to specify as a command-line argument the number of Bitcoins,n,
that they would like to buy. If that argument cannot be converted to a float,
the program should exit via sys.exit with an error message.
Queries the API for the CoinDesk Bitcoin Price Index at https://api.coindesk.com/v1/bpi/currentprice.json,
which returns a JSON object, among whose nested keys is the current price of Bitcoin as a float.
Be sure to catch any exceptions.

Outputs the current cost of Bitcoins in USD to four decimal places, using , as a thousands separator.
'''
import sys
import requests
import json

def main():

    try:

        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()

        coin_rate = response["bpi"]["USD"]["rate_float"]

        #print(json.dumps(rate, indent = 2 ))
        #print(sys.argv[1], type(int(sys.argv[1])), coin_rate)
        print(f"${coin_rate * float(sys.argv[1]):,}")

    except ValueError:
        sys.exit("Command-line argument is not a number")

    except IndexError:
        sys.exit("Missing command-line argument")


if __name__ == "__main__":
    main()