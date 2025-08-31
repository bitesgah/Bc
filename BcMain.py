import os, discord, json, re
from discord.ext import commands

whiteListRolesLinks = []
whiteListCategorieIdsLinks = [
  1149392386267566121,
  1223272950124249088,
  1203516085199175700,
  1179914950873976985,
  912004828031508500,
  1180979426368954368,
  1120029010743791646 ,
  1029088139114983455,
  1190268754974736483,
  807994561799389196,
  1017573084879913101,
]

whiteListChannelIdsLinks = [
  1295135722008870995,
  1295137295132921907,
  1295137822629560341,
  1295137898349465621,
  1295138064523595857,
  1295138163517296684,
  1295138447379402883,
]

class MyDiscordBot(commands.Bot):
  
  def __init__(self, intents):
    super().__init__(command_prefix=".", activity=discord.Activity(type=discord.ActivityType.watching, name="BC* Discord"), intents=intents)

  
  async def on_ready(self):
    print("Bot is ready!")
    for f in os.listdir('./cogs'):
      if f.endswith('.py'):
        await bot.load_extension(f'cogs.{f[:-3]}')
    await bot.wait_until_ready()
    await self.tree.sync()

    guild = self.get_guild(608340567046225951)
    whiteListRolesLinks.extend([
      guild.get_role(961960101147725904), # BC* ⫣ CEO & Owner
      guild.get_role(709826426769244191), # BC* ⫣ DC Admin
      guild.get_role(1017812761406885971), # BC* ⫣ IT Staff
      guild.get_role(984539067628802120), # BC* ⫣ Designer
      guild.get_role(743025392897491005), # BC* ⫣ Mod
      guild.get_role(830416938919526400), # BC* ⫣ Test Mod
      guild.get_role(808077568418643978), # BC* ⫣ E-Sport BS Member
      guild.get_role(993824111820296262), # ✳️ ⫣ Supercell Content Creator
      guild.get_role(965322500215037962), # BC* ⫣ Content Creator
      guild.get_role(1147529643960832102), # BC* ⫣ Social Media Staff
      guild.get_role(1122596382096765028), # BC* ⫣ Academy Manager
      guild.get_role(1122596725979361290), # BC* ⫣ Academy Coach
      guild.get_role(1018858040621019167), # BC* Academy
      guild.get_role(1208109804799791156), # BC* ⫣ Gaming Analyst
      guild.get_role(1207381143146598471), # BC* ⫣ Gaming Manager
      guild.get_role(1207381965960122428), # BC* ⫣ Gaming Coach
      guild.get_role(1204477983377719426), # BC* ⫣ Gaming
      guild.get_role(1129167461095325776), # BC* Esport Team Captain
    ])




  # Member joint dem Server
  async def on_member_join(self, member):
    if member.guild.id == 608340567046225951:
      user = await bot.fetch_user(member.id)
      channel = await bot.fetch_channel(1400465540295950386) # welcome channel
      # embed bauen
      em=discord.Embed(title="Welcome to **BerlinCityClub***", description="Accept <a:BC_Arrow:807993129944481792> <#807639532740149258>\n\nTake <a:BC_Arrow:807993129944481792>  <#1019324582123020399>\n\nHave Fun on our DC Server <a:BC_TeddyLove:824405582899183666>", color=int("FF2412", 16))
      file = discord.File("welcome.png")
      em.set_image(url="attachment://welcome.png")
      em.set_footer(text=f"{member.guild.member_count}th Member\nwww.berlincityclub.de", icon_url=user.display_avatar.url)
      await channel.send(f"{user.mention}", embed=em, file=file)
    
    
  async def on_message(self, message: discord.Message):
    if message.author.bot or not message.guild:
      return    
    channel = message.channel
    member = message.guild.get_member(message.author.id)

    canPostLink = False
    if isinstance(member, discord.Member):
      for role in whiteListRolesLinks:
        if role in member.roles:
          canPostLink = True
          break

    if channel.category:
      if channel.category.id in whiteListCategorieIdsLinks:
        canPostLink = True

    if channel.id in whiteListChannelIdsLinks:
      canPostLink = True

    if not canPostLink:
      # Überprüfen ob Nachricht Link enthält
      pattern = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
      # Suche nach dem Muster im Text
      if re.search(pattern, message.content):
        await message.delete()
        await message.channel.send(f"You are not allowed to post Links {member.mention}!", delete_after=5)
        return


    # Wenn Message in #tiktok-gameplay gesendet wird:
    if isinstance(channel, discord.TextChannel):
      if channel.id == 1079531223287877672:
        if message.attachments:
          await message.add_reaction("<:BC_Vote_Yes:820273539122200636>")
          await message.add_reaction("<:BC_Vote_No:820273616754966539>")
          return

    
    # Counting Channel
    if isinstance(channel, discord.TextChannel):
      if channel.id == 1043177846136377384:
        messages = [message async for message in channel.history() if not message.author.bot]
        async def checkcountnumbers(correct, answer=None):
          if correct: 
            pass
            #await message.add_reaction("<a:BC_Correct:807917418022305812>")
          else:
            await message.delete()
            await channel.send(answer, delete_after=2)


        try:
          num = int(message.clean_content)
          if not int(messages[1].clean_content)+1 == num:
            return await checkcountnumbers(False, f"{member.mention} incorrect number!")
          if messages[1].author == message.author:
            return await checkcountnumbers(False, f"{member.mention} You can't send multiple numbers in a row!")
          return await checkcountnumbers(True)
        except:
          return await checkcountnumbers(False, f"{member.mention} incorrect input!")
     
        

intents = discord.Intents.all()
bot = MyDiscordBot(intents=intents)   
bot.remove_command('help')
with open("jsons/env.json", "r") as f:
  env = json.load(f)
bot.run(env['TOKEN'])

