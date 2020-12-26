from bs4 import BeautifulSoup
from requests import get
from datetime import date

'''
Our objective is to extract 
the top stories column, containing
each headline and summary and authors name
'''
date = date.today()
def url_to_file(url):
    """
    saves the source content of the webpage
    to a file
    """
    
    try:
        r = get(url)
        print(r.status_code)
        if r.status_code == 200:
            try:
                with open(f'print-{date}.html', 'w') as f:
                    f.write(r.text)
            except UnicodeEncodeError as e:
                print("Unicode error :using encodeing utf-8")
                with open(f'print-{date}.html', 'w', encoding="utf-8") as f:
                    f.write(r.text)
        else:
            print("passing headers")
            headers = {"user-agent":"Edg/87.0.664.66"}
            r = get(url, headers=headers)
            print(r.status_code)
            if r.status_code == 200:
                try:
                    with open(f'print-{date}.html', 'w') as f:
                        f.write(r.text)
                except UnicodeEncodeError as e:
                    print("Unicode error: using encodeing utf-8")
                    with open(f'print-{date}.html', 'w', encoding="utf-8") as f:
                        f.write(r.text)
            else:
                print(f"Unable to send requests {r.status_code}")
        return r
    except Exception  as e:
        print("Error occured",e)

def soup_to_file(text):    
    try:
        with open("report.txt",'w') as f:
            f.write(text)
    except:
        print("Unicode error: using encodeing utf-8")
        with open("report.html",'w', encoding = 'utf-8') as f:
            f.write(str(soup.prettify()))


url="https://theprint.in/"
r = url_to_file(url)

if r:
    soup = BeautifulSoup(r.text,'lxml')
    print("Parsing soup")
    topStories = soup.find('div',class_="td_module_column").find_all('div',class_="td-module-meta-info")
    #print(len(topStories))
    #soup_to_file(str(topStories))
    count=1
    column=""
    for story in topStories:
        link=story.a.get('href')
        summary = story.a.text
        author = story.span.a.text
        column += f"{count}.{summary} \n author:{author} \n link:{link}\n\n"
        count+=1
    soup_to_file(column)
        