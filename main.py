import os

from telegram import Bot, Update, ParseMode

from telegram.ext import Updater, CallbackContext, Filters
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler

from telegram.utils.request import Request

from debug.color import ColorsPrint
from brain.base_brain import user_check, send_operator_msg
from debug.debug import log_error
from config import TOKEN


# @user_check
@log_error
def do_start(update: Update, context: CallbackContext):
    """ Функция обработчик команды /start """

    print('\nUser: ', update.effective_user.username)
    print('ID: ', update.message.chat_id)

    update.message.reply_text(
        text=f"Привет, {update.message.chat.first_name} 👋\n"
             f"Я бот компании <b>{context.bot.get_me().first_name}</b>.\n\n"
             f"<em>Бот создан только для сотрудников компании WONDERWALL.</em>",
        parse_mode=ParseMode.HTML,
    )

    update.message.reply_text(
        text=f"Бот находится в разработке",
        parse_mode=ParseMode.HTML,
    )


# @user_check
@log_error
def do_echo(update: Update, context: CallbackContext):
    """ Функция обработчик входящих сообщений """
    send_operator_msg(context, 'TEst')

    update.message.reply_text(
        text=f"Бот находится в разработке",
        parse_mode=ParseMode.HTML,
    )


@log_error
def do_help(update: Update, context: CallbackContext):
    """ Функция обработчик команды /help """
    pass


@log_error
def main():
    req = Request(
        connect_timeout=0.5,
    )

    bot = Bot(
        request=req,
        token=TOKEN,
    )

    updater = Updater(
        bot=bot,
        use_context=True,
    )

    # Проверить что бот корректно подключился к Telegram API
    os.system('clear')
    print(ColorsPrint('Запускаем бота...', 'att').do_colored())
    print(f'\nСоединение с {bot.get_me().first_name} — ', ColorsPrint('OK', 'suc').do_colored())

    # Обработчики команд
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", do_start))
    dp.add_handler(CommandHandler("help", do_help))
    dp.add_handler(MessageHandler(Filters.text, do_echo))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
