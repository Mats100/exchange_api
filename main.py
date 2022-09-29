import requests

api_key = " 7d6e4eb5d0ace911ba59089d"

def get_data():
    currency = input("Enter Currency:")
    url = f'https://v6.exchangerate-api.com/v6/7d6e4eb5d0ace911ba59089d/latest/{currency}'

    if requests.get(url).status_code == 200:
        data = requests.get(url).json()
        print(f'Last Updated time {data["time_last_update_utc"]}\n')
        print(f'United States Dollar = {data["conversion_rates"]["USD"]}\n'
            f'United Arab Emirates Dirham = {data["conversion_rates"]["AED"]}\n'
            f'British Pound Sterling = {data["conversion_rates"]["GBP"]}\n'
            f'Europe Union = {data["conversion_rates"]["EUR"]}\n'
            f'Australian Dollar = {data["conversion_rates"]["AUD"]}\n'
            f'Pakistani Rupee = {data["conversion_rates"]["PKR"]}\n'
            f'Indian Rupee = {data["conversion_rates"]["INR"]}\n'
            f'Bangladeshi Taka = {data["conversion_rates"]["BDT"]}\n'
            f'Saudi Riyal = {data["conversion_rates"]["SAR"]}\n'
            f'Qatari Riyal = {data["conversion_rates"]["QAR"]}\n'
            f'Kuwaiti Dinar = {data["conversion_rates"]["KWD"]}\n'
            f'Turkish Lira = {data["conversion_rates"]["TRY"]}')
    else:
        print("Currency not found")

get_data()
