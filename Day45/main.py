from bs4 import BeautifulSoup
import requests

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"


response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")


# print(soup.prettify())

texts = soup.find_all(name="h3", class_="title")
all_title = [text.getText() for text in texts]
all_title = all_title[::-1]
print(all_title)

with open(r"C:\Users\SN798EZ\Downloads\Self Study\Udemy-Python\Day45\movies.txt", mode="w", encoding="utf-8") as file:
    for movie in all_title:
        file.write(f"{movie}\n")


















# response = requests.get("https://news.ycombinator.com/")

# yc_web = response.text

# soup = BeautifulSoup(yc_web, "html.parser")
# articles_tags = soup.find_all(name="span", class_="titleline")
# articles = [article.find("a") for article in articles_tags]
# article_texts = [article.getText() for article in articles]
# article_links = [article.get("href") for article in articles]
# score_tags = soup.find_all(name="span", class_="score")
# article_scores = [article.getText() for article in score_tags]
# scores = [int(score.split(" ")[0]) for score in article_scores]

# largest = max(scores)
# index = scores.index(largest)

# print(article_texts[index])
# print(article_links[index])
# print(scores[index])
























# import lxml

# with open("C:\\Users\\SN798EZ\\Downloads\\Self Study\\Udemy-Python\\Day45\\website.html", encoding="utf-8") as file:
#     contents = file.read()


# soup = BeautifulSoup(contents, 'html.parser')
# # print(soup.title.string)

# # print(soup.prettify())

# # print(soup.p)

# all_anchor_tags = soup.find_all(name="a")
# # print(all_anchor_tags)

# for tag in all_anchor_tags:
#     # print(tag.getText())
#     # print(tag.get("href"))
#     pass

# heading = soup.find_all(name="h1", id="name")
# # print(heading)

# section_heading = soup.find(name="h3", class_="heading")
# # print(section_heading.get("class"))

# company_url = soup.select_one(selector="p a")
# # print(company_url)

# company_url = soup.select_one(selector="#name")
# # print(company_url)

# headings = soup.select(".heading")
# print(headings)