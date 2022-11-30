from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "start"),
            types.BotCommand("help", "info"),
            types.BotCommand("transcribe", "dna to rna"),
            types.BotCommand("translate", "rna to protein"),
            types.BotCommand("accession", "search sequences"),
        ]
    )
