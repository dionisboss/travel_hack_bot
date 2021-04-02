from aiogram.dispatcher.filters.state import StatesGroup, State


class GeneralState(StatesGroup):
    Main_menu = State()
    Exhibition_start = State()
    Excursion = State()
    Free_float = State()
    Quiz = State()
    End = State()

class Excursion(StatesGroup):
    Starting = State()
    Exhibit1 = State()
    Exhibit2 = State()
    Exhibit3 = State()
    Exhibit4 = State()
    End = State()



# class ExcursionState(StatesGroup):
#     def __init__(self, db_exhibition_id):
#         self.db_exhibition_id = db_exhibition_id
#
#     def form_states(self):
#         pass
#
# class Questionare_state(StatesGroup):
#     pass
