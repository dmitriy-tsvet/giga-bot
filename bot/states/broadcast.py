from aiogram.fsm.state import StatesGroup, State


class BroadcastStates(StatesGroup):
    get_text = State()
    broadcast = State()
