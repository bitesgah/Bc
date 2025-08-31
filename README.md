# Discord Bot - BerlinCityClub

A comprehensive Discord bot for the BerlinCityClub server with multiple automated features and moderation tools.

## Features

### 🐦 **Twitter Notifications**
- Automatically checks for new tweets every 45 minutes (11 AM - 10 PM)
- Posts notifications with reactions when new content is detected
- Uses rotating API keys for reliability

### 📱 **TikTok Notifications** 
- Monitors for new TikTok videos every 30 minutes (11 AM - 2 PM)
- Sends automatic notifications to designated channels
- Includes custom emojis and reactions

### 🌐 **Daily Social Media Promotion**
- Automatically posts social media links at 9:00 PM daily
- Includes interactive Linktree button
- Custom embed with all social platforms

### 🔗 **Link Protection System**
- Advanced link filtering and moderation
- Role-based permissions for link posting
- Category and channel-specific whitelist system
- Automatic link deletion for unauthorized users

### 🔢 **Counting Channel Management**
- Validates sequential number counting
- Prevents same user from posting consecutive numbers
- Automatic error handling and user feedback
- Maintains counting integrity

### 👋 **Welcome System**
- Custom welcome messages for new members
- Dynamic member count display
- Embedded welcome image
- Personalized greetings with user mentions

### 🎮 **Gaming Content Reactions**
- Automatic voting reactions on gameplay content
- Community engagement features
- Channel-specific functionality

## Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/bitesgah/Bc.git
   cd Bc
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configuration**
   - Copy `jsons/env.json.example` to `jsons/env.json`
   - Copy `jsons/twitter.json.example` to `jsons/twitter.json`
   - Copy `jsons/notify.json.example` to `jsons/notify.json`
   - Fill in all placeholders with your actual values:
     - Discord Bot Token
     - RapidAPI Keys for Twitter and TikTok APIs
     - Discord Channel & Role IDs

4. **Start the bot**
   ```bash
   python BcMain.py
   ```

## Configuration Details

### env.json
```json
{
    "TOKEN": "YOUR_DISCORD_BOT_TOKEN_HERE"
}
```

### twitter.json
```json
{
  "ApiKey1": "YOUR_RAPIDAPI_KEY_1_HERE",
  "ApiKey2": "YOUR_RAPIDAPI_KEY_2_HERE",
  "currentAPIKey": "ApiKey1",
  "newesttweet": ""
}
```

### notify.json
```json
{
  "ttnotify": {
    "latestvideourl": ""
  },
  "notifyingchannel": "YOUR_DISCORD_CHANNEL_ID_HERE",
  "ttnotrole": "YOUR_DISCORD_ROLE_ID_HERE",
  "ApiKey1": "YOUR_RAPIDAPI_KEY_1_HERE",
  "ApiKey2": "YOUR_RAPIDAPI_KEY_2_HERE",
  "currentAPIKey": "ApiKey2"
}
```

## Bot Permissions Required

- Send Messages
- Manage Messages (for link deletion)
- Add Reactions
- Embed Links
- Read Message History
- Use External Emojis

## Technical Details

- **Language**: Python 3.10+
- **Framework**: discord.py
- **APIs Used**: 
  - Twitter Data API (RapidAPI)
  - TikTok Scraper API (RapidAPI)
- **Timezone**: Europe/Berlin
- **Architecture**: Cog-based modular system

## Important Notes

⚠️ **Security**: Never commit real API keys or tokens to the repository!
⚠️ **Setup**: All `.json` files in the `jsons/` folder must be configured before starting the bot.
⚠️ **Permissions**: Ensure the bot has proper permissions in your Discord server.

## License

This project belongs to and is maintained by **BerlinCityClub** organization.
Website: https://berlincityclub.de/

All rights reserved by BerlinCityClub.
