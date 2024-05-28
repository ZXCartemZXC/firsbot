from aiogram import Bot, Dispatcher, types, executor
from config import TELEGRAM_TOKEN

API_TOKEN = "7356815664:AAGJoWVjd84AkJZKZo5F4KTH7UXRK1IN4sE"

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

async def set_commands(bot: Bot):
    commands = [
        types.BotCommand(command='/start', description='Команда для того, чтобы запустить бота'),
        types.BotCommand(command='/help', description='Команда для того, чтобы помочь'),
        types.BotCommand(command='/list', description='Команда для того, тобы узнать список '),
        types.BotCommand(command='/price', description='Команда для того, чтобы узнать цены'),
        types.BotCommand(command='/data', description='Команда для того, чтобы посмотреть рабочие дни'),


    ]
    await bot.set_my_commands(commands)

@dp.message_handler(commands = 'start')
async def start(message:types.Message):
    await message.answer('Привет, я твой первый эхо-бот!')

@dp.message_handler(commands = 'help')
async def help(message:types.Message):
    await message.answer('Я могу помочь тебе с ...')

@dp.message_handler(commands='list')
async def list(message:types.Message):
    await message.answer('Список услуг:')

@dp.message_handler(commands='price')
async def price(message:types.Message):
    await message.answer('Цены:')

@dp.message_handler(commands='data')
async def data(message: types.Message):
    await message.answer('Рабочие дни:')


@dp.message_handler()
async def echo(message:types.Message):
    await message.answer(message. text)
async def on_startup(dispatcher):
    await set_commands(dispatcher.bot)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates = True, on_startup=on_startup)

