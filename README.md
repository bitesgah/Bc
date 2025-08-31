# Discord Bot - BerlinCityClub

Ein Discord Bot für den BerlinCityClub Server mit verschiedenen Funktionen.

## Features

- **Twitter Notifications**: Automatische Benachrichtigungen bei neuen Tweets
- **TikTok Notifications**: Benachrichtigungen bei neuen TikTok Videos  
- **Linktree Sharing**: Tägliche Social Media Links um 21:00 Uhr

## Setup

1. **Repository klonen**
   ```bash
   git clone <repository-url>
   cd Bc
   ```

2. **Dependencies installieren**
   ```bash
   pip install -r requirements.txt
   ```

3. **Konfiguration**
   - Kopiere `jsons/env.json.example` zu `jsons/env.json`
   - Kopiere `jsons/twitter.json.example` zu `jsons/twitter.json`
   - Kopiere `jsons/notify.json.example` zu `jsons/notify.json`
   - Fülle alle Platzhalter mit deinen echten Werten aus:
     - Discord Bot Token
     - RapidAPI Keys
     - Discord Channel & Role IDs

4. **Bot starten**
   ```bash
   python BcMain.py
   ```

## Konfiguration Details

### env.json
```json
{
    "TOKEN": "Dein Discord Bot Token"
}
```

### twitter.json
```json
{
  "ApiKey1": "Dein RapidAPI Key 1",
  "ApiKey2": "Dein RapidAPI Key 2",
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
  "notifyingchannel": DEINE_CHANNEL_ID,
  "ttnotrole": DEINE_ROLE_ID,
  "ApiKey1": "Dein RapidAPI Key 1",
  "ApiKey2": "Dein RapidAPI Key 2",
  "currentAPIKey": "ApiKey2"
}
```

## Wichtige Hinweise

⚠️ **Sicherheit**: Niemals echte API Keys oder Tokens in das Repository committen!
⚠️ **Setup**: Alle `.json` Dateien im `jsons/` Ordner müssen vor dem Start konfiguriert werden.

## Lizenz

[Füge hier deine gewünschte Lizenz ein]
