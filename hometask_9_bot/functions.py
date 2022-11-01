import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from log import *

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

def start(update, context):
    
    update.message.reply_text('Привет! Выбери необходимую команду')
    update.message.reply_text('/addit x y - сложение чисел\n/sub x y - вычитание чисел\n/mult x y - перемножение чисел\n/div x y - деление чисел')


def help(update, context):
    
    log (update, context)
    update.message.reply_text('Help!')


def echo(update, context):
    """Echo the user message."""
    update.message.reply_text(update.message.text)


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def addit (update, context):
    log (update, context)
    msg = update.message.text
    items = msg.split()
    x = float(items[1])
    y = float(items[2])
    update.message.reply_text(f'{x} + {y} = {round((x+y),2)}')

def sub (update, context):
    log (update, context)
    msg = update.message.text
    items = msg.split()
    x = float(items[1])
    y = float(items[2])
    update.message.reply_text(f'{x} - {y} = {round((x-y),2)}')

def mult (update, context):
    log (update, context)
    msg = update.message.text
    items = msg.split()
    x = float(items[1])
    y = float(items[2])
    update.message.reply_text(f'{x} * {y} = {round((x*y),2)}')

def div (update, context):
    log (update, context)
    msg = update.message.text
    items = msg.split()
    x = float(items[1])
    y = float(items[2])
    update.message.reply_text(f'{x} / {y} = {round((x/y),2)}')
