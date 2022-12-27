from bs4 import BeautifulSoup
import requests

url = "https://www.flipkart.com/cameras/dslr-mirrorless/pr?sid=jek%2Cp31%2Ctrv&p%5B%5D=facets.fulfilled_by%255B%255D%3DFlipkart%2BAssured&p%5B%5D=facets.type%255B%255D%3DMirrorless&param=179&ctx=eyJjYXJkQ29udGV4dCI6eyJhdHRyaWJ1dGVzIjp7InZhbHVlQ2FsbG91dCI6eyJtdWx0aVZhbHVlZEF0dHJpYnV0ZSI6eyJrZXkiOiJ2YWx1ZUNhbGxvdXQiLCJpbmZlcmVuY2VUeXBlIjoiVkFMVUVfQ0FMTE9VVCIsInZhbHVlcyI6WyJTaG9wIE5vdyEiXSwidmFsdWVUeXBlIjoiTVVMVElfVkFMVUVEIn19LCJ0aXRsZSI6eyJtdWx0aVZhbHVlZEF0dHJpYnV0ZSI6eyJrZXkiOiJ0aXRsZSIsImluZmVyZW5jZVR5cGUiOiJUSVRMRSIsInZhbHVlcyI6WyJUb3AgTWlycm9ybGVzcyBDYW1lcmFzIl0sInZhbHVlVHlwZSI6Ik1VTFRJX1ZBTFVFRCJ9fSwiaGVyb1BpZCI6eyJzaW5nbGVWYWx1ZUF0dHJpYnV0ZSI6eyJrZXkiOiJoZXJvUGlkIiwiaW5mZXJlbmNlVHlwZSI6IlBJRCIsInZhbHVlIjoiRExMRzJYRENGQlhWVVpUSCIsInZhbHVlVHlwZSI6IlNJTkdMRV9WQUxVRUQifX19fX0%3D&fm=neo%2Fmerchandising&iid=M_a317426a-6c86-4f6b-8d9e-bf3c2a63c31e_3.Q5LU1U8PHMK6&ssid=l4wt0557qo0000001672033009731&otracker=hp_omu_Best%2Bof%2BElectronics_2_3.dealCard.OMU_Q5LU1U8PHMK6_3&otracker1=hp_omu_PINNED_neo%2Fmerchandising_Best%2Bof%2BElectronics_NA_dealCard_cc_2_NA_view-all_3&cid=Q5LU1U8PHMK6"

response = requests.get(url)
htmlcontent = response.content

soup = BeautifulSoup(htmlcontent,"html.parser")


print(soup.a.attrs)
exit()
print(soup.find_all('a'))
print(soup.a)
print(soup.title.parent.name)
print(soup.title.string)
print(soup.title.name)
print(soup.title)



anchors = soup.find_all('a')
all_links = set()
for link in anchors:
    if link.get('href') != '#':
        linkText = "https://www.flipkart.com/" + link.get('href')
        all_links.add(linkText)


titles = []
prices = []
images = []

for d in soup.find_all('div',{'class':'_2kHMtA'}):
    title = d.find('div',attrs={'class':'_4rR01T'})
    price = d.find('div',attrs={'class':'_30jeq3 _1_WHN1'})
    image = d.find('img',attrs={'class':'_396cs4'})

    # e = d.parents
    # for i in e:
    #     print(i)
    # p = price.stripped_strings
    # for i in p:
    #     print(i)

    titles.append(title.string)
    prices.append(price.string)
    images.append(image.get('src'))

# print(titles)
# print(prices)
# print(images)