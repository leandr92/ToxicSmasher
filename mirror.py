# file: mirror.py
from datetime import datetime, timedelta
from telethon.sync import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl.types import PeerUser, PeerChat, PeerChannel
from telethon.tl.functions.messages import SendMessageRequest
import random

from config import (API_ID, API_HASH, SESSION_STRING, SOURCE_CHANNEL, TARGET_CHANNEL)

client = TelegramClient(StringSession(SESSION_STRING), API_ID, API_HASH)
print("connected")


# Обработчик новых сообщений
@client.on(events.NewMessage(chats=SOURCE_CHANNEL))
async def handler_new_message(event):

    phrases = [
        "Я не знаю, что делает вас глупым, но это действительно работает.",
        "Если бы у меня было такое лицо, как у вас, я бы подал в суд на своих родителей!",
        "Я знаю, вы родились глупым, но почему у вас рецидив?",
        "Я знаю, вы не так глупы, как выглядите. Такое невозможно!",
        "Как ты сюда попал? Неужели кто-то оставил клетку открытой?",
        "Я могу выгнать из вас обезьяну, но это будет очень дорого для вас стоить!",
        "Да вы просто шаблон для построения идиота.",
        "Вы являетесь живым доказательством того, что человек может жить без мозгов!",
        "Вы всегда так глупы, или сегодня особый случай?",
        "Вы все еще любите природу, несмотря на то, что она сделала с вами?",
        "Ваши родители когда-нибудь просили вас бежать из дома?",
        "Я видел людей, как ты, но тогда я должен был заплатить за билет!",
        "Продолжайте говорить, когда-нибудь вам все-таки удастся сказать что-нибудь умное!",
        "Почему ты здесь? Я думал, что зоопарк закрывается на ночь!",
        "Опять тюльку гонишь?",
        "Сделайте мне, чтобы вас было не слышно!",
        "Закройте рот с той стороны, дует",
        "Руки из жопы, только ломать умеешь, больше ничего",
        "С жиру бесишься",
        "Повторите, пожалуйста, еще раз. Я, как коллекционер тупых и идиотских высказываний, просто обязан это записать. Авторство указывать?",
        "Чтоб оно вам поперек горла встало, когда по-большому пойдете.",
        "Вот Вы человек и порядочный, и скромный, — а вот не умеете этого показать.",
        "Таким как Вы, надо ставить памятники! Надгробные.",
        "Да, я вижу, Вас постоянно преследуют умные мысли. Но Вы всегда оказываетесь быстрее!",
        "В Вашем присутствии совсем не вежливо выглядеть талантливым и умным.",
        "Да, Вы, я смотрю мастер спорта по традиционному русскому единоборству — борьбе с похмельным синдромом..",
        "Неужели, я похож на стоматолога? Нет? Тогда закройте, пожалуйста рот.",
        "Твоя подруга упала и разбила подбородок, но это не страшно, ведь у нее есть второй.",
        "Куда мне до вас? Придётся очень долго опускаться...",
        "Природа щедро обделила тебя всем.",
        "Не волнуйся, когда-нибудь ты скажешь что-нибуть смешное.",
        "А много ли у вас друзей среди бактерий?",
        "Вот сидит в человеке дерьмо, а он его гордо называет характером.",
        "Ты как фантик — красивый и шуршишь и уже ненужен…",
        "Ты такой… Ну как сказать… А впрочем ты и этого не поймёшь…",
        "Если бы ты попытался думать хотя бы своим костным мозгом, но и его к сожалению ты не развивал.",
        "Не волнуйся… придёт то самое время и ты скажешь что нибудь смешное.",
        "Вы постоянно напоминаете мне океан… Меня от вас так же тошнит…",
        "Сделайте вид, шоб я вас долго искал",
        "Шоб вы так жили, как мы вам рады",
        "Ты поц или да?"
    ]
    minutes10 = timedelta(minutes=10)
    try:
           if datetime.now() >= client.message_last_time + minutes10:

            phrase = random.choice(phrases)
            if event.message.from_id.user_id == 395989767:
                print(phrase)
            if event.message.from_id.user_id == 682060469:
                result = await client(SendMessageRequest(await client.get_entity(SOURCE_CHANNEL), phrase,
                                                         reply_to_msg_id=event.message.id))
                client.message_last_time = datetime.now()

    except Exception as e:
        print(e)

if __name__ == '__main__':
    client.start()
    client.message_last_time = datetime.now() - timedelta(minutes=10)
    client.run_until_disconnected()
