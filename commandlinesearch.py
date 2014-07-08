from bs4 import BeautifulSoup
import urllib2
import sys #Used for command line arguments
import re


def search (searchTerm, start="0"):
	stripped = searchTerm.replace(" ", "+")
	url = "https://www.google.ca/search?q=" + stripped + "&start="+str(start)
	hdr = {'User-Agent': 'Mozilla/5.0'}
	req = urllib2.Request(url,headers=hdr)
	soup = BeautifulSoup(urllib2.urlopen(req))
	headings = soup.find_all('h3')
	descriptions = soup.find_all (class_='st')
	for item in headings: #Returns Search Result Headings
		element = re.search('">(.*?)</a>', str(item.next_element))
		element = element.group()
		element = element[2:-4]
		element = element.replace("<b>", '\033[36m\033[1m')
		element = element.replace("</b>", '\033[0m\033[0m')
		print element

start = 0
arguments = sys.argv

if len(arguments) > 1:
	arguments.pop(0)  #Remove the file from the arguments
	term = "+".join(arguments)
	print term
else:
	term = str(raw_input("Enter your Search Term: "))

search (term)
print ("Type exit, help, new, more, or nav[result#]")
while True:
	command = raw_input ("\033[31m\033[1m"+" >>>\033[0m\033[0m ")
	command = command.replace(" ", '')
	if command == 'exit':
		break
	elif command == 'help':
		print ("Help Text")
	elif command == 'new':
		start = 0
		term = str(raw_input("Enter your Search Term: "))
		search (term)
	elif command == 'more':
		start += 10
		search(term,start)
	elif command[:3] == 'nav':
		print ("selected option: "+command[4:-1])
	else:
		print ("Command Not Recognized.")
		print ("Type exit, help, new or nav[result#]")



