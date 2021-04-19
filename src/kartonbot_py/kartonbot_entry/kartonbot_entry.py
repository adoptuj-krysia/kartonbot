from datetime import datetime
from typing import Callable, List


class KartonBotEntry:
    """KartonBotEntry jest najważniejszym modelem używanym w KartonBocie. Pojedyncze KartonBotEntry
    reprezentuje listę wiadomości Sławka, przypisaną do nich listę linków do zdjęć oraz funkcję, która określa,
    czy dany KartonBotEntry powinien być używany o podanej dacie i godzinie."""

    def __init__(self, name: str, messages: List[str], images: List[str], applicable: Callable[[datetime], bool]):
        self.name = name
        self.messages = messages
        self.images = images
        self.applicable = applicable
