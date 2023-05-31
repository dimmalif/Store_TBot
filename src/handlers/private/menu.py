import random

from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import CommandStart
from aiogram.types import Message, CallbackQuery
from aiogram.utils.deep_linking import get_start_link

from src.database.services.repos import UserRepo, InviteRepo
from src.keyboards.inline.inline_markup.users.start_menu import start_menu_kb, start_menu_cb
from src.keyboards.inline.inline_markup.users.register import register_start_kb


async def create_invite(call: CallbackQuery, invite_db: InviteRepo):
    invite_key = hash(random.randint(call.from_user.id - 1000, call.from_user.id + 1000))
    invite_link = await invite_db.get_invite_user_id(user_id=call.from_user.id)
    if invite_link:
        await invite_db.update(create_link=str(invite_key), user_id=call.from_user.id)
        print(invite_link.create_link)
        url = await get_start_link(f'key-{invite_link.create_link}')
        await call.message.answer(f'Ваше нове посилання-запрошення: {url}')
    else:
        await invite_db.add(create_link=str(invite_key), user_id=call.from_user.id)
        await call.message.answer(f'Ваше нове посилання-запрошення: https://t.me/TestStore_course_bot?start={invite_key}')


def setup(dp: Dispatcher):
    dp.register_callback_query_handler(create_invite, start_menu_cb.filter(action='invite'), state='*')
