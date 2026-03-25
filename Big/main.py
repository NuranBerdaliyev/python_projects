from parser.parser import Parser
from index.index import Indexer
from search.search import SearchEngine

import aiohttp, asyncio

urls = [
    "https://jamesclear.com/creative-thinking",
    "https://jamesclear.com/stay-on-the-bus",
    "https://jamesclear.com/one-sentence-habits"
]
class Main:
    i=Indexer()
    p=Parser()

    async def __fetching(self, urls):
        async with aiohttp.ClientSession() as session:
            fetch_list=[self.p.fetch(session, url) for url in urls]
            coroutines_result=await asyncio.gather(*fetch_list)
            return [self.p.extract_words(html) for html in coroutines_result]
        
    async def add_words(self, urls):
        fetched_words=await self.__fetching(urls)
        
        for list_f in fetched_words:
            self.i.add_words(list_f)
        
        return self.i
        






        
        

