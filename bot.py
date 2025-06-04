import aiohttp
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import asyncio

# Инициализация бота
BOT_TOKEN = "8092584045:AAH-laCoHhIz-msrxTW_QE58kIAtadsicmI"
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# URL API от Gradio
API_URL = "http://localhost:7860/api/predict"

# Обработчик команды /start
@dp.message(Command(commands=['start']))
async def start_cmd(message: types.Message):
    await message.reply("Привет! Отправь мне текст, и я определю его настроение (позитивное, негативное или нейтральное).")

# Обработчик текстовых сообщений
@dp.message()
async def analyze_text(message: types.Message):
    text = message.text
    try:
        async with aiohttp.ClientSession() as session:
            # Формируем запрос в формате, который ожидает Gradio API
            payload = {"data": [text]}
            async with session.post(API_URL, json=payload) as response:
                if response.status == 200:
                    result = await response.json()
                    # Извлекаем результат из структуры Gradio API
                    sentiment_result = result['data'][0]
                    await message.reply(sentiment_result)
                else:
                    await message.reply(f"Ошибка API: {response.status}")
    except Exception as e:
        await message.reply(f"Произошла ошибка: {str(e)}")

# Запуск бота
async def main():
    await dp.start_polling(bot, skip_updates=True)

if __name__ == '__main__':
    asyncio.run(main())