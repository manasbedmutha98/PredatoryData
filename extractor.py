
from bs4 import BeautifulSoup
import requests
import csv

url = "https://www.biomedcentral.com/journals-a-z"


page = requests.get(url)

htmlpage = page.text

soup = BeautifulSoup(htmlpage, 'html.parser')

#print(soup.prettify())

li = soup.findAll("li", {"class": "c-list-group__item"})

journal_links = [listitem.a['href'] for listitem in li]
journal_names = [listitem.a.text for listitem in li]

with open('Journal Names.csv', 'w') as writeFile:
	writer = csv.writer(writeFile)
	head = ['No.','Title','Link']
	writer.writerow(head)	

	for i in range(len(journal_names)):
		lines = [str(i+1), journal_names[i], 'http:'+journal_links[i]]
		#print(lines)
		writer.writerow(lines)	

#print(journal_links)

class journal():

	def __init__(self, name, link):
		self.name = name
		self.link = "http:"+link
		self.soup = ""
		self.pages = 0
		self.paper_name = []
		self.paper_link = []
		#print(self.link)

	def getsoup(self):
		page = requests.get(self.link+"/articles")
		self.soup = BeautifulSoup(page.text, 'html.parser')
		#return self.soup

	def getpages(self):
		size = self.soup.findAll("p", {"class": "u-text-sm u-reset-margin"})
		# print(size)
		size = size[0].text
		self.pages = int(size.split()[-1])
		# print(self.pages)
		#return self.pages

	def findpapers(self):
		for i in range(self.pages):
			link = self.link + "/articles?searchType=journalSearch&sort=PubDate&page="+str(i)
			page = requests.get(link)
			self.papersoup = BeautifulSoup(page.text, 'html.parser')

			papers = self.papersoup.findAll("h3", {"class": "c-teaser-old__title"})
			# print(papers)
			for item in papers:
				content = item.findChildren("a" , recursive=False)[0]
				pagelink = self.link+content['href']
				pdflink = pagelink.replace("articles","track/pdf")
				self.paper_link.append(pdflink)
				self.paper_name.append(content.text)

		self.paperqty = len(self.paper_link)
			# print(self.paper_name)
			# print(self.paper_link)

		# print("Papers: ",str(self.paperqty))

		import csv
		with open('./Links/'+self.name+'.csv', 'w') as writeFile:
			writer = csv.writer(writeFile)
			head = ['No.','Title','Link']
			writer.writerow(head)	
			for i in range(self.paperqty):
				lines = [str(i+1), self.paper_name[i], self.paper_link[i]]
				#print(lines)
				writer.writerow(lines)	


from tqdm import tqdm
import os
# filers = os.listdir("./")


for i in tqdm(range(3)): #len(journal_names)
	jour = journal(journal_names[i],journal_links[i])
	jour.getsoup()
	jour.getpages()
	jour.findpapers()


