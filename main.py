import pandas as pd 
from bs4 import BeautifulSoup 
import requests, lxml 
import csv
def bs4_scrape_articles():
    params = { 
            "user": "uZmrRHAAAAAJ", 
            "hl": "en",              
            "gl": "us",            
            "cstart": 0,                 
            "pagesize": "100" 
        } 
    
    headers = { 
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3538.102 Safari/537.36 Edge/18.19582", 
        } 
    
    all_articles = [] 
    
    articles_is_present = True 
    
    while articles_is_present: 
        html = requests.post("https://scholar.google.co.in/citations?user=uZmrRHAAAAAJ&hl=en", params=params, headers=headers, timeout=30) 
        soup = BeautifulSoup(html.text, "lxml") 
    
        for index, article in enumerate(soup.select("#gsc_a_b"), start=1):
            for index,arti in enumerate(soup.select('.gsc_a_tr'),start=1):
                if (arti.find('td','gsc_a_t')):
                    title = arti.find('td','gsc_a_t').find('a','gsc_a_at').text
                    authors = arti.find('td','gsc_a_t').find('div','gs_gray').text
                    if (arti.find('td','gsc_a_y').text > '0'):
                        date = arti.find('td','gsc_a_y').text
                    else:
                        date = '0'
                    
                all_articles.append({ 
                "title": title, 
                "authors": authors,  
                "year":date
                }) 
            
        if soup.select_one(".gsc_a_e"): 
            articles_is_present = False 
        else: 
            params["cstart"] += 100  
        
        pd.DataFrame(data=all_articles).to_csv(f"google_scholar.csv", index=False) 
def sorting():
    df = pd.read_csv('google_scholar.csv')
    cx = df.sort_values("year",ascending=False)
    pd.DataFrame(data=cx).to_csv(f"google_scholar_sort.csv", index=False)
bs4_scrape_articles()
sorting()