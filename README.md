# Telegradroid
![image](https://hackatime-badge.hackclub.com/U0A3U5X0QUE/Telegradroid)

## Setup
This setup guide was made for Windows. Some steps may differ if you're using another OS

- Download the source code and extract it on your device
- Install Python from this [website](https://python.org) (download standalone installer). In installation setup check "Add Python to PATH"
- Download [PostgreSQL](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads) 18 or newer
- In installation setup program will ask you to set up password for the database user, you need it to connect the bot with database (After installation cancel the StackBuilder setup)
- Search for "sql shell" in windows start menu and launch it. Connect to the database (just keep hitting Enter until it asks you for a password) and execute the following queries:

```
create schema bot;
```

```
create table bot.users (
    user_id bigint not null unique primary key,
    first_name varchar,
    last_name varchar,
    username varchar,
    lang varchar not null,
    last_seen timestamp not null default now(),
    apps jsonb default '{}'
);
```
Create .env file in the root directory of the project and copy & paste following:
```
BOT_TOKEN=

DB_USER=postgres
DB_PASS=
DB_HOST=localhost
DB_NAME=postgres

OPEN_WEATHER_KEY=
CEREBRAS_AI_KEY=
```
- Type your database user password next to `DB_PASS`

### Getting bot token
- Search for [BotFather](https://t.me/BotFather) in Telegram
- Send /newbot command and follow the instructions
- After creating a bot, BotFather will give you a token. Copy and paste it next to `BOT_TOKEN` variable in `.env` file

### Getting API Keys
- Sign up in [this website](https://home.openweathermap.org/api_keys) and copy your API Key
- Do the same with [this website](https://www.cerebras.ai/)
- Fill the corresponding variables in `.env` file

### Installing required libraries and launching the bot
- Open the terminal (powershell or cmd) in project directory and execute the following commands:
```
pip install -r requirements.txt
```

```
python main.py
```

### Final steps
Go to your bot and enjoy :)

[Optional] You can also customize your bot in [BotFather](https://t.me/BotFather)
