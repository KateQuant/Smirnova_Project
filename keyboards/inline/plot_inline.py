from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from qpa_final_project.keyboards.inline.callback_datas import gc_callback


def plot_button(accession):
    button = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="GC-content distribution",
                                 callback_data=gc_callback.new(accession=accession)),
        ],
    ])
    return button
