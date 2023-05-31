from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, CallbackQuery
from src.database.services.repos import UserRepo, InviteRepo
from src.keyboards.inline.inline_markup.users.start_menu import start_menu_kb
from src.states.states import RegisterSG

from src.keyboards.inline.inline_markup.users.register import register_start_cb, register_start_kb


async def register_start(call: CallbackQuery, state: FSMContext):
    await call.message.answer('Введіть ключ')
    await RegisterSG.invite_link.set()


async def register_finish(message: Message, user_db: UserRepo, invite_db: InviteRepo, state: FSMContext):

    check_link = await invite_db.get_invite_id(create_link=message.text)
    print(check_link)
    print(message.text)
    if check_link:
        await user_db.add(user_id=message.from_user.id,
                          full_name=message.from_user.full_name,
                          mention=message.from_user.get_mention()
                          )
        text = f'Вас зареєстровано!\n🏪\n Ви можете обрати товар або прочитати детальніше про цього бота'
        await message.answer(text, reply_markup=start_menu_kb())
    else:
        text = 'Ви ввели некоректний ключ-запрошення, спробуйте ще раз'
        await message.answer(text, reply_markup=register_start_kb())


def setup(dp: Dispatcher):
    dp.register_callback_query_handler(register_start, register_start_cb.filter(action='register'), state='*')
    dp.register_message_handler(register_finish, state=RegisterSG.invite_link)
