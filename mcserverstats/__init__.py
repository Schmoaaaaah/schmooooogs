from .mcserverstats import mcserverstatscog


def setup(bot):
    bot.add_cog(mcserverstatscog())
