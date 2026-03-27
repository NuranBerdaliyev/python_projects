from dataclasses import dataclass, field
from collections import defaultdict
from index.index import Indexer
@dataclass
class SearchEngine:
    index_dict: Indexer = field(default_factory=Indexer)

    def search_count(self, word: str):
        self.index_dict.get_count(word.lower())