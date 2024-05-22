from currency_converter import CurrencyConverter


def main():
    print("this is currency converter")
    
    amount = int (input("Enter the Amount:"))
    from_currency=input("From Currency code :").upper()
    to_currency=input("to Currency code :").upper()
   
    c=CurrencyConverter()
    converted_amount = c.convert(amount , from_currency , to_currency)
    print(f"This {amount} {from_currency} in {to_currency} is :{converted_amount}")

main()