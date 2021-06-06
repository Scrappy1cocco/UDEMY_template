from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from loader import dp
from states import Form


@dp.message_handler(Command("form"))
async def enter_form(message: types.Message):
    await message.answer("Введите имя: ")
    await Form.s1.set()

@dp.message_handler(state=Form.s1)
async def name_s1(message: types.Message, state: FSMContext):
    name = message.text
    await state.update_data(data_name=name)
    await message.answer("Введите e-mail: ")
    await Form.next()

@dp.message_handler(state=Form.s2)
async def email_s2(message: types.Message, state: FSMContext):
    e_mail = message.text
    await state.update_data(data_email=e_mail)
    await message.answer("Введите телефон: ")
    await Form.next()

@dp.message_handler(state=Form.s3)
async def phone_s3(message: types.Message, state: FSMContext):
    data = await state.get_data()
    name = data.get("data_name")
    e_mail = data.get("data_email")
    phone = message.text
    await message.answer(f"Привет! Ты ввел следующие данные: \n\n"
                         f"Имя - {name} \n\n"
                         f"Email - {e_mail} \n\n"
                         f"Телефон - {phone}")
    await state.reset_state()