from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp
from keyboards import start_default_keyboard
from states import RegistrationState


@dp.message_handler(text=["Присоединиться к игре"])
async def in_game(message: types.message):
    await message.answer(text="Введите номер стола: ")
    await RegistrationState.wait_pin.set()


@dp.message_handler(state=RegistrationState.wait_pin)
async def game_search(message: types.message, state: FSMContext):
    # запрос в бд на наличее стола
    if message.text == "1234":
        # забрать с базы присвоить роль игроку и отправить в бд остаток массива
        await message.answer(text="Вы успешно зарегистрировалис!\n"
                                  "Ожидаем других игроков")
    else:
        await message.answer(text="Стол не найден.\n"
                                  "Уточните код стола у администратора")
    await state.reset_state()
    # Здесь нужно достать сз бд список где pin = message.text
    # если из бд пришел Nane то сказать что такого пина нет и
    # вернуть на главный экран или попросить повторно ввести пин
    # если все ок и игра нашлась пишем что он зареган