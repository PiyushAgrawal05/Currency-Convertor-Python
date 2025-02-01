import requests
from country_code import countries_and_currencies
import json

# getting the base country and the final country
base_country = input("Enter the base country you wish to get the exchange rate of:")
try:
    country = countries_and_currencies[base_country.title()]
except KeyError:
    print('Invalid country name')
    exit()
to_country = input("Enter the country you want to get the exchange value of from the base country:")
try:
    final_country = countries_and_currencies[to_country.title()]
except KeyError:
    print('Invalid country name')
    exit()
amount = int(input('Enter the amount you want to get the exchange value of:'))

url = f'https://v6.exchangerate-api.com/v6/41c7f2f16235a7dd82e05159/latest/{country}'

# getting request
try:
    api_request = requests.get(url)
    data = json.loads(api_request.text)
except Exception as e:
    print(f'An error occured: {e}')
    
# calculating the final amount
final_amount = amount*data['conversion_rates'][final_country]
print(f'{amount}{country} = {final_amount}{final_country}')
