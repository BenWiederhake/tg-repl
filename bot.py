#!/usr/bin/env python3

import logging
import os
import secret  # See secret_template.py
import secrets
import importlib

# Written for telegram.__version__ >= 20.0a0
from telegram import Chat, ChatMember, ChatMemberUpdated, Update
from telegram.ext import (
    Application,
    CallbackContext,
    Handler,
    Updater,
)

logger = logging.getLogger(__name__)

BOT = None
IO_LIST = []

IN = 0
CTX = 1
OUT = 2
ERR = 3
CONSTANTS = dict(IN=0, CTX=1, OUT=2, ERR=3)


class AlwaysHandler(Handler):
    def check_update(self, update):
        return True


def limit(text):
    if len(text) < 4000:
        return text
    return f'{text[:4000]}… ({len(text)} bytes)'


async def generic_callback(update: Update, context: CallbackContext):
    if update.effective_user.id != secret.OWNER_ID:
        return

    n = len(IO_LIST)
    added_io_object = [update, context, None, None]
    IO_LIST.append(added_io_object)

    if update.message and update.message.text and not update.message.text.startswith('/'):
        eval_globals = dict(IO=IO_LIST, update=update, context=context, import_module=importlib.import_module, bot=BOT, **CONSTANTS)
        try:
            added_io_object[2] = eval(update.message.text, eval_globals)
        except BaseException as e:
            added_io_object[3] = e

    print(added_io_object)

    if added_io_object[2] is not None:
        await update.message.reply_text(limit(f'IO[{n}][OUT] = {added_io_object[2]}'))
    elif added_io_object[3] is not None:
        await update.message.reply_text(limit(f'IO[{n}][ERR] = {added_io_object[3]}'))
    else:
        await update.message.reply_text(limit(f'IO[{n}][IN] = {update}'))


def run():
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    logger.info("Alive")

    application = Application.builder().token(secret.TOKEN).build()
    global BOT
    BOT = application.bot

    application.add_handler(AlwaysHandler(generic_callback))

    logger.info("Begin idle loop")
    application.run_polling()


if __name__ == '__main__':
    run()
