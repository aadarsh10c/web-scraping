from bs4 import BeautifulSoup

with open('simple.html') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')
    
#print content of soup object
#this command prints contents of HTML
#with all the indents, i.e in a pretty
#way
#print(soup.prettify())

#Now if i want to print only the title
#its O/P is :<title>Test - A Sample Website</title>
print(soup.title)

#now if i only want the text part of the title
#O/P:Test - A Sample Website
print(soup.title.text)

#now if want to print the content of specfic div tag
#then u will have to specify the attribute
#note in below 'class_' is used to access class
#attriute ,because to not to confuse with python 'class'
#keyword
#print(soup.find('div', class_='article'))

'''
Now if we want to access the head line within the 
article 
'''
#article=soup.find('div',class_='article')
#headline = article.a.text
#print(headline)


#Now if we want to acess the summary of the article
#summary=article.p.text
#print(summary)

'''
Now i we want to get a list of all the articles within
the html ,we need to use 'find_all' method, it returns
a list contain a given tag as arguement and we cann loop
thruogh the list and display the contents we want to display.

suppose i want to display the headline and summary, of all
the div with class as article:

'''
for article in soup.find_all('div',class_='article'):
    headline = article.a.text
    print(headline)
    
    summary=article.p.text
    print(summary)
    
    print()
    
