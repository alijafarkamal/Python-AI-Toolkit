import requests

def currency_converter():
    api_key = "256fca49ce0e78c320a81a19"  # Replace with your ExchangeRate-API key
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/USD"

    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to fetch exchange rates. Status code: {response.status_code}, Response: {response.text}")
        return
     
    rates = response.json().get("conversion_rates", {})
    if not rates:
        print(f"No exchange rate data found. Response: {response.json()}")
        return

    print("\nAvailable currencies:")
    for currency in list(rates.keys())[:20]:  # Displaying a sample of 20 currencies
        print(currency, end=", ")
    print("\n... and more.")

    base_currency = input("\nEnter the base currency (e.g., USD): ").upper()
    target_currency = input("Enter the target currency (e.g., EUR): ").upper()
    amount = float(input("Enter the amount to convert: "))

    if base_currency not in rates or target_currency not in rates:
        print("Invalid currency codes. Please try again.")
        return

    conversion_rate = rates[target_currency] / rates[base_currency]
    converted_amount = amount * conversion_rate

    print(f"\n{amount} {base_currency} = {converted_amount:.2f} {target_currency}")

currency_converter()
