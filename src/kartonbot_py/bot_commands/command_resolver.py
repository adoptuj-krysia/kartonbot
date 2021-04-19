import os
import sys
import random
from config import config_get
from datetime import datetime
from metadata import kartonbot_metadata
from kartonbot_py.common.date_utils import date_to_str
from kartonbot_py.bot_commands.admin_command_resolver import AdminCommandResolver
from kartonbot_py.kartonbot_entry.applicable_entry_finder import ApplicableEntryFinder
from kartonbot_py.bot_commands.embed_util import make_info_embed, make_embed, make_error_embed, make_karton_embed, make_success_embed


class CommandResolver:
    """Klasa przetwarzająca wiadomości użytkownika na odpowiednie funkcje Kartonbota"""

    def __init__(self, userdb, kartonbot_entries, krychotron):
        self.userdb = userdb
        self.kartonbot_entries = kartonbot_entries
        self.krychotron = krychotron

    async def user_first_visit(self, message):
        self.userdb.register_user(message.author)
        # await message.author.send("ℹ️ Witaj, użytkowniku. Wygląda na to, że używasz KartonBota po raz pierwszy.")
        # await message.author.send("ℹ️ Możesz sprawdzić statystyki twojego konta KartonBot używając komendy **!kartonbot stats**.")
        # await message.author.send("ℹ️ Wpisz **!kartonbot help**, aby uzyskać szczegółową listę dostępnych komend.")
        force_op_users = config_get("KARTONBOT_ADMINS")
        if force_op_users is not None:
            if str(message.author) in force_op_users.split(":"):
                self.userdb.set_admin(str(message.author), True)

    async def user_recurring_visit(self, message):
        self.userdb.increment_usage_count(message.author)

    async def resolve_command(self, message):
        if message.content.startswith('!kartonbot piotrullo'):
            embed = make_karton_embed("Aaalee sieee naajebałem.", "https://bit.ly/3pBGZVr")
            await message.channel.send(embed=embed)

        elif message.content.startswith("!kartonbot krychotron"):
            if message.author.voice and message.author.voice.channel:
                channel = message.author.voice.channel
                command_splitted = message.content.split(' ')
                allowed_entries = [str(n) for n in range(1, 8)]

                if len(command_splitted) > 2:
                    if not command_splitted[2] in allowed_entries:
                        await message.channel.send(embed=make_error_embed("Krychotron nie obsługuje takiego dźwięku. Podaj liczbę z zakresu <1; 7>."))
                        return
                    else:
                        arg = command_splitted[2]
                else:
                    arg = "combined"

                if self.krychotron.has_pending_tasks():
                    embed = make_info_embed(f"Będziesz musiał zaczekać, aż moduł Krychotrona obsłuży żądanie.\nTwoje miejsce w kolejce: {self.krychotron.count_pending_tasks()}")
                    await message.channel.send(embed=embed)
                else:
                    await message.channel.send(embed=make_success_embed("Odpalam Krychotrona, miłej zabawy!"))
                self.krychotron.add_to_queue(channel, "assets/krychotron/krychotron_0_{}.ogg".format(arg))
            else:
                await message.channel.send(embed=make_error_embed("Musisz połączyć się z jakimś kanałem głosowym, aby móc używać Krychotrona."))

        elif message.content.startswith("!kartonbot info"):
            embed = make_embed()
            embed.add_field(name=f"KartonBot - wydanie {kartonbot_metadata['release_number']}", value="Przygotowane z sercem przez Adoptuj Krysia Entertainment", inline=False)
            embed.add_field(name="Strona projektu", value="https://adoptuj-krysia.github.io", inline=False)
            embed.add_field(name="Wersja interpretera Python", value=sys.version, inline=False)
            embed.add_field(name="Baza Adoptuj Krysia ostatni raz zaktualizowana", value=date_to_str(datetime.fromtimestamp(os.path.getmtime("data/cache.p"))), inline=False)
            await message.channel.send(embed=embed)

        elif message.content.startswith('!kartonbot help'):
            embed = make_embed()
            embed.add_field(name="!kartonbot", value="wyświetla losowe zdjęcie i tekst Kartona")
            embed.add_field(name="!kartonbot krychotron", value="odtwarza na kanale głosowym legendarny wywiad z Kartonem")
            embed.add_field(name="!kartonbot piotrullo", value="wyświetla pana Piotra pod wpływem napojów wyskokowych")
            embed.add_field(name="!kartonbot stats", value="wyświetla statystyki użytkownika, który użył komendy")
            embed.add_field(name="!kartonbot admin", value="wyświetla listę komend administratora KartonBot")
            embed.add_field(name="!kartonbot info", value="wyświetla informacje na temat uruchomionego skryptu bota")
            embed.add_field(name="!kartonbot help", value="wyświetla tę wiadomość pomocy")
            await message.channel.send(embed=embed)

        elif message.content.startswith("!kartonbot stats"):
            username = str(message.author)
            registration_date = self.userdb.get_registration_date(username)
            total_uses = self.userdb.get_total_uses(username)
            embed = make_embed()
            embed.add_field(name="Twoja data rejestracji", value=registration_date)
            embed.add_field(name="Użyłeś Kartonbota już", value=f"{total_uses} razy")
            await message.channel.send(embed=embed)

        elif message.content.startswith("!kartonbot admin"):
            if self.userdb.is_admin(message.author):
                await AdminCommandResolver(self.userdb, self.kartonbot_entries).resolve_command(message)
            else:
                embed = make_error_embed("Ooo, nie działa. Wygląda na to, że nie posiadasz uprawnień administratora KartonBot.\n"
                                         "Mark Zuckerberg już po ciebie leci, czekaj na helikopter.\n"
                                         "Pamiętaj, administrator KartonBot to nie to samo, co administrator serwera.")
                await message.channel.send(embed=embed)

        elif message.content.strip() == '!kartonbot':
            applicable_entry = ApplicableEntryFinder(self.kartonbot_entries).get_applicable_entry()
            random_entry = random.choice(applicable_entry.messages).replace("\\n", "\n"), random.choice(applicable_entry.images)
            embed = make_karton_embed(*random_entry)
            await message.channel.send(embed=embed)

        else:
            embed = make_error_embed("Wygląda na to, że nie ma takiej komendy.\n"
                                     "Nie przejmuj się, każdy czasami popełnia jakieś błędy.\n"
                                     "Moim błędem było na przykład to, że się urodziłem.\n"
                                     "Sprawdź listę komend administratora wpisując !kartonbot admin")
            await message.channel.send(embed=embed)
