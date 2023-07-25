import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def scrape_user_profile_with_show_more(user_id):
    url = f'https://scholar.google.com/citations?user={user_id}&hl=en'
    driver = webdriver.Chrome()  # Change this to Firefox() if using GeckoDriver.

    try:
        driver.get(url)
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID, 'gsc_rsb_st')))
        papers = []

        while True:
            paper_elements = driver.find_elements(By.CLASS_NAME,'gsc_a_tr')
            for paper in paper_elements:
                title = paper.find_element(By.CLASS_NAME,'gsc_a_at').text
                authors = paper.find_element(By.CLASS_NAME,'gsc_a_at').get_attribute('data-did-bidi')
                year = paper.find_element(By.CLASS_NAME,'gsc_a_h').text
                papers.append({'Title': title, 'Authors': authors, 'Year': year})

            try:
                show_more_button = driver.find_element(By.ID,'gsc_bpf_more')
                show_more_button.click()
                time.sleep(2)
            except Exception:
                break

        return papers
    finally:
        driver.quit()

def save_to_csv(data, filename):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        fieldnames = ['Title', 'Authors', 'Year']
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        for paper in data:
            writer.writerow(paper)

if __name__ == '__main__':
    user_id = 'uZmrRHAAAAAJ'  # Replace this with the Google Scholar User ID you want to scrape.
    filename = f'{user_id}.csv' 

    try:
        papers = scrape_user_profile_with_show_more(user_id)
        save_to_csv(papers, filename)
        print(f"Data scraped successfully and saved to {filename}")
    except Exception as e:
        print(f"An error occurred: {e}")
