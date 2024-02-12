import requests
import datetime
from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from config import courcses

cmd_router = Router()


@cmd_router.message(CommandStart())
async def cmd_start(massage: Message):
    s = (f"Assalomu Alaykum {massage.from_user.full_name}\nValyuta kurslari haqida malumot beruvchi botimizgaxush kelinsiz!\n"
         f"Yordam uchun /help buyrug'ni bosing")
    await massage.answer(text=s)


@cmd_router.message(Command("help"))
async def cmd_help(massage: Message):
    s = (f"Quydagi komandalar yordamida botdan samarali foydalamishingiz mumkin:\n\n"
         f"/kurslar - valyuta kurslarini blish\n"
         f"/dollar - dollar kursni blish\n"
         f"/yevro - yevro kursni blish \n"
         f"/rubl - rubl kursni blish\n"
         f"/hafta - 1 haftalik kurslar ro'yxati\n\n"
         f"Agar biron summa jo'natsangiz, bot uni turli valyutalardagi qiymatni qaytaradi. (masalan 1000000)")
    await massage.answer(text=s)


@cmd_router.message(Command("kurslar"))
async def cmd_kurslar(message: Message):
    response = requests.get("https://cbu.uz/uz/arkhiv-kursov-valyut/json/")
    s = "Bugungi valyuta kurslari\n"
    for kurs in response.json():
        if kurs["Ccy"] in ["USD", "EUR", "RUB"]:
            courcses[kurs['Ccy']] = float(kurs["Rate"])
            s += f"1 {kurs["CcyNm_UZ"]} - {kurs["Rate"]} so'm\n"
    await message.answer(text=s)


@cmd_router.message(Command("dollar"))
async def cmd_dollar(message: Message):
    s = f"1 dollar {courcses["USD"]} so'm"
    await message.reply(text=s)


@cmd_router.message(Command("yevro"))
async def cmd_yevro(message: Message):
    s = f"1 yevro {courcses["EUR"]} so'm"
    await message.reply(text=s)


@cmd_router.message(Command("rubl"))
async def cmd_rubl(message: Message):
    s = f"1 rubl {courcses["RUB"]} so'm"
    await message.reply(text=s)


@cmd_router.message(Command("hafta"))
async def cmd_hafta(message: Message):
    today = datetime.date.today()
    s = ''
    for i in range(7):
        response = requests.get(f"https://cbu.uz/oz/arkhiv-kursov-valyut/json/all/{today}/")
        s += f"{today}\n"
        for kurs in response.json():
            if kurs["Ccy"] in ["USD", "EUR", "RUB"]:
                s += f"1 {kurs["CcyNm_UZ"]} - {kurs["Rate"]} so'm\n"
        today = today - datetime.timedelta(days=1)
        s += "\n"
    await message.reply(text=s)