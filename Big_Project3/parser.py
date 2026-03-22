import requests, re

def fetch(url):
    r=requests.get(url)
    return r.text

def extract_words(html):
    html=re.sub(r'<[^>]+>', ' ', html)
    words_list=re.findall(r'\b[a-z]{3,}\b', html)
    return words_list

if __name__=='__main__':
    text=fetch("https://kinogo-5.online/filmy/23234-ljubov.html")
    text_extracted=extract_words(text)
    print(text_extracted)