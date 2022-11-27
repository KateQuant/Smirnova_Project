from qpa_final_project.keyboards.inline.callback_datas import coding_callback, noncoding_callback
from qpa_final_project.loader import dp, bot
from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher.storage import FSMContext
from qpa_final_project.keyboards.inline.dna_inline import string_button
from qpa_final_project.data.db_query import get_rna_string

import re


@dp.message_handler(state='enter_sequence')
async def transcribe_sequence(message: types.Message, state: FSMContext):

    dna = str(message.text).upper()
    dna_pattern = '^[ACTG]*$'

    if re.findall(dna_pattern, dna):
        await message.answer(text=f"{dna}", reply_markup=string_button(dna))
        await state.reset_state()
    else:
        await message.answer(text="Incorrect format. Please input correct sequence that contain only 'ATGC' letters")
        await state.reset_state()


@dp.message_handler(Command("transcribe"))
async def enter_sequence(message: Message, state: FSMContext):
    await message.answer("Enter sequence in format 'ATGC'")
    await state.set_state('enter_sequence')


@dp.callback_query_handler(coding_callback.filter())
async def coding_transcription(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    dna = callback_data.get("dna")
    transcript = get_rna_string(dna)
    await bot.send_message(chat_id=call.from_user.id, text=transcript, reply_markup=None)


@dp.callback_query_handler(noncoding_callback.filter())
async def noncoding_transcription(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    dna = callback_data.get("dna")
    transcript = dna.replace('T', 'U')
    await bot.send_message(chat_id=call.from_user.id, text=transcript, reply_markup=None)

