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
VIEW, START, ADD, REMOVE = range(4)

SHOW = '<просмотр телефонной книги>'
ADD_LIST = '<добавление записи в телефонную книгу>'


# функция обратного вызова точки входа в разговор
def start(update, _):
    reply_keyboard = [['<просмотр телефонной книги>','<добавление записи в телефонную книгу>']]
    markup_key = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard= True)
    update.message.reply_text(
      'Добро пожаловать в ToDoList.', reply_markup = markup_key, )
    if update.message.text == SHOW:
        return VIEW
    if update.message.text == ADD_LIST:
        return ADD


def view(update, _):
    update.message.reply_text('тест')
    user = update.message.from_user
    logger.info("Контакт %s: %s", user.first_name, update.message.text)
    contact_list = o.read_csv()
    update.message.reply_text(contact_list)
    update.message.reply_text('Что-то')
    return START


def add(update, context):
    pass
    


# def player_turn(update, context):
#     user = update.message.from_user
#     logger.info(
#         "Ход игрока %s: %f / %f", user.first_name, update.message.text)
#     turn_count =context.user_data.get('turn_count')
#     candy_count = context.user_data.get('candy_count')
#     if candy_count < turn_count:
#         turn_count = turn_count - (turn_count - candy_count)
#     player_turn = update.message.text
#     if player_turn.isdigit():
#         player_turn = int(player_turn)
#         if player_turn <= turn_count:
#                 candy_count -= player_turn
#                 if candy_count < 1:
#                     update.message.reply_text(
#                         f'Игрок проиграл') 
#                     return ConversationHandler.END 
#                 context.user_data['candy_count'] = candy_count
#                 update.message.reply_text(
#                         f'Вы ввели {player_turn} конфет. В куче осталось {candy_count}: ')
#                 update.message.reply_text(f'Внимание ходит бот...')
#                 context.user_data['turn_count']=turn_count
#                 summ = turn(candy_count, turn_count)
#                 context.bot.send_message(update.effective_chat.id,
#                             f'Максимально допустимое значение за ход - {summ}') 
#                 return COMPUTER_TURN
#         else:
#                 update.message.reply_text(
#                         f'Максимально допустимое значение за ход - {turn_count}')    
#     else:
#         update.message.reply_text(
#                         f'Нужно ввести число')

# def turn(candy_count, turn_count):
#     return candy_count+turn_count
        
# def computer_turn(update, context):
#     turn_count = context.user_data.get('turn_count')
#     candy_count = context.user_data.get('candy_count')
#     if candy_count < turn_count:
#         turn_count = turn_count - (turn_count - candy_count)
#     if candy_count > 1:
#         candy_count -= turn_count-1
#     else:
#         candy_count -= turn_count
#     if candy_count <1:
#         update.message.reply_text(
#                         f'Бот проиграл')
#         return ConversationHandler.END 
#     context.user_data['candy_count'] = candy_count
#     update.message.reply_text(
#             f'Бот походил на {turn_count-1} конфет. В куче осталось {candy_count}: ')
#     update.message.reply_text(
#             f'Ваш ход. Введите число в диапазоне от 1 до {turn_count}: ')
#     context.user_data['turn_count']=turn_count            
#     return PLAYER_TURN

    
    
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
    game_conversation_handler = ConversationHandler( # здесь строится логика разговора
        # точка входа в разговор
        entry_points=[CommandHandler('start', start)],
        # этапы разговора, каждый со своим списком обработчиков сообщений
        states={
            VIEW:[MessageHandler(Filters.text, view)],
            START: [CommandHandler('start', start)],
            ADD:[MessageHandler(Filters.text, add)],
            #COMPUTER_TURN: [MessageHandler(Filters.text, computer_turn)],
        },
        # точка выхода из разговора
        fallbacks=[CommandHandler('cancel', cancel)],
    )

    # Добавляем обработчик разговоров `conv_handler`
    dispatcher.add_handler(game_conversation_handler)

    # Запуск бота
    updater.start_polling()
    updater.idle()