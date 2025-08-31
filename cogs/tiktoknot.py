from discord.ext import commands, tasks
import requests, json
import datetime, pytz

localdatetime = pytz.timezone("Europe/Berlin")

def load_data():
    with open("jsons/notify.json", "r") as f:
        return json.load(f)

def save_data(data):
    with open("jsons/notify.json", "w") as f:
        json.dump(data, f, indent=2)

def nextApiKey():
    data = load_data()
    if data["currentAPIKey"] == "ApiKey1":
        data["currentAPIKey"] = "ApiKey2"
    else:
        data["currentAPIKey"] = "ApiKey1"
    save_data(data)

def getNewestTiktok():
    data = load_data()
    url = "https://tiktok-scraper2.p.rapidapi.com/user/videos"

    querystring = {"sec_uid":"MS4wLjABAAAAXzDBV3aRUJf39QG-40SZSZ_cQRNO9Pq7G72k46vEd9IdNUAWfQCMd7PSbzqb31Qj","user_id":"7334131610214483000"}

    headers = {
        "x-rapidapi-key": data[data["currentAPIKey"]],
        "x-rapidapi-host": "tiktok-scraper2.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    nextApiKey()
    
    if response:
        response_data = response.json()
        if "posts" in response_data:
            newest_url = response_data["posts"][3]["link"]
            return newest_url
    print(response.json())
    return None


class ttnot(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.check.start()

    @tasks.loop(minutes=30)
    async def check(self):
        # Ausserhalb des Zeitfensters nicht prüfen um Aufrufe zu sparen
        hour_now = datetime.datetime.now(localdatetime).hour
        if hour_now < 11 or hour_now > 14:
            return
        
        notificationData = load_data()
        if "ttnotify" not in notificationData:
            return

        print(f"Checking TikTok")
        latestvideourl = getNewestTiktok()
        if latestvideourl is None:
            print("Failed to fetch the latest TikTok video.")
            return

        print(latestvideourl)
        if str(notificationData["ttnotify"]["latestvideourl"]) != latestvideourl:
            notificationData["ttnotify"]["latestvideourl"] = latestvideourl
            discord_channel_id = notificationData['notifyingchannel']
            discord_channel = self.bot.get_channel(int(discord_channel_id))
          
            msg = await discord_channel.send(
                f"<a:BC_Hype:807804225421049867> We just uploaded to TikTok. Let's check it out:\n{latestvideourl} <a:TikTok:1099399314104664175>"
            )
            await msg.add_reaction("<a:BC_Correct:807917418022305812>")

            save_data(notificationData)

async def setup(bot):
    await bot.add_cog(ttnot(bot))
