class Item:
    def __init__(
        self, code, name, description, can_be_carried, usable, is_unlocked=None
    ):
        self.__code = code
        self.__name = name
        self.__description = description
        self.__can_be_carried = can_be_carried
        self.__usable = usable
        self.__is_unlocked = is_unlocked

    @property
    def code(self):
        return self.__code

    @property
    def name(self):
        return self.__name

    @property
    def description(self):
        return self.__description

    @property
    def can_be_carried(self):
        return self.__can_be_carried

    @property
    def usable(self):
        return self.__usable

    @property
    def is_unlocked(self):
        return self.__is_unlocked
