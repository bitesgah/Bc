# Discord Bot - BerlinCityClub

A Discord bot for the BerlinCityClub server with various social media integration features.

## Features

- **Twitter Notifications**: Automatic notifications for new tweets
- **TikTok Notifications**: Notifications for new TikTok videos  
- **Linktree Sharing**: Daily social media links at 9:00 PM

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
     - RapidAPI Keys
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
  "notifyingchannel": YOUR_DISCORD_CHANNEL_ID_HERE,
  "ttnotrole": YOUR_DISCORD_ROLE_ID_HERE,
  "ApiKey1": "YOUR_RAPIDAPI_KEY_1_HERE",
  "ApiKey2": "YOUR_RAPIDAPI_KEY_2_HERE",
  "currentAPIKey": "ApiKey2"
}
```

## Important Notes

⚠️ **Security**: Never commit real API keys or tokens to the repository!
⚠️ **Setup**: All `.json` files in the `jsons/` folder must be configured before starting the bot.

## License

This project belongs to and is maintained by **BerlinCityClub** organization.
Website: https://berlincityclub.de/

All rights reserved by BerlinCityClub.
