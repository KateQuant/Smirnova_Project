from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from qpa_final_project.loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("List of comands: ", '\n'
            "/start - start dialog", '\n'
            "/help - get info", '\n'
            "/transcribe - transcribe your sequence from dna to rna", '\n'
            "/translate - translate your sequence from rna to protein", '\n'
            "/accession - retrieve FASTA file by sequence accession number from NCBI “nucleotide“ database and "
            "build the gc-contenet plot on basis of it file"
            )

    await message.answer("\n".join(text))
