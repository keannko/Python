from typing import Mapping
import requests


def get_info():
    response = requests.get("https://yobit.net/api/3/info")

    with open("info.txt", "w") as file:
        file.write(response.text)

    return response.text

def get_ticker(coin1="doge", coin2="usdt" ):
    response = requests.get(f"https://yobit.net/api/3/ticker/{coin1}_{coin2}?ignore_invalid=1")

    with open("ticker.txt", "w") as file:
        file.write(response.text)

def get_depth(coin1="doge", coin2="usdt", limit=150):
    response = requests.get(f"https://yobit.net/api/3/depth/{coin1}_{coin2}?limit={limit}&ignore_invalid=1")

    with open("depth.txt", "w") as file:
        file.write(response.text)


def main():
    print(get_depth())

if __name__ == "__main__":
    main()