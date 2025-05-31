from aiogram.fsm.state import State, StatesGroup


class ItemStates(StatesGroup):
    title = State()
    price = State()
    text = State()
    image = State()


