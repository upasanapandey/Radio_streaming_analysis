# Function for accessing the Geo_location data of a particular Radio station
# Author: Upasana Pandey
import requests
from bs4 import BeautifulSoup
import os


def geo_location(url, directory):
    '''
    Function to capture geo location data for radio station
    '''
    # Making get request and storing the response in a variable
    webpage = requests.get(url)
    # Parsing the content of web page by html parser
    soup = BeautifulSoup(webpage.content, 'html.parser')
    # Finding all meta tags present, stored in a list format
    meta_tag = soup.findAll('meta')
    # Finding location of Radio station from list
    for tag in meta_tag:
        if 'name' in tag.attrs.keys() and tag.attrs['name'] in ['description', 'name']:
             test_str = tag.attrs['content']
              # print(test_str)
              sub_list = ['Listen to ', 'from ', 'live on Radio Garden', '-']
               for sub in sub_list:
                    test_str = test_str.replace(sub, '')
                print("Radio station & Location:" + test_str)
                location = geo_data(test_str.strip())
                with open(directory+test_str+".txt", 'w') as f:
                    f.write(location)
                f.close()


def geo_data(dest) -> str:
    URL = "https://geocode.search.hereapi.com/v1/geocode"
    # Acquire from developer.here.com
    api_key = 'iI7YcmpbXvwlCJ2_gb2HSz-Q6vdlRu1rSOpCTfM1BPQ'
    # Parameters for Geo_location API
    PARAMS = {'apikey': api_key, 'q': dest.replace(u'\xa0', u' ')}
    # sending get request and saving the response as response object
    r = requests.get(url=URL, params=PARAMS)
    data = str(r.json())
    print(data)
    return data
