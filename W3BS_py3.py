#
# W3BS is used for collecting headlines from major news sites
#

import requests
import os
from bs4 import BeautifulSoup
import re
import KYS # multi-purpose AI 

'''
2 BIG variables are 'return_t' and 'substance'. both include the same thing but 'substance' is in list form.
'return_t' is for KYS while 'substance' is for display output

1 MORE important variable is 'headlines'. extraction of headlines from 'substance'
'''

def yahoo(soup):
	global return_t ; return_t+='\nYAHOO\n\n'
	global headlines ; headlines+='\nYAHOO\n'
	substance = [] ; substance.append(' [+] YAHOO\n')
	#main headline
	access_maintitle = str(soup.find_all('h2', id='ntk-title'))
	start = access_maintitle.find('ntk-title')
	end = access_maintitle.find('</h2>]')
	substance.append(access_maintitle[start+11 : end])
	print('\n',substance[0]) ; print(substance[1])
	return_t+=str(substance[1])+'\n'
	headlines+=str(substance[1])+'\n'
	return substance

def fox(soup):
	global return_t ; return_t+='\nFOX\n\n'
	global headlines ; headlines+='\nFOX\n' ; j = 0
	print('\n [ + ] F O X')
	h2_container = soup.find_all('h2', class_='title title-color-default')
	substance = [] ; substance.append(' [+] FOX\n')
	for h2 in h2_container:
		h21 = h2.find_all('a')
		for h22 in h21:
			print(h22.get_text())
			substance.append(h22.get_text())
			return_t+=(str(h22.get_text())+'\n')
			if j == 0 or j == 1 or j == 10: # 10th title is the headline for fox
				headlines+=(str(h22.get_text())+'\n')
			j+=1
	return substance # return value for KYS
	#access_headline = 
	#print('\n'+access_headline)
	'''
	access_headline = str(soup.prettify)
	substance = re.findall('headline', access_headline)
	print(substance[0])
	'''
	#access_headline = str(soup.prettify)

def cnn(soup):
	global return_t ; return_t+='\nCNN\n\n'
	global headlines ; headlines+='\nCNN\n' ; j = 0
	script_container = soup.find_all('script')
	a1 = script_container[2].string # 2 is a stationary value
	b1 = a1.split('headline')
	substance = [''] ; print('\n [ + ] CNN', end='')
	for i in range (1, len(b1)): # print out the all articles, exactly len(b1) amount of articles
		c1 = b1[i]
		c1 = c1[3:c1.index('"', 3)] # c1.index('"', 3) = search for '"' in c1 starting from c1[3]
		#print(c1)
		try: 
			substance.append(str(c1))
		except Exception:
			substance.append(c1)
	for i in range(0, len(substance)):
		print(substance[i])
		return_t+=(str(substance[i])+'\n')
		if j == 2 or j == 7:
			headlines+=(str(substance[i])+'\n')
		if j == 8: # 8th article on CNN is parsed wierdly always so we need to handle that
			start = str(substance[i]).find('>')
			end = str(substance[i]).find('\\u003c/strong>')
			headlines+=(str(substance[i]))[start+1:end]
		j+=1
	return substance # return value for KYS
'''
	ul_container = soup.find_all('ul')
	for i in range(0, len(ul_container)):
		#print ul_container[i].find_all(class_='cd cd--card cd--article cd--idx-0 cd--large cd--vertical cd--has-siblings cd--has-media cd--media__image cd--has-banner')
		li_container = ul_container[i].find_all('li')

	for i in range(0, len(li_container)):
		li_container[i].article
'''
	#access_headline = str(soup.find_all('h2', class_='banner-text screaming-banner-text banner-text-size--char-47'))

	#print(soup.prettify)

def access(pagetext, num):
	soup = BeautifulSoup(pagetext,'html.parser')
	#a = soup.prettify()
	#print(soup.find_all(class_="chorus"))
	# soup.find_all(id="third")
	# soup.find_all('p', class_="chorus")
	substance = []
	if num == 0:
		substance1 = yahoo(soup)
		return substance1
	elif num == 1:
		substance2 = fox(soup)
		return substance2
	elif num == 2:
		substance3 = cnn(soup)
		return substance3
	#access_maintitle_prettify = re.findall(r'"(.*?)"', access_maintitle)	
	#print(access_maintitle[start+11])
	#print(access_maintitle[end-1])

def main():
	global return_t
	i = 0 ; j = 0 ; substance = []
	url = ['https://us.yahoo.com', 'https://www.foxnews.com', 'https://edition.cnn.com']
	for u in url:
		page = requests.get(u) # retrieve html of page u
		j+=1
		if page.status_code == 200:
			ret_value = access(page.text, i) # primary function of this program access()
			substance.append(ret_value)
		else:
			print("Error "+page)
			break
		i=i+1

	# response
	#KYS.ALPHA_read(return_t) # send article text to KYS for text-to-speech (reads out all article titles)
		# headline titles only
	KYS.ALPHA_read(headlines) # (read headline titles only)

headlines = ''
return_t = ''
main()
'''
soup.head.title :: returns <title></title> tags

'''