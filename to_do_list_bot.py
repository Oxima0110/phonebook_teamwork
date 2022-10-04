import logging
import operations as o
from operations import contact_list
from config import TOKEN
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
)
# Включим ведение журнала
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

# Определяем константы этапов разговора
START, MENU, EDIT, ADD, DELETE, VIEW, SEARCH = range(7)


# функция обратного вызова точки входа в разговор
def start(update, _):
    reply_keyboard = [['VIEW', 'ADD', 'DELETE', 'EDIT', 'SEARCH']]
    markup_key = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    update.message.reply_text(
        'Добро пожаловать в ToDoList.', reply_markup=markup_key)
    return MENU

def menu(update, _):
    if update.message.text == 'VIEW':
        return VIEW
    if update.message.text == 'ADD':
        update.message.replay_text("Введите задачу: ")
        return ADD
    if update.message.text == 'DELETE':
        update.message.replay_text('Какую задачу хотите удалить?: ')
        return DELETE
    if update.message.text == 'EDIT':
        update.message.replay_text("Какую задачу хотите редактировать?: ")
        return EDIT
    if update.message.text == 'SEARCH':
        update.message.replay_text("Поисковая строка: ")
        return SEARCH


def view(update, _):
    user = update.message.from_user
    logger.info("Контакт %s: %s", user.first_name, update.message.text)
    update.message.reply_text('Что-то')
    # contact_list = o.read_csv()
    # update.message.reply_text(contact_list)
    update.message.reply_text('Что-то')
    #return START


def add(update, context):
    task = update.message.text
    o.add_task(task)


def search(update, _):
    searchstring = update.message.text
    contacts = o.read_csv()
    searched_contacts = o.search_contact(searchstring, contacts)
    update.message.reply_text(searched_contacts)


def delete(update, context):
    searchstring = update.message.text
    searched_contacts = o.search_contact(searchstring)
    # o.select_contact(choice, searched_contacts)
    # o.delete_contact(contact_list[contact])


def cancel(update, _):
    # определяем пользователя
    user = update.message.from_user
    # Пишем в журнал о том, что пользователь не разговорчивый
    logger.info("Пользователь %s отменил разговор.", user.first_name)
    # Отвечаем на отказ поговорить
    update.message.reply_text(
        'Мое дело предложить - Ваше отказаться'
        ' Будет скучно - пиши.',
    )
    return ConversationHandler.END


if __name__ == '__main__':
    # Создаем Updater и передаем ему токен вашего бота.
    updater = Updater(TOKEN)
    # получаем диспетчера для регистрации обработчиков
    dispatcher = updater.dispatcher

    # Определяем обработчик разговоров `ConversationHandler`
    # с состояниями GENDER, PHOTO, LOCATION и BIO
    game_conversation_handler = ConversationHandler(  # здесь строится логика разговора
        # точка входа в разговор
        entry_points=[CommandHandler('start', start)],
        # этапы разговора, каждый со своим списком обработчиков сообщений
        states={
            VIEW: [MessageHandler(Filters.text, view)],
            START: [CommandHandler('start', start)],
            ADD: [MessageHandler(Filters.text, add)],
            DELETE: [MessageHandler(Filters.text, delete)],
            #EDIT: [MessageHandler(Filters.text, edit)],
            SEARCH: [MessageHandler(Filters.text, search)],
            MENU: [MessageHandler(Filters.text, menu)],

        },
        # точка выхода из разговора
        fallbacks=[CommandHandler('cancel', cancel)],
    )

    # Добавляем обработчик разговоров `conv_handler`
    dispatcher.add_handler(game_conversation_handler)

    # Запуск бота
    updater.start_polling()
    updater.idle()
