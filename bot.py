import asyncio
import logging
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton

# Ваш API-токен
BOT_TOKEN = "8643337792:AAFR-BSodfGd__BCQO4gzAcTcVTJt7h7NVs"

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Главное меню (Reply-клавиатура)
main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="О нас"), KeyboardButton(text="Направления")],
        [KeyboardButton(text="Контакты")]
    ],
    resize_keyboard=True
)

dp = Dispatcher()

@dp.message(CommandStart())
async def cmd_start(message: Message):
    welcome_text = (
        f"Приветствую, {message.from_user.first_name}!\n\n"
        "Добро пожаловать в официальный бот **Молодежного ресурсного центра**! "
        "Здесь вы можете узнать актуальную информацию о нашей деятельности, "
        "проектах и ключевых направлениях работы.\n\n"
        "Выберите интересующий раздел в меню ниже 👇"
    )
    await message.answer(welcome_text, reply_markup=main_keyboard, parse_mode="Markdown")

@dp.message(F.text == "О нас")
async def about_handler(message: Message):
    about_text = (
        "🏢 **О Молодежном ресурсном центре**\n\n"
        "Молодежный ресурсный центр — это единая площадка для развития, "
        "поддержки гражданских инициатив и самореализации молодежи.\n\n"
        "**Наша миссия:**\n"
        "— Содействие всестороннему развитию и социализации молодежи;\n"
        "— Поддержка молодежных проектов, волонтерских движений и творческих начинаний;\n"
        "— Консультирование и юридическо-информационная помощь."
    )
    await message.answer(about_text, parse_mode="Markdown")

@dp.message(F.text == "Направления")
async def directions_handler(message: Message):
    directions_text = (
        "📌 **Основные направления деятельности:**\n\n"
        "🔹 **Волонтерство и добровольчество** — организация и проведение экологических, социальных и благотворительных акций.\n"
        "🔹 **Культура и досуг** — проведение фестивалей, концертов, фотоконкурсов, интеллектуальных игр и молодежных фестов.\n"
        "🔹 **Предпринимательство и гранты** — информирование о госпрограммах, консультации по грантам и поддержке стартапов.\n"
        "🔹 **Спорт и ЗОЖ** — спартакиады, спортивные турниры и продвижение здорового образа жизни.\n"
        "🔹 **Правовая и консультативная помощь** — поддержка в вопросах трудоустройства, образования и социализации."
    )
    await message.answer(directions_text, parse_mode="Markdown")

@dp.message(F.text == "Контакты")
async def contacts_handler(message: Message):
    contacts_text = (
        "📞 **Контакты и информация:**\n\n"
        "📍 **Адрес:** Аккольский район, г. Акколь\n"
        "🕒 **График работы:** Пн – Пт, с 09:00 до 18:30 (перерыв: 13:00 – 14:30)\n"
        "📸 **Instagram:** [@jro_aqkol](https://www.instagram.com/jro_aqkol)\n\n"
        "Следите за нашими новостями и анонсами предстоящих мероприятий!"
    )
    await message.answer(contacts_text, parse_mode="Markdown", disable_web_page_preview=True)

async def main():
    bot = Bot(token=BOT_TOKEN)
    logging.info("Бот Молодежного ресурсного центра успешно запущен...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
