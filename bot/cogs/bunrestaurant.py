import time
import discord
import datetime
from bs4 import BeautifulSoup
from discord.ext import commands
from discord import app_commands

from bot import LOGGER, BOT_NAME_TAG_VER, color_code
from bot.utils.crawler import getText

class BunRestaurant(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.bun_restaurant = "https://www.kumoh.ac.kr/ko/restaurant04.do"

    @app_commands.command(name="bun")
    async def bun(self, interaction: discord.Interaction):
        """ 분식당 메뉴 """
        a = datetime.datetime.today().weekday()

        header = {'User-Agent': 'Mozilla/5.0(Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko'}
        result = getText(self.bun_restaurant, header)
        parse = BeautifulSoup(result, 'lxml')
        menus = parse.find("div", {"class": "menu-list-box"}).find("tbody").find_all("td")

        embed=discord.Embed(title="**오늘의 분식당 메뉴**", description=menus[a].getText(), color=color_code)
        # embed.set_footer(text=BOT_NAME_TAG_VER)
        return await interaction.response.send_message(embed=embed)

async def setup(bot):
    await bot.add_cog(BunRestaurant(bot))
    LOGGER.info('BunRestaurant loaded!')