# KartonBot
_KartonBot by Adoptuj Krysia Entertainment_

KartonBot jest botem do Discorda, który stanowi idealne uzupełnienie do aplikacji Adoptuj Krysia na Androida.
Podobnie jak aplikacja, bot wyświetla dostosowane do daty i godziny zdjęcia i różne ciekawe złote myśli naszego mentora.

## Jak zaprosić bota na serwer?
Niestety, na tę chwilę opcja zaproszenia bota jest wyłączona. Spowodowane jest to kłopotami z serwerem.
Jeżeli bardzo chcesz skorzystać z bota, możesz użyć instrukcji zawartych poniżej, aby stworzyć swoją własną instancję bota i wtedy zaprosić ją na swoj serwer.

## Jak używać bota?
Gdy już zaprosisz Kartona na swój serwer, użyj komendy **!kartonbot help**.
Wyświetli ona wszystkie ważne komendy, o których musisz wiedzieć.

## Jakich uprawnień wymaga bot?
- wysyłanie wiadomości tekstowych
- dołączanie linków do wiadomości tekstowych
- dołączanie plików do wiadomości tekstowych
- dołączanie do kanałów dźwiękowych
- rozmawianie na kanałach dźwiękowych

## Na jakiej licencji jest rozpowrzechniany bot?
Bot jest rozpowrzechniany na darmowej, otwartej licencji GNU GPL v3
https://www.gnu.org/licenses/gpl-3.0.html

## Jak stworzyć własną instancję bota?
Aktualnie, zespół Adoptuj Krysia wspiera dwie główne metody powołania bota do życia.
Możesz zainstalować go i uruchomić bezpośrednio na komputerze lub użyć Dockera, aby mieć pewność, że bot będzie działał poprawnie na każdym systemie operacyjnym.

### Sposób 1 - Jak uruchomić bota w kontenerze Dockera?
1. Zainstaluj i skonfiguruj **docker** oraz **docker-compose**, jeśli jeszcze tego nie zrobiłeś.
2. Sklonuj to repozytorium komendą ```git clone https://github.com/adoptuj-krysia/kartonbot```
3. Wygeneruj twój własny token bota na stronie https://discord.com/developers
4. Przejdź do katalogu z pobranym repozytorium używając polecenia ```cd kartonbot```
5. Edytuj plik **docker-compose.yml**. Znajduje się on w folderze, który właśnie otworzyłeś.
6. W pliku **docker-compose.yml** wklej wygenerowany token bota do zmiennej **KARTONBOT_TOKEN**.
7. W tym samym pliku umieść twoją nazwę użytkownika Discord wraz z tagiem, na przykład Username#1234. Nazwę użytkownika umieść w zmiennej **KARTONBOT_ADMINS**.
8. Uruchom kontener poleceniem ``docker-compose up``. Jeśli wpisałeś dobry token bota, kontener powinien się uruchomić, a bot powinien zacząć nasłuchiwać wiadomości użytkowników.
9. Zaproś bota na serwer. Pamiętaj, by nadać botowi wymagane uprawnienia. Link do zaproszenia bota możesz wygenerować na stronie https://discord.com/developers/

### Sposób 2 - Jak uruchomić bota bezpośrednio (bez konteneryzacji)

1. Będziesz potrzebował Pythona 3 z zainstalowanym menedżerem pakietów __pip__. Pobierz Pythona, jeżeli nie masz go jeszcze zainstalowanego.
2. Wygeneruj twój własny token bota na stronie https://discord.com/developers
3. Sklonuj to repozytorium poleceniem ```git clone https://github.com/adoptuj-krysia/kartonbot```
4. Zainstaluj wymagane biblioteki. Jeżeli znasz się na narzędziach Pythona, możesz użyć środowiska wirtualnego: ```python -m pip install -r requirements.txt```
5. W pliku `config.py` wklej token bota, który wygenerowałeś w punkcie drugim. Umieść również swoją nazwę użytkownika, aby stać się administratorem.
6. Uruchom bota  poleceniem ```python start.py```
