from discord import Embed
import requests
from requests.structures import CaseInsensitiveDict


class mcstat():
    def makequery(serveraddres):
        url = "https://api.mcsrvstat.us/2/"+serveraddres
        headers = CaseInsensitiveDict()
        headers["Accept"] = "application/json"
        resp = requests.get(url, headers=headers)
        query = resp.json()
        return query

    def makeembedofquery(query, servername, serveraddres):
        if(query["online"] == True):
            embed = Embed(title=servername)
            embed.set_thumbnail(url="https://api.mcsrvstat.us/icon/"+serveraddres)
            embed.add_field(name="Host", value=serveraddres, inline=True)
            embed.add_field(name="Online", value=query["online"], inline=True)
            embed.add_field(name="Version", value=query["version"], inline=True)
            #if ("plugins" in query):
            #    embed.add_field(name="Plugins", value=query["plugins"], inline=True)
            #if ("mods" in query):
            #    embed.add_field(name="Mods", value=query["mods"], inline=True)
            embed.add_field(name="motd", value=(query["motd"])["clean"], inline=True)
            playersonline = (query["players"])["online"]
            maxplayers = (query["players"])["max"]
            embed.add_field(name="players", value=(str(playersonline)+"/"+str(maxplayers)), inline=True)
            embed.set_footer(text="here you go!")
        else:
            embed = Embed(title=servername)
            embed.set_thumbnail(
                url="https://api.mcsrvstat.us/icon/"+serveraddres)
            embed.add_field(name="Host", value=serveraddres, inline=True)
            embed.add_field(name="Online", value=query["online"], inline=True)
        return embed

    def makeembedserver(name, addres):
        embed = Embed(title="Server")
        embed.add_field(name="Host", value=addres, inline=True)
        embed.add_field(name="Name", value=name, inline=True)
        embed.set_footer(text="here you go!")
        return embed
