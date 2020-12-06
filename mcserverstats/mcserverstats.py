from redbot.core import commands, checks, Config
from .mcstat import mcstat
from discord import Embed


class mcserverstatscog(commands.Cog):
    """My custom cog"""

    def __init__(self):
        self.config = Config.get_conf(self, identifier=1234567890)
        default_guild = {
            "servers" : []
        }
        self.config.register_guild(**default_guild)

    @checks.admin_or_permissions(manage_guild=True)
    @commands.command(name="addmcserver")
    async def addmcserver(self, ctx, name, addres):
        """This does stuff!"""
        # Your code will go here
        #servers = 
        #server = await self.config.guild(ctx.guild).servers() 
        #.set(name = [name,addres])
        #server = server + [name,addres]
        #servers[name] = [name, addres]
        guild_group = self.config.guild(ctx.guild)
        async with guild_group.servers() as servers:
            if(len(servers)==0):
                servers.append([name,addres])
                await ctx.send("Added Server:")
                await ctx.send(embed = mcstat.makeembedserver(name, addres))
            else:
                existing = False
                for i in range(0,len(servers)):
                    server = servers[i]
                    if(server[0]==name or server[1]==addres):
                        await ctx.send("There is already a Server with this addres or name!")
                        existing = True
                if(existing == False):
                    servers.append([name,addres])
                    await ctx.send("Added Server:")
                    await ctx.send(embed = mcstat.makeembedserver(name, addres))
        #await ctx.send("Value of "+name+" has been changed to: Name = "+name+" Addres = "+addres+".")

    @checks.admin_or_permissions(manage_guild=True)
    @commands.command(name="removemcserver")
    async def removemcserver(self, ctx, name):
        """This does stuff!"""
        # Your code will go here
        guild_group = self.config.guild(ctx.guild)
        async with guild_group.servers() as servers:
            if (len(servers) == 0):
                await ctx.send("No servers added yet")
            else:
                foundserver = False
                for i in range(0,len(servers)):
                    server = servers[i]
                    if(server[0]==name):
                        addres = server[1]
                        del servers[i]
                        await ctx.send("Removed Server:")
                        await ctx.send(embed = mcstat.makeembedserver(name, addres))
                        foundserver = True
                if(foundserver == False):
                    await ctx.send("No Server with this Name found!")
        #servers = await self.config.guild(ctx.guild).mc
        #servers.pop(name)

    @commands.command(name="mcserverstats", aliases=["mcss"])
    async def mcserverstats(self, ctx, servername):
        """This does stuff!"""
        # Your code will go here
        servers = await self.config.guild(ctx.guild).servers()
        if (len(servers) == 0):
            await ctx.send("Currently no Servers added")
        else:
            for i in range(0,len(servers)):
                server = servers[i]
                if(servername != "all"):
                    if(server[0]==servername):
                        await ctx.send(embed=mcstat.makeembedofquery(mcstat.makequery(server[1]), server[0], server[1]))
                else:
                    await ctx.send(embed=mcstat.makeembedofquery(mcstat.makequery(server[1]), server[0], server[1]))

    @commands.command(name="listmcserver", aliases=["lmcs"])
    async def listmcserver(self, ctx):
        """This does stuff!"""
        # Your code will go here
        servers = await self.config.guild(ctx.guild).servers()
        if len(servers) == 0:
            await ctx.send("No servers added yet")
        else:
            for i in range(0,len(servers)):
                server = servers[i]
                await ctx.send(embed = mcstat.makeembedserver(server[0],server[1]))
                #await ctx.send(mcstat.makeembedserver(server[0], server[1]))
