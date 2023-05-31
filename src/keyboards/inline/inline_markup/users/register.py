from src.keyboards.inline.inline_markup.base import *

register_start_cb = CallbackData('rg', 'action')


def register_start_kb():
    def button_cb(action: str):
        return dict(callback_data=register_start_cb.new(action=action))

    inline_keyboard = [
        [InlineKeyboardButton(Buttons.unregistered.register, **button_cb('register'))]
    ]

    return InlineKeyboardMarkup(row_width=2, inline_keyboard=inline_keyboard)
