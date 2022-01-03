import requests

img_url = "https://cdn.arstechnica.net/wp-content/uploads/2017/09/warcraft-iii-official-screen-2.jpg"
video_url = "https://www.instagram.com/p/CX06lQdMYJH/?utm_source=ig_web_copy_link"


def download_img(url):
    try:
        response = requests.get(url=url)

        with open("1.jpg", "wb") as file:
            file.write(response.content)

        return "Successdully download"

    except:
        return "Check your URL"


def download_video(url):
    try:
        response = requests.get(url=url)

        with open("1.mp4", "wb") as file:
            for chunk in response.iter_content(chunk_size=1024 * 1024):
                if chunk:
                    file.write(chunk)
         

        return "Successdully download"

    except:
        return "Check your URL"


def main():
    # print(download_img(img_url))
     print(download_video(video_url))


if __name__ == "__main__":
    main()
