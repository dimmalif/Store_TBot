from src.keyboards.inline.inline_markup.base import *

admin_cb = CallbackData('am', 'action')


def admin_kb():
    def button_cb(action: str):
        return dict(callback_data=admin_cb.new(action=action))

    inline_keyboard = [
        [InlineKeyboardButton(Buttons.admin_menu.add_product, **button_cb('add_product'))],
    ]

    return InlineKeyboardMarkup(row_width=2, inline_keyboard=inline_keyboard)
