from aiogram import types
from aiogram.dispatcher import FSMContext
from random import randint

from loader import dp, db, bot
from keyboards import start_default_keyboard
from states import RegistrationState


@dp.message_handler(text=["Присоединиться к игре"])
async def in_game(message: types.message):
    await message.answer(text="Введите номер стола: ")
    await RegistrationState.wait_pin.set()


@dp.message_handler(state=RegistrationState.wait_pin)
async def game_search(message: types.message, state: FSMContext):
    data = db.search_table(id_table=message.text)
    if data is not None:
        roles_list = data[-2].split()
        admin_chat_id = data[-1]
    if data is None:
        await message.answer(text="Стол не найден.\n"
                                  "Уточните номер стола у администратора")
    elif roles_list == []:
        await message.answer(text="Стол заполнен.")
    else:
        user_role = roles_list.pop(randint(0, len(roles_list) - 1))
        str_roles = " ".join(roles_list)
        db.update_roles_user(id_table=message.text, roles_list=str_roles)
        await message.answer(text="Вы успешно зарегистрировались!\n"
                                  f"Ваша роль {user_role}\n"
                                  "Ожидаем других игроков")
        await bot.send_message(chat_id=admin_chat_id,
                               text=f"Игрок: {message.from_user.username} - {user_role}")
    await state.reset_state()
