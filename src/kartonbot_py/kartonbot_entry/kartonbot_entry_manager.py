import dill
from kartonbot_py.kartonbot_entry.adoptuj_krysia_scraper import AdoptujKrysiaScraper
from kartonbot_py.kartonbot_entry.entry_mapper import EntryMapper


class KartonBotEntryManager:
    """Zarządza obiektami dla obiektów klasy KartonBotEntry, między innymi zapisując na dysku cache
    dla wygenerowanych obiektów."""

    def __init__(self):
        try:
            self.kartonbot_entries = KartonBotEntryManager.load_mapped_entries_from_cache()
        except (IOError, dill.PicklingError):
            self.kartonbot_entries = KartonBotEntryManager.regenerate_mapped_entries()

    @staticmethod
    def regenerate_mapped_entries():
        img = AdoptujKrysiaScraper.scrape_krychu_images()
        texts = AdoptujKrysiaScraper.scrape_widget_texts()
        mapped = EntryMapper(img, texts).map_entries()
        with open("data/cache.p", "wb") as cache_file:
            dill.dump(mapped, cache_file)
        return mapped

    @staticmethod
    def load_mapped_entries_from_cache():
        with open("cache.p", "rb") as cache_file:
            return dill.load(cache_file)
