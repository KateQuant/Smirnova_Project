from Bio import SeqIO
import os

from qpa_final_project.keyboards.inline.callback_datas import gc_callback
from qpa_final_project.loader import dp, bot
import logging
from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher.storage import FSMContext
from qpa_final_project.data.script import get_prefix, fasta_creator
from qpa_final_project.keyboards.inline.plot_inline import plot_button
from qpa_final_project.utils_old.misc.plot_gc import gc_content_plot
from qpa_final_project.data.config import PATH_TO_DOCS_FROM_NCBI


@dp.message_handler(state='enter_accession')
async def show_accession_items(message: types.Message, state: FSMContext):
    accession = message.text
    # logging.info(f'{type(accession)}')
    prefix = get_prefix(accession)

    if prefix <= 2:
        path_to_doc = fasta_creator(accession)
        logging.info(f'{path_to_doc=}')

        await bot.send_document(chat_id=message.from_user.id, document=types.InputFile(path_to_doc),
                                reply_markup=plot_button(accession))

        # os.remove(path_to_doc)
        await state.reset_state()

    else:
        await message.answer(text="Incorrect accession number, try again")
        await state.reset_state()


@dp.message_handler(Command("accession"))
async def find_accession_number(message: Message, state: FSMContext):
    await message.answer('Enter the sequence accession number from the database NCBI nucleotide')
    await state.set_state('enter_accession')


@dp.callback_query_handler(gc_callback.filter())
async def send_gc_plot(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    accession = callback_data.get("accession")
    file_path = f"{PATH_TO_DOCS_FROM_NCBI}{accession}.fasta"
    logging.info(f"{accession=}")
    logging.info(f"{file_path=}")

    sequence_parse = SeqIO.read(file_path, "fasta")
    dna_sequence = str(sequence_parse.seq)
    dna_name = str(sequence_parse.description)

    name_save = call.from_user.full_name
    path_to_picture = gc_content_plot(dna_sequence, name_save)

    await bot.send_photo(chat_id=call.from_user.id, photo=types.InputFile(path_to_picture),
                         caption=f"GC-content plot for {dna_name}", reply_markup=None)

    os.remove(path_to_picture)
    os.remove(file_path)

