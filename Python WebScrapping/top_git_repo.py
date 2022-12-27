#We are going to scrape https://github.com/topics

#importing required libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd
import sqlalchemy


url = "https://github.com/topics"

response = requests.get(url)

contents = response.text

#creating html file of the page
with open('webpage.html', "w", encoding="utf-8") as f:
    f.write(contents)

doc = BeautifulSoup(contents,'html.parser')

topic_title_tags = doc.find_all('p',{'class':'f3 lh-condensed mb-0 mt-1 Link--primary'})

topic_desc_tags = doc.find_all('p',{'class':'f5 color-fg-muted mb-0 mt-1'})

topic_link_tags = doc.find_all('a',{'class':'no-underline flex-1 d-flex flex-column'})

topic_titles = []

for tag in topic_title_tags:
    topic_titles.append(tag.text)

topic_description = []

for tag in topic_desc_tags:
    topic_description.append(tag.text.strip())


topic_link = []
base_url = "https://github.com"

for tag in topic_link_tags:
    topic_link.append(base_url + tag['href'])

topic_dict = {
    "title": topic_titles,
    "description": topic_description,
    "urls": topic_link
}

#Converting into Dataframe
topic_df = pd.DataFrame(topic_dict)


topic_df.to_csv('topics.csv')

# Getting information about topic page
username = []
repo_name = []
stars = []
repu_url = []

topic_repo_dict = {
    "username":username,
    "repo_name":repo_name,
    "stars":stars,
    "repu_url":repu_url
}

#counting the stars of the repositories
def parse_star_count(stars_str):
        stars_str = stars_str.strip()
        if stars_str[-1] == 'k':
            return int(float(stars_str[:-1])* 1000)
        return int(stars_str)

#getting csv and storing data in the database
for index,i in enumerate(topic_link):

    response = requests.get(i)
    topic_doc = BeautifulSoup(response.text,'html.parser')
    repo_tags = topic_doc.find_all('h3',{'class':'f3 color-fg-muted text-normal lh-condensed'})

    for count,j in enumerate(repo_tags):
        a_tags = j.find_all('a')

        #getting username of the owner of repository
        name = a_tags[0].text.strip()
        topic_repo_dict["username"].append(name)

        #getting the repository name
        repo = a_tags[1].text.strip()
        topic_repo_dict["repo_name"].append(repo)

        #getting link of the repository
        repo_url = base_url + a_tags[1]['href']
        topic_repo_dict["repu_url"].append(repo_url)

        #getting the count of the stars of the repository
        star_tags = topic_doc.find_all('span',{'class':'Counter js-social-count'})
        star = parse_star_count(star_tags[count].string)
        topic_repo_dict["stars"].append(star)

    # converting data into dataframe
    topic_repo_df = pd.DataFrame(topic_repo_dict)
    topic_repo_df.to_csv(topic_titles[index]+ '.csv',index=None)
    
    #creating engine and storing data in the database
    engine = sqlalchemy.create_engine("postgresql://postgres:1713@localhost/webscrapping")
    topic_repo_df.to_sql(name = topic_titles[index],if_exists='replace',con = engine)

    username.clear()
    repo_name.clear()
    stars.clear()
    repu_url.clear()
