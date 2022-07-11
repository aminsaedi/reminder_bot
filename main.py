import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

print("Starting App")
from reminders import get_reminder, add_reminder

async def get_today(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
	today_tasks = get_reminder.by_day_of_week(None)
	for task in today_tasks:
		await update.message.reply_text(task)

async def add_task(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
	add_reminder.add_for_day(' '.join(update.message.text.split()[1:-1]), update.message.text.split()[-1])
	await update.message.reply_text("Task Added")

app = ApplicationBuilder().token(os.environ['TOKEN']).build()

app.add_handler(CommandHandler("today", get_today))
app.add_handler(CommandHandler("add", add_task))

app.run_polling()
