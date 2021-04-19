import os
import discord, discord.errors
from config import config_get
from kartonbot_py.database.user_database import UserDatabase
from kartonbot_py.background_tasks.krychotron import Krychotron
from kartonbot_py.background_tasks.bot_activity import BotActivity
from kartonbot_py.bot_commands.command_resolver import CommandResolver
from kartonbot_py.kartonbot_entry.kartonbot_entry_manager import KartonBotEntryManager


if not os.path.isdir("data"):
    os.mkdir("data")


discord_bot_token = config_get("KARTONBOT_TOKEN")
force_op_users = config_get("KARTONBOT_ADMINS")


client = discord.Client()
kartonbot_entries = KartonBotEntryManager().kartonbot_entries
kartonbot_userdb = UserDatabase()
bot_activity = BotActivity(client)
krychotron = Krychotron(client)
command_resolver = CommandResolver(kartonbot_userdb, kartonbot_entries, krychotron)


@client.event
async def on_ready():
    print('Bot zalogował się do Discorda pod nickiem: {0.user}'.format(client))
    if force_op_users is not None:
        for user in force_op_users.split(":"):
            if kartonbot_userdb.contains_user(user):
                kartonbot_userdb.set_admin(user, True)


@client.event
async def on_message(message):
    if message.author == client.user or not message.content.startswith("!kartonbot"):
        return
    if not kartonbot_userdb.contains_user(message.author):
        await command_resolver.user_first_visit(message)
    await command_resolver.resolve_command(message)
    await command_resolver.user_recurring_visit(message)


client.loop.create_task(bot_activity.task_loop())
client.loop.create_task(krychotron.task_loop())

try:
    client.run(discord_bot_token)
except discord.errors.LoginFailure:
    print("Wystąpił błąd logowania.")
    print("Być może podano niewłaściwy token?")
    exit(1)