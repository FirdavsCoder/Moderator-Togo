import logging
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from filters.private_filter import IsPrivate
from keyboards.inline.buttons_for import add_group
from loader import dp


@dp.message_handler(IsPrivate(), CommandStart())
async def bot_start(message: types.Message):
	logging.info(f"{message.from_user.username} shaxsiyda startni bosi!")
	logging.info(f"{message.from_user.username}ning id si: {message.from_user.id}")
	text = f"👋Assalomu alaykum!, {message.from_user.full_name}!\n\n"
	text += "👮🏻‍♂️ Gruppada yangi a'zolar Qo'shildi - Chiqdi yani (Kirdi - Chiqdi) haqida malumotni o'chirish va guruhni reklamalardan tozalash uchun maxsus bot. \n\n\
☑️ Men ishlashim uchun guruhingizga qo'shib admin berishingiz kerak !"
	await message.answer(text, reply_markup=add_group)
 
 
 
@dp.callback_query_handler(text_contains = "help")
async def send_help(call: types.CallbackQuery):
    logging.info(f"{call.from_user.full_name} buyruqlarni korayapti!")
    await call.message.answer("👮‍♂️ Guruh adminlari ishlatishi mumkin bo‘lgan buyruqlar:\n\n/ro - Guruh a‘zosini “read only” rejimiga tushuradi;\n/unro - Guruh a‘zosidan cheklovni oladi;\n/ban  - Guruh a‘zosini  guruhdan chiqaradi,boshqa qaytib kira  olmaydi;\n/unban - Bandan oladi; \n\n \
☑️ Qo'shimcha xizmatlar:\n \
/soat  - Soatni ko'rsatadi. \n\
/sana - Sanani ko'rsatadi. \n\
/id - Sizning id raqamingiz.\n \
/gid - Guruh id raqami.")
