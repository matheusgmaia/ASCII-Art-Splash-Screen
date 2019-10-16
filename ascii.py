import random
import requests
i = random.randrange(9) + 1 
website="https://raw.githubusercontent.com/matheusgmaia/ASCII-Art-Splash-Screen/master/art/"+ str(i) + ".txt"
try:
    print(requests.get(website, timeout=2).text)
except:
    print("Ta sem internet. Ps: Te amo amo")
