from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove


menu = [
    [InlineKeyboardButton(text="📝 Генерировать текст", callback_data="generate_text"),
    InlineKeyboardButton(text="🖼 Генерировать изображение", callback_data="generate_image")],
    [InlineKeyboardButton(text="💳 Купить токены", callback_data="buy_tokens"),
    InlineKeyboardButton(text="💰 Баланс", callback_data="balance")],
    [InlineKeyboardButton(text="💎 Партнёрская программа", callback_data="ref"),
    InlineKeyboardButton(text="🎁 Бесплатные токены", callback_data="free_tokens")],
    [InlineKeyboardButton(text="🔎 Помощь", callback_data="help")],
    [InlineKeyboardButton(text="🐹 Kand", callback_data="kand")]
]
my_menu = [
    [InlineKeyboardButton(text="🔎 Помощь", callback_data="help")],
    [InlineKeyboardButton(text="🐹 Kand", callback_data="kand")]
]
kand_menu = [[InlineKeyboardButton(text="•⩊• стиль аниме", callback_data="ANIME"),
                InlineKeyboardButton(text="👨🏻‍🎨 стиль Кандински", callback_data="KANDINSKY")],
                [InlineKeyboardButton(text="⚡ свой стиль", callback_data="DEFAULT"),
                InlineKeyboardButton(text="💎 детализированное изображение", callback_data="UHD")],
                [InlineKeyboardButton(text="◀️ Выйти в меню", callback_data="menu")]]
menu = InlineKeyboardMarkup(inline_keyboard=menu)
my_menu = InlineKeyboardMarkup(inline_keyboard=my_menu)
kand_menu = InlineKeyboardMarkup(inline_keyboard=kand_menu)
kand_iexit_menu = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="◀️ Выйти в меню", callback_data="menu"), InlineKeyboardButton(text="🔄 Попробовать снова", callback_data="kand")]])
iexit_skip_kb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="◀️ Выйти в меню", callback_data="menu"), InlineKeyboardButton(text="⏩ Пропустить", callback_data="skip")]])
exit_kb = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="◀️ Выйти в меню")]], resize_keyboard=True)
iexit_kb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="◀️ Выйти в меню", callback_data="menu")]])
