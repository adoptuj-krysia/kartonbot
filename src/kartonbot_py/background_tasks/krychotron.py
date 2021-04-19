import asyncio
import discord
from collections import deque


class Krychotron:
    """Klasa Krychotron zajmuje się kolejkowaniem odgłosów, które bot odgrywa na kanałach dźwiękowych."""

    def __init__(self, discord_client):
        self._queue = deque()
        self._discord_client = discord_client

    def add_to_queue(self, voice_channel, sound_path):
        self._queue.append((voice_channel, sound_path))

    def has_pending_tasks(self):
        return len(self._queue) > 0

    def count_pending_tasks(self):
        return len(self._queue)

    async def task_loop(self):
        await self._discord_client.wait_until_ready()
        while not self._discord_client.is_closed():
            if self.has_pending_tasks():
                channel, sound_path = self._queue[-1]
                vc = await channel.connect()
                vc.play(discord.FFmpegPCMAudio(source=sound_path))
                while vc.is_playing():
                    await asyncio.sleep(.1)
                self._queue.pop()
                await vc.disconnect()
            await asyncio.sleep(1)
