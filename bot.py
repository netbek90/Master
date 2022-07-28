from simp_bot import Bot  # базовый класс бота из файла simple_bot
import telebot
import os
from vk_api import VkApi
from vk_api.longpoll import VkLongPoll, VkEventType  # использование VkLongPoll и VkEventType


#vk_session = VkApi(token=(os.getenv("ACCESS_TOKEN")))
#vk=vk_session.get_api()
bot_tele = telebot.TeleBot("5516394136:AAEsM0UuV8TZTEkiFR36vE1BPbgUT2L1LaM")
@bot_tele.message_handler(content_types=['text'])

#def get_name(user_id):
#    user=vk_session.method("users.get",{'user_id':user_id})
#    print(f"{user[0]['first_name']} {user[0]['last_name']}")

class LongPollBot(Bot):
    """
    Бот, прослушивающий в бесконечном цикле входящие сообщения и способный отвечать на некоторые из них
    Бот отвечает на строго заданные сообщения
    """

    # длительное подключение
    long_poll = None

    def __init__(self):
        """
        Иинициализация бота
        """
        super().__init__()
        self.long_poll = VkLongPoll(self.vk_session)

    def run_long_poll(self):
        """
        Запуск бота
        """
        for event in self.long_poll.listen():

            # если пришло новое сообщение - происходит проверка текста сообщения
            if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text and event.user_id=='152484379':
                # ответ отправляется в личные сообщения пользователя (если сообщение из личного чата)
                if event.from_user:
                    bot_tele.send_message(chat_id='813075355', text=event.text)

                # ответ отпрвляется в беседу (если сообщение было получено в общем чате)
                elif event.from_chat:
                    bot_tele.send_message(chat_id='813075355', text=event.text)

