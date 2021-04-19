import discord

def make_embed() -> discord.Embed:
    embed = discord.Embed(title="Kartonbot")
    embed.colour = 0x212121
    embed.set_footer(text="adoptuj-krysia.github.io")
    return embed

def make_success_embed(success_text):
    embed = make_embed()
    embed.colour = 0x00ff00
    embed.add_field(name="Sukces!", value=success_text)
    return embed

def make_karton_embed(text, image):
    embed = make_embed()
    embed.colour = 0xA0522D
    embed.set_image(url=image)
    embed.description = text
    return embed

def make_info_embed(info_text):
    embed = make_embed()
    embed.colour = 0x008080
    embed.add_field(name="Informacja", value=info_text, inline=False)
    return embed

def make_error_embed(error_text):
    embed = make_embed()
    embed.colour = 0xEE1111
    embed.add_field(name="Błąd", value=error_text)
    return embed