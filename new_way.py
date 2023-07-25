import pandas as pd 
from bs4 import BeautifulSoup 
import requests, lxml 
 
 
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
 
        for index, article in enumerate(soup.select("#gsc_a_b .gsc_a_t"), start=1): 
            url = f'https://scholar.google.com{article.select_one(".gsc_a_at")["href"]}'
            page_html = requests.post(url,params=params, headers=headers, timeout=30)
            page_soup = BeautifulSoup(page_html.text,"lxml")
            title = page_soup.select_one(".gsc_oci_title_wrapper").text
            print(title)
        
            # all_articles.append({ 
            #     "title": article_title, 
             
            #     "authors": article_authors, 
            #     "publication": article_publication, 
            #     "year":article_year 
            # }) 
 
        if soup.select_one(".gsc_a_e"): 
            articles_is_present = False 
        else: 
            params["cstart"] += 100  
     
 
    # pd.DataFrame(data=all_articles).to_csv(f"google_scholar_{params['user']}_articles.csv", encoding="utf-8", index=False) 
 
 
bs4_scrape_articles()