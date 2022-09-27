import logging
from aiogram import types
from filters.group_filter import IsGroup
from loader import dp


@dp.message_handler(IsGroup(), commands = ['start'])
async def send_group(message: types.Message):
	logging.info(f"{message.from_user.username} guruhda startni bosdi!")
	logging.info(f"{message.from_user.username}ning id si: {message.from_user.id}")
	await message.reply(f"Assalomu alaykum {message.from_user.get_mention(as_html=True)} siz guruhdasiz!")