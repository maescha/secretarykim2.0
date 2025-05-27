## Secretary Kim 2.0

Revamping old Discord bot but this time with python
original: https://github.com/maescha/secretary-kim

## When Replicating

1. run `pip install -r requirements.txt`
   > or `[py/python3] -m pip install -U discord.py` and `py -m pip install requests` and `py -m pip install python-dotenv`
2. Create a .env filE and save a new `DISCORDTOKEN` variable with the reset token key from https://discord.com/developers/applications/[...]/bot or the **bot tab**
   - should be formatted like this:
     `DISCORDTOKEN=123456789456`
     > **TOKEN WAS RESET 5/27/2025**

## How to Run

type in terminal `py bot.py`

- if above does not work, then use `python3 bot.py`

You will know that you are successfully logged into your Discord server as the bot, if you see the following message in your terminal:

`Logged on as Secretary Kim 2.0#3142!`

## Todo features (optional in future)

- use tvmaze api to show web/streaming schedule of tv shows
  https://www.tvmaze.com/api
