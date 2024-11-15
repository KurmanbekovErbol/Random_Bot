import asyncio
import random
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters import CommandStart
from Random_token import token

bot = Bot(token=token)
dp = Dispatcher()

@dp.message(CommandStart())
async def Start(message: Message):
    await message.answer("Бот: Я загадал число от 1 до 3 угадайте")

Random = str(random.randint(1,3))

@dp.message(F.text == Random)
async def Win(message: Message):
    await message.answer("Правильно вы отгадали")
    await message.reply_photo(photo='https://media.makeameme.org/created/you-win-nothing-b744e1771f.jpg')


@dp.message(F.text != Random)
async def Lost(message: Message):
    await message.reply_photo(photo='https://media.makeameme.org/created/sorry-you-lose.jpg')
    
    

async def main():
    await dp.start_polling(bot)

asyncio.run(main())