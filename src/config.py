import os
# W poniższym pliku można umieszczać dane konfiguracyjne Kartonbota.

# Uwaga! Kartonbot być konfigurowany także przez zmienne środowiskowe!
# Jeżeli w systemie jest obecna zmienna środowiskowa o nazwie takiej samej,
# jak nazwa jednego z kluczy poniżej, wartość w zmiennej środowiskowej bierze pierwszeństwo!
# Metoda konfiguracji przez zmienne środowiskowe jest przydatna np. podczas uruchamiania bota w kontenerze Dockera.

config = {

    # Token bota, niezbędny do zalogowania się do serwisu Discord.
    # Wygenerujesz go na stronie discord.com/developers
    "KARTONBOT_TOKEN":
    "ODAzOTQ1NDg4NDk1NTQyMjcz.YBFKlQ.E7TsPlkFjiNUiYrz65tGtYgYwS8",

    # Lista "permanentnych administratorów" Kartonbota.
    # Składa się z nazw i tagów użytkowników odzielanych dwukropkami.
    # Permanentny administrator otrzymuje uprawnienia administratora przy starcie bota i nie da się mu
    # ich w żaden sposób odebrać.
    "KARTONBOT_ADMINS":
    "Deru#1970"

}

# Nie modyfikować, funkcja odpowiedzialna za pobieranie danych konfiguracji
def config_get(entry_key):
    entry_key = entry_key.upper()
    if os.environ.get(entry_key) is not None:
        return os.environ[entry_key]
    else:
        return config[entry_key]