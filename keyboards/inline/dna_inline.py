from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from qpa_final_project.keyboards.inline.callback_datas import coding_callback, noncoding_callback


def string_button(dna):
    button = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="Coding template",
                                 callback_data=coding_callback.new(dna=dna)),
        ],
        [
            InlineKeyboardButton(text="Noncoding template",
                                 callback_data=noncoding_callback.new(dna=dna)),
        ],
    ])
    return button

