import os
import random
import discord
from config import config_get
from datetime import datetime
from kartonbot_py.bot_commands.embed_util import make_info_embed, make_embed, make_error_embed, make_karton_embed, make_success_embed
from kartonbot_py.kartonbot_entry.applicable_entry_finder import ApplicableEntryFinder

class AdminCommandResolver:
    """To samo co CommandResolver, ale dla komend administratora"""

    def __init__(self, userdb, kartonbot_entries):
        self.userdb = userdb
        self.kartonbot_entries = kartonbot_entries

    async def resolve_command(self, message):

        if message.content.strip() == '!kartonbot admin':

            embed = make_info_embed("Wysłałem listę komend administratora w wiadomości prywatnej.")
            await message.channel.send(embed=embed)

            embed = make_embed()
            embed.add_field(name="!kartonbot admin dumpdb", value="pobiera zrzut bazy danych użytkowników KartonBota")
            embed.add_field(name="!kartonbot admin dumpdb", value="pobiera zrzut bazy danych użytkowników KartonBota")
            embed.add_field(name="!kartonbot admin mock dd.mm.rrrr hh:ss", value="wywołuje losowego Sławka z puli dostępnych o podanej dacie i godzinie")
            embed.add_field(name="!kartonbot admin deop Nick", value="odbiera uprawnienia administratora użytkownikowi o danym nicku")
            embed.add_field(name="!kartonbot admin op Nick", value="nadaje uprawnienia administratora użytkownikowi o danym nicku (użytkownik musi wcześniej choć raz użyć KartonBota)")
            embed.add_field(name="!kartonbot admin mythicaldebian", value="wyświetla legendarnego mitycznego fioletowego Sławka")
            await message.channel.send(embed=embed)

        elif message.content.startswith("!kartonbot admin mock"):
            command_splitted = message.content.split(' ')
            if len(command_splitted) < 5:
                await message.channel.send(embed=make_error_embed("Podaj prawidłową datę i godzinie w formacie DD.MM.RRRR HH:SS."))
            try:
                date_str = command_splitted[3] + " " + command_splitted[4]
                date = datetime.strptime(date_str, "%d.%m.%Y %H:%M")
                applicable_entry = ApplicableEntryFinder(self.kartonbot_entries).get_mocked_applicable_entry(date)
                random_entry = random.choice(applicable_entry.messages).replace("\\n", "\n"), random.choice(applicable_entry.images)
                embed = make_karton_embed(*random_entry)
                await message.channel.send(embed=embed)
            except ValueError:
                await message.channel.send(embed=make_error_embed("Podaj prawidłową datę i godzinie w formacie DD.MM.RRRR HH:SS."))

        elif message.content.startswith("!kartonbot admin mythicaldebian"):
            special_entry = next(filter(lambda entry: entry.name == "special", self.kartonbot_entries))
            random_entry = random.choice(special_entry.messages), random.choice(special_entry.images)
            embed = make_karton_embed(*random_entry)
            await message.channel.send(embed=embed)

        elif message.content.startswith("!kartonbot admin dumpdb"):
            embed = make_info_embed("Wysłałem zrzut bazy danych we wiadomości prywatnej.")
            await message.channel.send(embed=embed)

            embed = make_embed()
            dumped_data = self.userdb.dump_db_to_str().split("\n")
            embed.add_field(name="Format", value=dumped_data[1], inline=False)
            for number, record in enumerate(dumped_data[2:]):
                embed.add_field(name=f"Rekord {number + 1}", value=record, inline=False)

            await message.author.send(embed=embed)

        elif message.content.startswith("!kartonbot admin op"):
            command_splitted = message.content.split(' ')
            if len(command_splitted) < 4:
                await message.channel.send(embed=make_error_embed("Podaj nick osoby, która ma zostać administratorem."))
            else:
                nick = " ".join(command_splitted[3:])
                if not self.userdb.contains_user(nick):
                    await message.channel.send(embed=make_error_embed("Użytkownik nie jest zarejestrowany w bazie KartonBota.\nPodaj nick osoby, która użyła Kartonbota chociaż raz."))
                elif self.userdb.is_admin(nick):
                    await message.channel.send(embed=make_error_embed("Ten użytkownik jest już administratorem."))
                else:
                    self.userdb.set_admin(nick, True)
                    await message.channel.send(embed=make_success_embed(f"Nadano uprawnienia administratora użytkownikowi {nick}."))

        elif message.content.startswith("!kartonbot admin deop"):
            command_splitted = message.content.split(' ')
            if len(command_splitted) < 4:
                await message.channel.send(embed=make_error_embed("Podaj nick osoby, której chcesz odebrać uprawnienia."))
            else:
                nick = " ".join(command_splitted[3:]).strip()
                force_op_users = config_get("KARTONBOT_ADMINS")

                if not self.userdb.contains_user(nick):
                    await message.channel.send(embed=make_error_embed("Użytkownik nie jest zarejestrowany w bazie KartonBota.\nPodaj nick osoby, która użyła Kartonbota chociaż raz."))
                elif not self.userdb.is_admin(nick):
                    await message.channel.send(embed=make_error_embed("Ten użytkownik nie jest administratorem."))
                elif force_op_users is not None and nick in force_op_users.split(":"):
                    await message.channel.send(embed=make_error_embed("Ten użytkownik ma ustawioną permamentną rangę administratora.\nPowstrzymaj się od takich niecnych działań w przyszłości, ładnie proszę. :)"))
                else:
                    self.userdb.set_admin(nick, False)
                    await message.channel.send(embed=make_success_embed(f"Odebrano uprawnienia administratora użytkownikowi {nick}."))

        else:
            embed = make_error_embed("Wygląda na to, że nie ma takiej komendy.\n"
                                     "Nie przejmuj się, każdy czasami popełnia jakieś błędy.\n"
                                     "Moim błędem było na przykład to, że się urodziłem.\n"
                                     "Sprawdź listę komend administratora wpisując !kartonbot admin")
            await message.channel.send(embed=embed)
