#!/usr/bin/env python
import bs4, requests, webbrowser

def getWebInfo(productUrl, cssSelector):
	req = requests.get(productUrl) # , headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36"})
	req.raise_for_status()
	soup = bs4.BeautifulSoup(req.text, 'html.parser')
	elements = soup.select(cssSelector)
	print(elements)
	return elements[0].text.strip()
	#webbrowser.open(productUrl)
	#return "TEST"

# passing the ULR target
#url = 'https://www.amazon.com.br/Automate-Boring-Stuff-Python-Programming/dp/1593275994'
#url = 'https://www.amazon.com.br/Curso-Intensivo-Python-Introdução-Programação/dp/8575225030'
url = 'https://xkcd.com'
# passing the CSS Selector
# amazon selector # selector = 'div.a-section div#soldByThirdParty.a-row span.a-size-medium.a-color-price.inlineBlock-display.offer-price.a-text-normal.price3P'
selector = '#ctitle'

result = getWebInfo(url, selector)
print('The title is ' + result)

# TODO: 1 - for xkcd find previous page and iterate more then 3 times
# TODO: 2 - pass ULR and Selector as sys.argv
# TODO: 3 - save the the result in a file or create a logging...
