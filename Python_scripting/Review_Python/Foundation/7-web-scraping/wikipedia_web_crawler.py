
import requests
import urllib
import bs4
import time
#--------- Web Crawling in python -------------#
'''
1- pip install 'requests' module

2- in Ipython interpreter >>> import requests 

2 >>> response = requests.get('https://en.wikipedia.org/wiki/Dead_Parrot_sketch'
3 >>> print(response.text)
4 >>> print(type(response.text))
5 >>> print(type(response.json()))


-------- Using Beautifull Soup library to parse HTML -----------
>>> from bs4 import BeautifulSoup

>>> import requests

>>> response = requests.get('https://en.wikipedia.org')

>>> html = response.test

>>> print(html)

# Use the BeautifulSoup to parse the html
>>> soup = BeautifulSoup(html, 'html.parser')

>>> soup.title # get the page title

>>> soup.p  # get a paragraph

>>> soup.p.a # get a link in a paragraph

>>> for link in soup.find_all('a') #Get all the links in paragraph
         print(link.get('href'))

# ---> see library documentation for more info/tutorial


-------------------The Sequence of Steps
We've determined that our program will be structured in a while loop. Earlier on we establish the steps that need to go in the loop

1 - Find the first link in the current article's HTML
2 - Download the HTML for the current article
3 - Add the first link from the current article to article_chain
  There's one other step we didn't explicitly state earlier:

4 - Pause for a couple seconds so we don't flood Wikipedia with requests.

------------Psaudocode ----------------
page = a random starting page
article_chain = []
while title of page isn't 'Philosophy' and we have not discovered a cycle:
    append page to article_chain
    download the page content
    find the first link in the content
    page = that link
    pause for a second


'''
start_url = "https://en.wikipedia.org/wiki/Special:Random"


target_url = "https://en.wikipedia.org/wiki/Philosophy"
article_chain = [start_url]


def find_first_link(url):
    response = requests.get(url)
    html = response.text
    soup = bs4.BeautifulSoup(html, "html.parser")
    
    # This div contains the article's body
    # (Dec 2020 Note: Body nested in two div tags)
    content_div = soup.find(id="mw-content-text").find(class_="mw-parser-output")

    # stores the first link found in the article, if the article contains no
    # links this value will remain None
    article_link = None

    # Find all the direct children of content_div that are paragraphs
    for element in content_div.find_all("p", recursive=False):
        # Find the first anchor tag that's a direct child of a paragraph.
        # It's important to only look at direct children, because other types
        # of link, e.g. footnotes and pronunciation, could come before the
        # first link to an article. Those other link types aren't direct
        # children though, they're in divs of various classes.
        if element.find("a", recursive=False):
            article_link = element.find("a", recursive=False).get('href')
            break

    if not article_link:
        return
    # Build a full url from the relative article_link url
    #first_link = requests.compat.urljoin('https://en.wikipedia.org/', article_link)
    first_link = urllib.parse.urljoin('https://en.wikipedia.org/', article_link)
    
    return first_link

def continue_crawl(search_history, target_url, max_steps=25):
    if search_history[-1] == target_url:
        print("We've found the target article!")
        return False

    elif len(search_history) > max_steps:
        print("The search has gone on suspiciously long, aborting search!")
        return False
        
    elif search_history[-1] in search_history[:-1]:
        print("We've arrived at an article we've already seen, aborting search")
        return False

    else:
        return True

article_chain = [start_url]

while continue_crawl(article_chain, target_url):
    print(article_chain[-1])

    first_link = find_first_link(article_chain[-1])
    if not first_link:
        print("We've arrived at an article with no links, aborting search!")
        break
    article_chain.append(first_link)
    
     # Slow things down so as to not hammer Wikipedia's servers
    time.sleep(2)

