from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "start"),
            types.BotCommand("help", "info"),
            types.BotCommand("transcribe", "DNA to RNA"),
            types.BotCommand("translate", "RNA to protein"),
            types.BotCommand("accession", "search sequences"),
            types.BotCommand("gc_plot", "build a plot"),
        ]
    )
