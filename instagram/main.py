import instaloader

L = instaloader.Instaloader()
a = L.login("keannko@bigmir.net", "Prince547@")

for post in a.get_posts():
    L.download_post(post, target=a)
