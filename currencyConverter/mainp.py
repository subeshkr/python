# mainp

import argparse
from converter import convert

def main():
    parser = argparse.ArgumentParser(description="Currency Converter")
    parser.add_argument("from_currency", help="The currency you are converting from (e.g., AUD)")
    parser.add_argument("to_currency", help="The currency you are converting to (e.g., USD)")
    parser.add_argument("amount", type=float, help="The amount you want to convert")
    args = parser.parse_args()

    result = convert(args.amount, args.from_currency.upper(), args.to_currency.upper())
    print(f"{args.from_currency.upper()} {args.amount} = {args.to_currency.upper()} {result}")

if __name__ == "__main__":
    main()
