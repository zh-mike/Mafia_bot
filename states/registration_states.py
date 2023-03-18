from aiogram.dispatcher.filters.state import State, StatesGroup

class RegistrationState(StatesGroup):
    wait_pin = State()
