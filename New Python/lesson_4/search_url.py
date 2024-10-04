import re



text = (
    "The main search site in the world is https://www.google.com The main social network for people in the "
    "world is https://www.facebook.com But programmers have their own social network http://github.com There "
    "they share their code. some url to check https://www.facebook.com www.facebook.com https://www.app.facebook.com My site: https://krabaton.info  https://api.io"
)


pattern = re.compile(r"https?://w{3}\.[\w+_]+\.\w{2,5}")
urls = re.findall(pattern, text)
print(urls)