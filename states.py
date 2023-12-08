from aiogram.fsm.state import StatesGroup, State


class Kand(StatesGroup):
    style = State()
    prompt = State()
    aprompt = State()
