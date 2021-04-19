from datetime import datetime
from typing import List
from kartonbot_py.kartonbot_entry.kartonbot_entry import KartonBotEntry


class ApplicableEntryFinder:
    """Klasa przyjmuje listę obiektow KartonBotEntry i na podstawie daty i godziny
     wyznacza odpowiedni rodzaj wiadomości do wysłania."""

    def __init__(self, kartonbot_entries: List[KartonBotEntry]):
        self.entry_collection = kartonbot_entries

    def get_applicable_entry(self) -> KartonBotEntry:
        for entry in self.entry_collection:
            if entry.applicable(datetime.now()) is True:
                return entry

    def get_mocked_applicable_entry(self, mocked_date) -> KartonBotEntry:
        for entry in self.entry_collection:
            if entry.applicable(mocked_date) is True:
                return entry
