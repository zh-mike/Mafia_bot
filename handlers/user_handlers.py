from aiogram import types
from aiogram.dispatcher import FSMContext
from random import randint


from loader import dp, db
from keyboards import start_default_keyboard
from states import RegistrationState


@dp.message_handler(text=["Присоединиться к игре"])
async def in_game(message: types.message):
    await message.answer(text="Введите номер стола: ")
    await RegistrationState.wait_pin.set()


@dp.message_handler(state=RegistrationState.wait_pin)
async def game_search(message: types.message, state: FSMContext):
    data = db.search_table(id_table=message.text)
    if data is None:
        await message.answer(text="Стол не найден.\n"
                                  "Уточните номер стола у администратора")
    else:
        roles_list = data[-1].split()
        user_role = roles_list.pop(randint(0, len(roles_list)-1))
        str_roles = " ".join(roles_list)
        db.update_roles_user(id_table=message.text, roles_list=str_roles)
        await message.answer(text="Вы успешно зарегистрировалис!\n"
                                  f"Ваша роль {user_role}\n"
                                  "Ожидаем других игроков")
    await state.reset_state()
