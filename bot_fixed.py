from telegram.ext import Application, CommandHandler, MessageHandler, CallbackQueryHandler, filters

from config import BOT_TOKEN


def main():
    app = Application.builder().token(BOT_TOKEN).build()
    print('CinemaCityHub Started')
    app.run_polling(drop_pending_updates=True)


if __name__ == '__main__':
    main()
