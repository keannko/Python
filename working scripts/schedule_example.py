import schedule
import requests


def greeting():
    todos_dict={
        '08:00':'Drink coffee',
        '11:00':'Working',
        '21:00':'Go sleep'
    }

    print("day's task")
    for k, v in todos_dict.items():
        print(f"{k} - {v}")


    crypto = ['btc_usd', 'doge_usd']

    for i in crypto:
        url = f'https://yobit.net/api/3/ticker/{i}'
        response = requests.get(url)
        data = response.json()
        price = round(data.get(f'{i}').get('last'),2)
        print(f"{i} : {price} $")

def main():
    greeting()
    # schedule.every(4).seconds.do(greeting)
    # schedule.every(4).minutes.do(greeting)
    # schedule.every().hour.do(greeting)

    schedule.every().day.at('09:27').do(greeting)
    schedule.every().thursday.do(greeting)
    schedule.every().friday.at('23:45').do(greeting)
    

    while True:
        schedule.run_pending()


if __name__=='__main__':
    main()