from aiogram import Dispatcher

from src.handlers.private import start, register, menu


def setup(dp: Dispatcher):
    start.setup(dp)
    register.setup(dp)
    menu.setup(dp)


