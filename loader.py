from pathlib import Path

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from config import TOKEN
from db_api import Database

bot = Bot(token=TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
db_path = Path("db_api", "database", "mafia_database.db")
db = Database(db_path=db_path)

db.create_table_new_table()