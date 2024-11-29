from bs4 import BeautifulSoup
import requests
name=[]
color=[]
capacity=[]
discription=[]
ratings=[]
reviews=[]
averageratings=[]
url=rf'https://www.flipkart.com/search?q=phones&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off&page=1'
html=requests.get(url).content
soup=BeautifulSoup(html,'lxml')
phones=soup.find_all('div','yKfJKb row')
for phone in phones:
    phonename=phone.find('div','KzDlHZ').get_text().split('(')[0]
    name.append(phonename)
    phonecolor=phone.find('div','KzDlHZ').get_text().split('(')[1].split(',')[0]
    color.append(phonecolor)
    phonecapacity=phone.find('div','KzDlHZ').get_text().split(',')[1].replace(')',' ')
    capcity.append(phonecapacity)
    phonediscription=phone.find('ul','G4BRas').get_text().split('ROM')[1].replace('|',' ')
    discription.append(phonediscription)
    phoneratings=phone.find('div','XQDdHH').get_text()
    ratings.append(phoneratings)
    phonereviews=phone.find('span','Wphh3N').get_text().split('Ratings')[0].replace(',',' ')
    reviews.append(phonereviews)
    phone_averagerating=phone.find('span','Wphh3N').get_text().split('&')[1].replace('Review',' ')
    averageratings.append(phone_averageratings)
print(name)
print(color)
print(capacity)
print(discription)
print(ratings)
print(reviews)
print(averageratings)