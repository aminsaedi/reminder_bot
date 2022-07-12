import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

print("Starting App")
from reminders import get_reminder, add_reminder
import datetime

async def get_today(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
	today_tasks = get_reminder.by_day_of_week(None)
	for task in today_tasks:
		await update.message.reply_text(task)

async def add_task(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
	add_reminder.add_for_day(' '.join(update.message.text.split()[1:-1]), update.message.text.split()[-1])
	await update.message.reply_text("Task Added")


async def callback_minute(context: ContextTypes.DEFAULT_TYPE) -> None:
	await context.bot.send_message(chat_id='701578028', text="Hello Amin")

telegram_app = ApplicationBuilder().token(os.environ['TOKEN']).build()

telegram_app.add_handler(CommandHandler("today", get_today))
telegram_app.add_handler(CommandHandler("add", add_task))

job_queue = telegram_app.job_queue

time = datetime.time(hour=7)

job_minute = job_queue.run_daily(callback_minute,time, days=(0, 1, 2, 3, 4, 5, 6))


telegram_app.run_polling()

