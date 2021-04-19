import asyncio
import discord
import random


class BotActivity:
    """Klasa BotActivity zajmuje się cyklicznym zmienianiem wyświetlanej aktywności bota."""

    def __init__(self, discord_client: discord.Client):
        self._discord_client = discord_client

    @staticmethod
    def _get_random_activity():
        activities = [
            "Bicie żony",
            "Instalowanie Debiana",
            "Dzwonienie do Marka Zuckerberga",
            "Popełnianie seppuku",
            "Programowanie w PHP",
            "Audiencja u Kornasia",
            "Rozważanie sensu życia"
        ]
        return random.choice(activities)

    async def task_loop(self):
        await self._discord_client.wait_until_ready()
        while not self._discord_client.is_closed():
            activity = BotActivity._get_random_activity()
            await self._discord_client.change_presence(activity=discord.Game(name=activity))
            await asyncio.sleep(600)
