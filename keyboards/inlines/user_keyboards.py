from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inlines.callback_data import game_roles_callback

def get_game_roles_keyboard(mafia_count: int = 0, peaceful_count: int = 0,
                            sheriff_count: int = 0, user_count: int = 0) -> InlineKeyboardMarkup:
    game_roles_keyboard = InlineKeyboardMarkup()
    game_roles_keyboard.row(InlineKeyboardButton(text=f"Мирный: {peaceful_count}",
                                                 callback_data=game_roles_callback.new(
                                                     action="None",
                                                     user_count=f"{user_count}",
                                                     sheriff_count=f"{sheriff_count}",
                                                     mafia_count=f"{mafia_count}",
                                                     peaceful_count=f"{peaceful_count}"
                                                 )),
                            InlineKeyboardButton(text='-',
                                                 callback_data=game_roles_callback.new(
                                                     action="peaceful_minus",
                                                     user_count=f"{user_count}",
                                                     sheriff_count=f"{sheriff_count}",
                                                     mafia_count=f"{mafia_count}",
                                                     peaceful_count=f"{peaceful_count}"
                                                 )),
                            InlineKeyboardButton(text='+',
                                                 callback_data=game_roles_callback.new(
                                                     action="peaceful_plus",
                                                     user_count=f"{user_count}",
                                                     sheriff_count=f"{sheriff_count}",
                                                     mafia_count=f"{mafia_count}",
                                                     peaceful_count=f"{peaceful_count}"
                                                 )),
                            )

    game_roles_keyboard.row(InlineKeyboardButton(text=f"Мафия: {mafia_count}",
                                                  callback_data=game_roles_callback.new(
                                                      action="None",
                                                      user_count=f"{user_count}",
                                                      sheriff_count=f"{sheriff_count}",
                                                      mafia_count=f"{mafia_count}",
                                                      peaceful_count=f"{peaceful_count}"
                                                  )),
                            InlineKeyboardButton(text='-',
                                                  callback_data=game_roles_callback.new(
                                                      action="mafia_minus",
                                                      user_count=f"{user_count}",
                                                      sheriff_count=f"{sheriff_count}",
                                                      mafia_count=f"{mafia_count}",
                                                      peaceful_count=f"{peaceful_count}"
                                                  )),
                            InlineKeyboardButton(text='+',
                                                  callback_data=game_roles_callback.new(
                                                      action="mafia_plus",
                                                      user_count=f"{user_count}",
                                                      sheriff_count=f"{sheriff_count}",
                                                      mafia_count=f"{mafia_count}",
                                                      peaceful_count=f"{peaceful_count}"
                                                  )),
                             )
    game_roles_keyboard.row(InlineKeyboardButton(text=f"Шериф: {sheriff_count}",
                                                 callback_data=game_roles_callback.new(
                                                     action="None",
                                                     user_count=f"{user_count}",
                                                     sheriff_count=f"{sheriff_count}",
                                                     mafia_count=f"{mafia_count}",
                                                     peaceful_count=f"{peaceful_count}"
                                                 )),
                            InlineKeyboardButton(text='-',
                                                 callback_data=game_roles_callback.new(
                                                     action="sheriff_minus",
                                                     user_count=f"{user_count}",
                                                     sheriff_count=f"{sheriff_count}",
                                                     mafia_count=f"{mafia_count}",
                                                     peaceful_count=f"{peaceful_count}"
                                                 )),
                            InlineKeyboardButton(text='+',
                                                 callback_data=game_roles_callback.new(
                                                     action="sheriff_plus",
                                                     user_count=f"{user_count}",
                                                     sheriff_count=f"{sheriff_count}",
                                                     mafia_count=f"{mafia_count}",
                                                     peaceful_count=f"{peaceful_count}"
                                                 )),
                            )
    game_roles_keyboard.row(InlineKeyboardButton(text=f"Создать игру.",
                                                 callback_data=game_roles_callback.new(
                                                     action="create",
                                                     user_count=f"{user_count}",
                                                     sheriff_count=f"{sheriff_count}",
                                                     mafia_count=f"{mafia_count}",
                                                     peaceful_count=f"{peaceful_count}"
                                                 ))
                            )

    return game_roles_keyboard