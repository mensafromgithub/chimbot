from aiogram import F, Router, types
from aiogram.filters import Command
from aiogram.types import Message
from aiogram import flags
from aiogram.fsm.context import FSMContext
from aiogram.types.callback_query import CallbackQuery
from aiogram.types import BufferedInputFile
import kandinsky
import stickers
from states import Kand
import kb
import text

router = Router()


@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer(text.greet.format(name=msg.from_user.full_name), reply_markup=kb.my_menu)


@router.message(F.text == "Меню")
@router.message(F.text == "Выйти в меню")
@router.message(F.text == "◀️ Выйти в меню")
async def menu(msg: Message, state: FSMContext):
    await state.clear()
    await msg.answer(text.menu, reply_markup=kb.my_menu)


@router.callback_query(F.data == "menu")
async def clbk_menu(clbck: CallbackQuery, state: FSMContext):
    await state.clear()
    await clbck.message.answer(text.menu, reply_markup=kb.my_menu)


@router.callback_query(F.data == "skip")
async def clbk_menu(clbck: CallbackQuery, state: FSMContext):
    await state.next()


@router.callback_query(F.data == "help")
async def bot_help(clbck: CallbackQuery):
    await clbck.message.edit_text(text._help, reply_markup=kb.iexit_kb)


"""@router.callback_query(F.data == "kand")
async def kand_input_image_prompt(clbck: CallbackQuery, state: FSMContext):
    await state.set_state(Gen.kand_prompt)
    await clbck.message.edit_text(text.kand)
    await clbck.message.answer(text.gen_exit, reply_markup=kb.iexit_kb)"""


@router.callback_query(F.data == "kand")
async def kand_input_image_style(clbck: CallbackQuery, state: FSMContext):
    await clbck.message.answer(text.kand_style, reply_markup=kb.kand_menu)
    await state.set_state(Kand.style)


@router.callback_query(Kand.style, F.data.in_(['ANIME', 'KANDINSKY', 'DEFAULT', 'UHD']))
async def kand_input_image_prompt(clbck: CallbackQuery, state: FSMContext):
    await state.update_data(style=clbck.message.text) 
    await clbck.message.answer(text.kand_prompt, reply_markup=kb.iexit_kb)
    await state.set_state(Kand.prompt)


@router.message(Kand.prompt)
async def kand_input_image_aprompt(msg: Message, state: FSMContext):
    await state.update_data(prompt=msg.text) 
    await msg.answer(text.kand_aprompt, reply_markup=kb.iexit_kb)
    await state.set_state(Kand.aprompt)


@router.message(Kand.aprompt)
@flags.chat_action("upload_photo")
async def generate_image(msg: Message, state: FSMContext):
    await state.update_data(aprompt=msg.text) 
    user_data = await state.get_data()
    style, prompt, aprompt = user_data['style'], user_data['prompt'], user_data['aprompt']
    mesg = await msg.answer_sticker(stickers.cat_sticker)
    img_res = kandinsky.api.check_generation(kandinsky.api.generate(prompt=prompt, style=style, aprompt=aprompt, model=kandinsky.model_id))#await
    if len(img_res) == 0:#
        return await mesg.edit_text(text.gen_error, reply_markup=kb.exit_kb) #
    await mesg.delete()
    await mesg.answer_photo(photo=BufferedInputFile(img_res[0], 'answer_photo'), caption=text.kand_watermark, reply_markup=kb.kand_iexit_menu)#0
    await state.clear()


"""@router.message(Gen.kand_prompt)
@flags.chat_action("upload_photo")
async def generate_image(msg: Message, state: FSMContext):
    data = msg.text.lower().split(';')
    style, prompt, aprompt = [i.split(':')[1].strip() for i in data]
    mesg = await msg.answer_sticker(stickers.cat_sticker)
    img_res = kandinsky.api.check_generation(kandinsky.api.generate(prompt=prompt, style=kandinsky.styles[style], aprompt=aprompt, model=kandinsky.model_id))#await
    if len(img_res) == 0:#
        return await mesg.edit_text(text.gen_error, reply_markup=kb.exit_kb) #
    await mesg.delete()
    await mesg.answer_photo(photo=BufferedInputFile(img_res[0], 'answer_photo'), caption=text.kand_watermark)#0"""
