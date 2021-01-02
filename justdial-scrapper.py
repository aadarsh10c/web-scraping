from bs4 import BeautifulSoup as BS
from requests import get
from datetime import date
import re
import json


date = date.today()

#Mobile codes
zip={"icon-acb":"0",
"icon-nm":"7",
"icon-ji":"9",
"icon-ts":"4",
"icon-wx":"2",
"icon-yz":"1",
"icon-lk":"8",
"icon-rq":"5",
"icon-po":"6",
"icon-vu":"3",
"icon-dc":"+",
"icon-fe":"(",
"icon-hg":")",
"icon-ba":"-"}

def url_to_file(url):
    """extract data from 
    url to file 
    """
    headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.66'}
    data=get(url,headers=headers)
    print(data.status_code)
    return data
    
def save_to_file(text):
    
    with open(f"report_{date}.json","w",encoding='utf-8') as f:
        json.dump(text,f)
        
def getPhone(spanList):
    """return phone number"""
    phoneNumber=''
    if spanList != None:
        for list in spanList:
            coded=list.get('class')
            number=zip.get(coded[1],'*')
            phoneNumber+=number
    else:
        phoneNumber="No Phone Number"
    return phoneNumber


data=url_to_file("https://www.justdial.com/Delhi/Pharmacies-in-Gurgaon/nct-10096237")  

soup=BS(data.content, 'lxml')

#find all the addresses with class name store-name

#1.Finda all
storeNames=soup.find_all('div',class_='col-sm-5 col-xs-8 store-details sp-detail paddingR0')
#store name
businessDetails=[]
count=1
for stores in storeNames:
    eachStore={'No.':count}
    
    #Extract name of each store and insert it in dictionary
    name=stores.find('h2',class_='store-name').text.strip()
    eachStore['Store Name']=name
    
    #extract phone numbers and inset it into dicitonary
    phone = stores.find('p',class_='contact-info')
    try:
        spanList=phone.select("span[class*='mobilesv']")
    except:
        spanList = None

    #Extract Phone number
    phoneNumber = getPhone(spanList)
    eachStore["Phone Number"]=phoneNumber

    #Extract Address
    mrehover =stores.find('span',class_='mrehover dn') 
    address = stores.find('span', class_='cont_fl_addr').text
    eachStore["Address"]=address

    #Append each store details in businessDetails list
    businessDetails.append(eachStore)
            
    #print(businessDetails)
    #print("+++++++++++++++++++++")
    count+=1

save_to_file(businessDetails)
print("Extracton Sucessful")
