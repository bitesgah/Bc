from discord.ext import commands, tasks
import requests, validators, datetime
import json
import pytz

localdatetime = pytz.timezone("Europe/Berlin")

def load_data():
  with open("jsons/twitter.json", "r") as f:
    return json.load(f)

def save_data(data):
  with open("jsons/twitter.json", "w") as f:
    json.dump(data, f, indent=2)

def nextApiKey():
  data = load_data()
  if data["currentAPIKey"] == "ApiKey1":
    data["currentAPIKey"] == "ApiKey2"
  else:
    data["currentAPIKey"] = "ApiKey1"
  save_data(data)

def newestTweet():
  nextApiKey()
  data = load_data()
    
  url = "https://twitter-data1.p.rapidapi.com/UserTweets/"

  querystring = {"id":"1384679325409103877","count":"1"}

  headers = {
    "x-rapidapi-key": data[data["currentAPIKey"]],
    "x-rapidapi-host": "twitter-data1.p.rapidapi.com"
  }

  response = requests.get(url, headers=headers, params=querystring).json()
  if "message" in response:
    return
  tweet_id = response["data"]["user"]["result"]["timeline"]["timeline"]["instructions"][2]["entries"][0]["entryId"].split("-")[1]
  
  return f"https://twitter.com/BerlinCityClub/status/{tweet_id}"
  
  


class twitternot(commands.Cog):
  
  def __init__(self, bot):
    self.bot = bot
    self.check.start()

  
  @tasks.loop(minutes=45)
  async def check(self):
    # Ausserhalb des Zeitfensters nicht prüfen um Aufrufe zu sparen
    hour_now = datetime.datetime.now(localdatetime).hour
    if hour_now < 11 or hour_now > 22:
        return

    with open("jsons/twitter.json", "r") as f:
      twitter = json.load(f)
      
    newest = newestTweet()
    print(newest)
    if validators.url(newest) and newest != twitter["newesttweet"]:
      twitter["newesttweet"] = newest
      channel = self.bot.get_channel(1120029010743791646)
      msg = await channel.send(f"<a:BC_Hype:807804225421049867> We just posted on Twitter. Let's check it out[:]({newest}) <:Xlogo:1160520008636575784>")
      await msg.add_reaction("<a:BC_Correct:807917418022305812>")

      with open("jsons/twitter.json", "w") as f:
        json.dump(twitter, f, indent=2)
          

async def setup(bot):
  await bot.add_cog(twitternot(bot))
