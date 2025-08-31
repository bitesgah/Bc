from discord.ext import commands, tasks
import datetime, discord, pytz


class ButtonView(discord.ui.View):
    def __init__(self):
      super().__init__() 
      button = discord.ui.Button(label='Linktree', style=discord.ButtonStyle.url, url='https://linktr.ee/berlincityclub')
      self.add_item(button)
 

class sendlinktree(commands.Cog):
  
  def __init__(self, bot):
    self.bot = bot
    self.send.start()

  @tasks.loop(hours=24)
  async def send(self):      
    channel = self.bot.get_channel(1024032410553303100)
    em=discord.Embed(title="Follow us on Social Media", description="BerlinCityClub\n<:Xlogo:1160520008636575784> <a:Instagram:809910247778025553> <a:TikTok:1099399314104664175> <a:Twitch:1098763633409921164> <a:YouTube:1098765710387322923>", color=int("FF2412", 16))
    em.set_footer(text="check out our links ⬇")
    await channel.send(embed=em, view=ButtonView())
    
  @send.before_loop
  async def before_send(self):
    await self.bot.wait_until_ready()
    # Warten bis es genau 21:00 Uhr ist
    berlin_tz = pytz.timezone("Europe/Berlin")
    now = datetime.datetime.now(berlin_tz)
    
    # Berechne die nächste 21:00 Uhr Zeit
    target_time = now.replace(hour=21, minute=0, second=0, microsecond=0)
    if now >= target_time:
      # Wenn es schon nach 21:00 ist heute, dann nächster Tag
      target_time += datetime.timedelta(days=1)
    
    # Warten bis zur Zielzeit
    await discord.utils.sleep_until(target_time)


async def setup(bot):
  await bot.add_cog(sendlinktree(bot))