#!/usr/bin/env python
import bs4, requests, webbrowser

def getPrice(productUrl, cssSelector):
	req = requests.get(productUrl, headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36"})
	req.raise_for_status()
	soup = bs4.BeautifulSoup(req.text, 'html.parser')
	elements = soup.select(cssSelector)
	print(elements)
	return elements[0].text.strip()
	#webbrowser.open(productUrl)
	#return "TEST"

# passing the ULR target
url = 'https://www.amazon.com.br/Automate-Boring-Stuff-Python-Programming/dp/1593275994'
#url = 'https://www.amazon.com.br/Curso-Intensivo-Python-Introdução-Programação/dp/8575225030'
# passing the CSS Selector
#selector = 'div.a-section div#soldByThirdParty.a-row span.a-size-medium.a-color-price.inlineBlock-display.offer-price.a-text-normal.price3P'
selector = '.inlineBlock-display'

price = getPrice(url, selector)
print('The price is ' + price)
