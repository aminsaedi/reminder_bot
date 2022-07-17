import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from reminders import get_reminder, add_reminder, clear_reminders
import datetime
import pytz

chat_id = None

with open('chat_id', 'r') as file:
    chat_id = str(file.read())

async def get_today(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    today_tasks = get_reminder.by_day_of_week(None)
    for task in today_tasks:
        await update.message.reply_text(task)


async def add_task(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    add_reminder.add_for_day(' '.join(update.message.text.split()[1:-1]), update.message.text.split()[-1])
    await update.message.reply_text("Task Added")

async def callback_minute(context: ContextTypes.DEFAULT_TYPE) -> None:
    today_tasks = get_reminder.by_day_of_week(None)
    for task in today_tasks:
        await context.bot.send_message(chat_id=chat_id, text="Good morning :)")
        await context.bot.send_message(chat_id=chat_id, text=task)


async def clear_tasks(update, context):
    clear_reminders.clear()
    await update.message.reply_text("Tasks cleared")


async def handle_start(update, context):
    with open('chat_id', 'w+') as file:
        file.write(str(update.message.chat_id))
    await update.message.reply_text("Welcome to Reminder bot")


telegram_app = ApplicationBuilder().token(os.environ['TOKEN']).build()

telegram_app.add_handler(CommandHandler("start", handle_start))
telegram_app.add_handler(CommandHandler("today", get_today))
telegram_app.add_handler(CommandHandler("add", add_task))
telegram_app.add_handler(CommandHandler("clear", clear_tasks))

job_queue = telegram_app.job_queue

time = datetime.time(hour=6, minute=0, tzinfo=pytz.timezone('US/Eastern'))
job_minute = job_queue.run_daily(callback_minute, time, days=(0, 1, 2, 3, 4, 5, 6))

telegram_app.run_polling()

