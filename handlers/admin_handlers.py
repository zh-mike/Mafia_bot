from aiogram import types

from loader import dp, bot, db
from keyboards import start_default_keyboard, get_game_roles_keyboard, game_roles_callback
from states import RegistrationState


@dp.message_handler(commands=['start'])
async def start_func(message: types.message):
    await message.answer(text='Добро пожаловать в Мафию',
                         reply_markup=start_default_keyboard)


@dp.message_handler(text=["Создать новую игру"])
@dp.message_handler(commands=["newgame"])
async def answer_menu_command(message: types.Message):
    text = f"Настройка игры" \
           f"\n\nВсего игроков: 0"
    await message.answer(text=text,
                         reply_markup=get_game_roles_keyboard())


@dp.callback_query_handler(game_roles_callback.filter(action="mafia_plus"))
async def plus_mafia(call: types.CallbackQuery):
    user_count = int(call.data.split(":")[-4])
    sheriff_count = int(call.data.split(":")[-3])
    mafia_count = int(call.data.split(":")[-2])
    peaceful_count = int(call.data.split(":")[-1])
    if mafia_count != 5:
        mafia_count += 1
        user_count +=1
        text = f"Настройка игры" \
               f"\n\nВсего игроков: {user_count}"
        await bot.edit_message_text(text=text,
                                    chat_id=call.message.chat.id,
                                    message_id=call.message.message_id,
                                    reply_markup=get_game_roles_keyboard(mafia_count=mafia_count,
                                                                         user_count=user_count,
                                                                         sheriff_count=sheriff_count,
                                                                         peaceful_count=peaceful_count))


@dp.callback_query_handler(game_roles_callback.filter(action="mafia_minus"))
async def minus_mafia(call: types.CallbackQuery):
    user_count = int(call.data.split(":")[-4])
    sheriff_count = int(call.data.split(":")[-3])
    mafia_count = int(call.data.split(":")[-2])
    peaceful_count = int(call.data.split(":")[-1])
    if mafia_count != 0:
        mafia_count -= 1
        user_count -= 1
        text = f"Настройка игры" \
               f"\n\nВсего игроков: {user_count}"
        await bot.edit_message_text(text=text,
                                    chat_id=call.message.chat.id,
                                    message_id=call.message.message_id,
                                    reply_markup=get_game_roles_keyboard(mafia_count=mafia_count,
                                                                         user_count=user_count,
                                                                         sheriff_count=sheriff_count,
                                                                         peaceful_count=peaceful_count))


@dp.callback_query_handler(game_roles_callback.filter(action="peaceful_plus"))
async def plus_peaceful(call: types.CallbackQuery):
    user_count = int(call.data.split(":")[-4])
    sheriff_count = int(call.data.split(":")[-3])
    mafia_count = int(call.data.split(":")[-2])
    peaceful_count = int(call.data.split(":")[-1])
    if peaceful_count != 15:
        peaceful_count += 1
        user_count += 1
        text = f"Настройка игры" \
               f"\n\nВсего игроков: {user_count}"
        await bot.edit_message_text(text=text,
                                    chat_id=call.message.chat.id,
                                    message_id=call.message.message_id,
                                    reply_markup=get_game_roles_keyboard(mafia_count=mafia_count,
                                                                         user_count=user_count,
                                                                         sheriff_count=sheriff_count,
                                                                         peaceful_count=peaceful_count))


@dp.callback_query_handler(game_roles_callback.filter(action="peaceful_minus"))
async def minus_peaceful(call: types.CallbackQuery):
    user_count = int(call.data.split(":")[-4])
    sheriff_count = int(call.data.split(":")[-3])
    mafia_count = int(call.data.split(":")[-2])
    peaceful_count = int(call.data.split(":")[-1])
    if peaceful_count != 0:
        peaceful_count -= 1
        user_count -= 1
        text = f"Настройка игры" \
               f"\n\nВсего игроков: {user_count}"
        await bot.edit_message_text(text=text,
                                    chat_id=call.message.chat.id,
                                    message_id=call.message.message_id,
                                    reply_markup=get_game_roles_keyboard(mafia_count=mafia_count,
                                                                         user_count=user_count,
                                                                         sheriff_count=sheriff_count,
                                                                         peaceful_count=peaceful_count))


@dp.callback_query_handler(game_roles_callback.filter(action="sheriff_minus"))
async def minus_sheriff(call: types.CallbackQuery):
    user_count = int(call.data.split(":")[-4])
    sheriff_count = int(call.data.split(":")[-3])
    mafia_count = int(call.data.split(":")[-2])
    peaceful_count = int(call.data.split(":")[-1])
    if sheriff_count != 0:
        sheriff_count -= 1
        user_count -= 1
        text = f"Настройка игры" \
               f"\n\nВсего игроков: {user_count}"
        await bot.edit_message_text(text=text,
                                    chat_id=call.message.chat.id,
                                    message_id=call.message.message_id,
                                    reply_markup=get_game_roles_keyboard(mafia_count=mafia_count,
                                                                         user_count=user_count,
                                                                         peaceful_count=peaceful_count,
                                                                         sheriff_count=sheriff_count))


@dp.callback_query_handler(game_roles_callback.filter(action="sheriff_plus"))
async def plus_sheriff(call: types.CallbackQuery):
    user_count = int(call.data.split(":")[-4])
    sheriff_count = int(call.data.split(":")[-3])
    mafia_count = int(call.data.split(":")[-2])
    peaceful_count = int(call.data.split(":")[-1])
    if sheriff_count != 2:
        sheriff_count += 1
        user_count += 1
        text = f"Настройка игры" \
               f"\n\nВсего игроков: {user_count}"
        await bot.edit_message_text(text=text,
                                    chat_id=call.message.chat.id,
                                    message_id=call.message.message_id,
                                    reply_markup=get_game_roles_keyboard(mafia_count=mafia_count,
                                                                         user_count=user_count,
                                                                         peaceful_count=peaceful_count,
                                                                         sheriff_count=sheriff_count))


@dp.callback_query_handler(game_roles_callback.filter(action="create"))
async def create_game(call: types.CallbackQuery):
    sheriff_count = int(call.data.split(":")[-3])
    mafia_count = int(call.data.split(":")[-2])
    peaceful_count = int(call.data.split(":")[-1])
    roles_list = ""
    roles_list += "Мафия " * mafia_count
    roles_list += "Шериф " * sheriff_count
    roles_list += "Мирный " * peaceful_count
    id_table = db.add_game_table(roles_list=roles_list, chat_id=call.message.chat.id)
    text = f"Игра успешно создана.\nНомер стола {id_table}"
    await call.message.answer(text=text)
