import requests
from bs4 import BeautifulSoup
import re

from requests.models import Response

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}

for x in range(0, 2):
    url = 'https://store.steampowered.com/category/racing/#p={x}&tab=NewReleases'
    r = requests.get(url, headers=headers)
    suop = BeautifulSoup(r.text, "html.parser") 
    New_Releases = suop.find('div', attrs={'id':'NewReleasesRows'})
    NewReleasesContents = suop.findAll('a', attrs={'class':'tab_item'})

    for NewReleasesContent in NewReleasesContents:
        imageUrl = NewReleasesContent.find('img', attrs={'class':'tab_item_cap_img'})['src']
        titles = NewReleasesContent.find('div', attrs={'class':'tab_item_name'}).text
        response = requests.get(imageUrl, headers=headers, stream=True)
        fileName = imageUrl.split("/")[-1].split("?")[0]
        ext = fileName[-4:]
        if response.ok:
            with open('images/' + re.sub(r'(?u)[^-\w.]', '-', titles) + ext, 'wb') as a:
                a.write(response.content)
