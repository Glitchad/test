class Room:
    def __init__(self, code, name, description, items, entities):
        self.__code = code
        self.__name = name
        self.__description = description
        self.__items = items
        self.__entities = entities

    @property
    def code(self):
        return self.__code

    @property
    def name(self):
        return self.__name

    @property
    def description(self):
        return self.__name

    @property
    def items(self):
        return self.__items

    @property
    def entities(self):
        return self.__entities
