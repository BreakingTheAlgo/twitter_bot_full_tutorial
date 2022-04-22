from bs4 import BeautifulSoup
import requests

reddit_url = "https://www.reddit.com/r/unpopularopinion/new/"

def generate_body(user_agent):

    print("Generating post body text...")

    title = ""

    headers = {
        'User-agent': user_agent
    }

    page = requests.get(reddit_url, headers=headers)

    soup = BeautifulSoup(page.text, "html.parser")

    first_post_title = soup.find('h3')

    if first_post_title is not None and first_post_title.text != '':
        title = first_post_title.text[:137] + '...'
        print("Body text found: " + title)
    else:
        print("Body text not found!")

    return title
