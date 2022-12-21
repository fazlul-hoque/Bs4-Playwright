
#https://stackoverflow.com/questions/74373189/how-to-get-a-list-of-all-links-from-a-dynamic-web-page/74374495#74374495

from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

data = []
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context(viewport={"width": 1920, "height": 1080})
    page = context.new_page()
    page.goto('https://workspace.google.com/marketplace/search/word')
    page.wait_for_timeout(4000)

    soup = BeautifulSoup(page.content(), 'lxml')
    for card in soup.select('a.RwHvCd'):
        link = 'https://workspace.google.com' + card.get('href').replace('./', '/') 
        print(link)