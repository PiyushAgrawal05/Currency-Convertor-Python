import requests
from country_code import countries_and_currencies
import json

# getting the base country and the final country
base_country = input("Enter the base country you wish to get the exchange rate of:")
country = countries_and_currencies[base_country.title()]
to_country = input("Enter the country you want to get the exchange value of from the base country:")
final_country = countries_and_currencies[to_country.title()]
amount = int(input('Enter the amount you want to get the exchange value of:'))

url = f'https://v6.exchangerate-api.com/v6/41c7f2f16235a7dd82e05159/latest/{country}'

# getting request 
api_request = requests.get(url)
data = json.loads(api_request.text)

# calculating the final amount
final_amount = amount*data['conversion_rates'][final_country]
print(f'{amount}{country} = {final_amount}{final_country}')