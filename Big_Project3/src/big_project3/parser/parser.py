import re

class Parser:
    async def fetch(self, session, url):
        async with session.get(url) as response:
            return await response.text()
    
    def extract_words(self, html):
        text=re.sub(r'<[^>]+>', ' ', html)
        words_list=re.findall(r'\b[a-z]{3,}\b', text.lower())
        return words_list