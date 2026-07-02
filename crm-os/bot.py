import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "8963989397:AAFH0mhDyutpuId8Nd1bFuwkJWYu4DaptFg"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton(
            "📊 Открыть CRM",
            WebAppInfo(url="crm-os-production.up.railway.app")
        )]
    ])

    await update.message.reply_text("CRM готова", reply_markup=keyboard)


app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.run_polling()
