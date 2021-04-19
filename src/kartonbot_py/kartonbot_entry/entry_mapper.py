from typing import List
from kartonbot_py.kartonbot_entry.entry_mapper_rules import mapper_rules
from kartonbot_py.kartonbot_entry.kartonbot_entry import KartonBotEntry


class EntryMapper:
    """EntryMapper łączy ze sobą teksty zasoby wygenerowane przez AdoptujKrysiaScraper i generuje z nich listę
     obiektów KartonBotEntry na podstawie reguł zapisanych w pliku entry_mapper_rules.py"""

    def __init__(self, krychu_images, widget_messages):
        self.krychu_images = krychu_images
        self.widget_messages = widget_messages

    def map_entries(self) -> List[KartonBotEntry]:
        kartonbot_entries = list()

        for rule in mapper_rules:
            entry = dict()
            entry["name"] = rule["img_group"]
            entry["images"] = self.krychu_images[rule["img_group"]]
            entry["messages"] = self.widget_messages[rule["msg_group"]]
            entry["applicable"] = rule["applicable"]
            kartonbot_entries.append(KartonBotEntry(**entry))

        return kartonbot_entries
