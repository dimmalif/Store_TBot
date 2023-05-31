from src.keyboards.inline.inline_markup.base import *

start_menu_cb = CallbackData('mn', 'action')


def start_menu_kb():
    def button_cb(action: str):
        return dict(callback_data=start_menu_cb.new(action=action))

    inline_keyboard = [
        [InlineKeyboardButton(Buttons.menu.choose_product, **button_cb('choose_product'))],
        [InlineKeyboardButton(Buttons.menu.invite, **button_cb('invite'))],
        [InlineKeyboardButton(Buttons.menu.help, **button_cb('help'))],
    ]

    return InlineKeyboardMarkup(row_width=2, inline_keyboard=inline_keyboard)
