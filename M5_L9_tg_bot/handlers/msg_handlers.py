from config import courcses
from aiogram import Router
from aiogram.types import Message
import requests

msg_router = Router()


@msg_router.message()
async def convert_sum(message:Message):
    if str(message.text).count("-") == 2:
        x = str(message.text)
        x_index = str(x).index("-")
        sana = x[x_index - 4: x_index + 6]
        if x_index > 5:
            matn = x[:x_index - 5]
        else:
            matn = x[x_index + 7:]
        if "USD" == matn or "dollar" == matn:
            matn = "USD"
            response = requests.get(f"https://cbu.uz/oz/arkhiv-kursov-valyut/json/{matn}/{sana}/")
            for kurs in response.json():
                s = f"{sana}\n1 dollar: {kurs["Rate"]} so'm"

        elif "EUR" == matn:
            response = requests.get(f"https://cbu.uz/oz/arkhiv-kursov-valyut/json/{matn}/{sana}/")
            for kurs in response.json():
                s = f"{sana}\n1 yevro: {kurs["Rate"]} so'm"

        elif "RUB" == matn:
            response = requests.get(f"https://cbu.uz/oz/arkhiv-kursov-valyut/json/{matn}/{sana}/")
            for kurs in response.json():
                s = f"{sana}\n1 rubl: {kurs["Rate"]} so'm"
        else:
            await message.reply(f"matni noto'g'ri krtildi !")
        await message.reply(text=s)

    elif message.text.isdigit():
        x = int(message.text)
        s = (f"{x} so'm:\n"
             f"- {x / courcses["USD"]:.2f} dollar\n"
             f"- {x / courcses["EUR"]:.2f} yevro\n"
             f"- {x / courcses["RUB"]:.2f} rubl")
        await message.reply(text=s)
    else:
        x = str(message.text)
        if "dollor" or "$" in x:
            a = [int(s) for s in x.split() if s.isdigit()]
            if a:
                x1 = a[0]
                s = f"{x1 * courcses['USD']: .2f} so'm"
        elif "yevro" or "€" in x:
            a = [int(s) for s in x.split() if s.isdigit()]
            if a:
                x1 = a[0]
                s = f"{x1 * courcses['EUR']: .2f} so'm"
        elif "rubl" in x:
            a = [int(s) for s in x.split() if s.isdigit()]
            if a:
                x1 = a[0]
                s = f"\t -{x1 * courcses['RUB']: .2f} so'm\n"
        await message.reply(text=s)