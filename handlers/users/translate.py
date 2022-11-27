from qpa_final_project.loader import dp
from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import Message
from aiogram.dispatcher.storage import FSMContext
from qpa_final_project.data.script import convert_rna_to_protein


@dp.message_handler(state='enter_rna')
async def transcribe_sequence(message: types.Message, state: FSMContext):
    translation = convert_rna_to_protein(message.text)
    await message.answer(text=f"{translation}")
    await state.reset_state()


@dp.message_handler(Command("translate"))
async def enter_sequence(message: Message, state: FSMContext):
    await message.answer("Enter sequence in format 'AUGC' and it should be multiple by 3")
    await state.set_state('enter_rna')


