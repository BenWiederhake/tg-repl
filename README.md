# tg-repl

> A simple REPL for your Telegram fiddling needs

## Table of Contents

- [Install](#install)
- [Usage](#usage)
- [Contribute](#contribute)

## Install

Just do `pip3 install -r requirements.txt` .

Then, copy `secret_template.py` to `secret.py`, and fill in your details. You get the token from ["The Botfather"](https://t.me/BotFather). If you don't yet know what your own ID is, you can either fiddle with the bot, or use [any of the plenty ID bots](https://t.me/get_my_user_id_bot).

### virtualenv

Alternatively, I recommend doing this inside a virtualenv, because there 13→20 transition in python-telegram-bot is kinda weird, and you may want to keep using v13 with some of your other projects. In that case:

```
$ python3 -m venv .virtualenv
$ . .virtualenv/bin/activate # The initial dot is the "source" command in most shells.
$ pip3 install -r requirements.txt # This now calls .virtualenv/bin/pip3
```

## Usage

`./bot.py` – that's it! Now you can talk to your bot, and see what it does. Some starting points:

- `2+2`
- `/start`
- `globals().keys()`
- `1/0`
- `IO[0][IN]`
- `update.message.from_user`

## Contribute

Feel free to dive in! [Open an issue](https://github.com/BenWiederhake/tg-repl/issues/new) or submit PRs.
