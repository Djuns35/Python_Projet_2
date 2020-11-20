import requests
from bs4 import BeautifulSoup


class Requester:

    def __init__(self):
        pass

    def html_requester(self, url):
        response = requests.get(url)

        if response.status_code == 200:
            request_html = BeautifulSoup(response.content.decode('utf-8', 'ignore'), features="html.parser")
            request_html.encode("utf8")
            return request_html

        else:
            exit()
