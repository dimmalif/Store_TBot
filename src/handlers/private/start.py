import re

from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import CommandStart
from aiogram.types import Message

from src.database.services.repos import UserRepo, InviteRepo
from src.keyboards.inline.inline_markup.users.start_menu import start_menu_kb
from src.keyboards.inline.inline_markup.users.register import register_start_kb

KEY_REGEX = re.compile(r'key-(\d+)')


async def start_cmd(message: Message, user_db: UserRepo):
    user = await user_db.get_user(message.from_user.id)
    if not user:
        text = 'Ви не зареєстровані.Для реєстрації перейдіть по посиланню-запрошенню або введіть код з запрошення'
        await message.answer(text, reply_markup=register_start_kb())
    else:
        text = f'🏪\n Ви можете обрати товар або прочитати детальніше про цього бота'
        await message.answer(text, reply_markup=start_menu_kb())


async def invite_start(message: Message, user_db: UserRepo,
                       invite_db: InviteRepo, deep_link: re.Match):

    invite_key = int(deep_link.groups()[-1])
    check_link = await invite_db.get_invite_id(create_link=invite_key)
    if check_link:
        await user_db.add(user_id=message.from_user.id,
                          full_name=message.from_user.full_name,
                          mention=message.from_user.get_mention()
                          )
        text = f'Вас зареєстровано!\n🏪\n Ви можете обрати товар або прочитати детальніше про цього бота'
        await message.answer(text, reply_markup=start_menu_kb())


def setup(dp: Dispatcher):
    dp.register_message_handler(invite_start, CommandStart(KEY_REGEX), state='*')
    dp.register_message_handler(start_cmd, CommandStart(), state='*')

