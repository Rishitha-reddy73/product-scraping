#import the packages required
import requests
from bs4 import BeautifulSoup
import pandas as pd

#get the requests url
r=requests.get('https://www.amazon.in/s?rh=n%3A6612025031&fs=true&ref=lp_6612025031_sar')
#parsing the content using html parser
soup=BeautifulSoup(r.content,"html.parser")
#This will prettify the content
soup.prettify()

#This will extract the span tags with class as mentioned below.
t1=soup.find_all('span',class_='a-size-base-plus a-color-base a-text-normal')
t2=soup.find_all('div',class_='a-section a-spacing-small puis-padding-left-small puis-padding-right-small')

c=1
prod_names=[]
prod_price=[]
ratings=[]
for i in t2:
    try:
        #We print the details of every item individually.
        name=i.find('span',class_='a-size-base-plus a-color-base a-text-normal').text
        price=i.find('span',class_='a-price-whole').text
        rating=i.find('span',class_='a-icon-alt').text
        prod_names+=[name]
        prod_price+=[price]
        ratings+=[rating]
        #printing the details to the terminal
        print(c,"-->",name)
        print('price: ',price)
        print('Rating: ',rating)
        c+=1
    except AttributeError:
        #It will print out-of-stock message in case of empty fields
        print("Out of stock!!")
    finally:
        #This will create a dataframe with the product names, prices, ratings scraped from the product page.
        df=pd.DataFrame({'Product Name':prod_names,'Price':prod_price,'Rating':ratings})
        #This will create a CSV file with the dataframe. The csv file is named as 'products.csv'
        df.to_csv('products.csv',index=False,encoding='utf-8')
