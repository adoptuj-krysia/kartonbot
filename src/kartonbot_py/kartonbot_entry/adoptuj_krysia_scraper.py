import requests
from typing import Dict, List
from bs4 import BeautifulSoup


class AdoptujKrysiaScraper:
    """Klasa łączy się z repozytorium Git aplikacji Adoptuj Krysia i pobiera najnowsze teksty widżetów i
    linki do obrazków Sławka. Oba rodzaje zasobów są pobierane z najnowszego wydania stabilnego apki."""

    @staticmethod
    def scrape_krychu_images() -> Dict[str, List[str]]:
        scrapped_data = dict()
        response = requests.get("https://bit.ly/2Yg61x4").text
        soup = BeautifulSoup(response, "html.parser")
        for friend_link in soup.select("a[title^='friend_']"):
            image_category = friend_link["href"].split('/')[-1].split(".")[0].split("_")[1]
            absolute_link = "https://github.com/" + friend_link["href"] + "?raw=1"
            if scrapped_data.get(image_category, None) is None:
                scrapped_data[image_category] = list()
            scrapped_data[image_category].append(absolute_link)
        return scrapped_data

    @staticmethod
    def scrape_widget_texts() -> Dict[str, List[str]]:
        scrapped_data = dict()
        response = requests.get("https://bit.ly/2KS4GcK").text
        soup = BeautifulSoup(response, "xml")
        for string_array in soup.select("string-array"):
            msg_group = string_array["name"]
            scrapped_data[msg_group] = list()
            for msg_line in string_array.select("item"):
                scrapped_data[msg_group].append(msg_line.text)
        return scrapped_data
