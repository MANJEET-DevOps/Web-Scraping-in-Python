from bs4 import BeautifulSoup
import requests
name=[]
kilometers=[]
fuel=[]
transmission=[]
model=[]
price=[]
location=[]
url='https://www.cars24.com/buy-used-car?f=make%3A%3D%3Amaruti&sort=bestmatch&serveWarrantyCount=true&listingSource=Homepage_Filters&storeCityId=132'
html=requests.get(url).content
soup=BeautifulSoup(html,'lxml')
cars=soup.find_all('div','_2YB7p')
for car in cars:
    car_name=car.find('h3','_11dVb').get_text()
    name.append(car_name)
    car_kilometer = car.find('ul','_3J2G-').get_text().split('km')[0]
    kilometers.append(car_kilometer)
    fuel_type = car.find('ul', '_3J2G-').get_text().split('km')[1].replace('Manual','').replace('Automatic','')
    fuel.append(fuel_type)
    transmission_type = car.find('ul', '_3J2G-').get_text().split('km')[1].replace('Petrol','').replace('CNG','').replace('Diesel','')
    transmission.append(transmission_type)
    model_type = car.find('span','_3JoYA').get_text()
    model.append(model_type)
    car_price = car.find('div','_2KyOK').get_text()
    price.append(car_price)
    car_location = car.find('p', '_3dGMY').get_text()
    location.append(car_location)
dict={'name':name,
'kilometers':kilometers,
'fuel':fuel,
'transmission':transmission,
'model':model,
'price':price,
'location':location}
import pandas as pd
df=pd.DataFrame(dict)
print(df)
df.to_csv(r'C:\Users\india\Desktop\cars24.csv')