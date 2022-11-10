# Телефонный справочник

import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.utils import executor
import datetime

API_TOKEN = 'TOKEN'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

@dp.message_handler(commands=['start', 'menu'])
async def send_welcome(message: types.Message):
    await message.reply('Привет! Это твой телефонный справочник!\nВыбери необходимый пункт меню:\n/open - показать справочник\n/add - добавить запись\n/dell {номер строки} - удалить запись\n/export - экспорт данных\n/menu - вызов меню')

@dp.message_handler(commands=['open'])
async def print_dict(message: types.Message):
    with open('Book1.csv','r', encoding='utf-8') as f:
        dictionary = f.readlines()
    for line in dictionary:
        await message.reply(line.replace(';', '   ').replace('\n', ''))
      
class Add(StatesGroup):
    add_name= State()

@dp.message_handler(commands=['add'], state = None)
async def add_contact(message: types.Message):
    await Add.add_name.set()
    await message.reply('Заполните данные справочника через пробел:\nФамилия Имя Дата_рождения Место_работы Телефон')
    
@dp.message_handler(state=Add.add_name)
async def data(message: types.Message, state: FSMContext):
    data = message.text.split(' ')
    surname = data[0]
    name = data[1]
    date_birth = data[2]
    company = data[3]
    tel_number = data[4]

    with open('Book1.csv','r', encoding='utf-8') as f:
        dictionary = f.readlines()
    count = 0
    for line in dictionary:
        count=int(line[0])
    res = 0
    new_line = []
    id = str(count+1) 
    new_line = [id, surname, name, date_birth, company, tel_number]
    res = ';'.join(new_line)+'\n'
    dictionary.append(res)  
    
    with open('Book1.csv', 'w', encoding='utf-8') as file:
        for line in dictionary:
            file.writelines(line)
    await message.reply('Данные добавлены в справочник')

    await state.finish()

@dp.message_handler(commands=['dell'])
async def num_dell(message: types.Message):
    num = int(message.text.split('dell')[-1])
    
    with open('Book1.csv','r', encoding='utf-8') as f:
        dictionary = f.readlines()
    with open('Book1.csv', 'w', encoding='utf-8') as file:        
        for line in dictionary:
            id = int(line[0])
            if id != num:
                file.writelines(line)

    await message.reply('Строка удалена из справочника')

@dp.message_handler(commands=['export'])
async def exp_file(message: types.Message):
    file = open('Book1.csv','rb')
    await message.reply_document(file)

@dp.message_handler()
async def echo(message: types.Message):
   await message.answer(message.text)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)