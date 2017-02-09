# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 15:18:19 2016

@author: paul delano
"""

'''
Pully

1.) v0.01 Setup search functionality
2.) v0.02 Have search return all links from front page unless other criteria is specified (author, date)
3.) v0.03 When specific link is returned, pull all text from link between <p></p>
4.) v0.1 Store Data in dataframe, send to SQL DB
'''

# v0.01
from bs4 import BeautifulSoup 
import urllib

admins = {'Paul':'Delano'}

# Pully Functionality 
def Pully():
    url = input('Where do you want to scrape from today?: ')
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, "lxml")

    title_tags = soup.findAll('a',{'class': 'title'})
    url_titles = [tag.text for tag in title_tags]

    if title_tags:
        print('Retrieving your links...')
        for url_title in url_titles:
            print(*url_title)

# Main       

def main():
    print('''
    Pully v0.01
    
    [1] Pully
    [2] Exit
    ''')
    
    action = input('Choose an option: ')
    
    if action == '1':
        Pully()
    elif action == '2':
        exit()
    else:
        print('select a number') 

# Login
login = input('Username: ')
passw = input('Password: ')

if login in admins:
    if admins[login] == passw:
        print('Welcome', login)
        while True: 
            main()
    else: 
        print('Invalid Password')
else:
    print('Invalid Username')