from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


add_group = InlineKeyboardMarkup(row_width=2)

btn = InlineKeyboardButton(text = "Guruhga qo'shish!", url = "https://telegram.me/moderator_n1bot?startgroup=new")
add_group.insert(btn)
btn1 = InlineKeyboardButton(text = "Buyruqlar!", callback_data="help")
add_group.insert(btn1)
