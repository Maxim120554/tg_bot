

class User:
    id = 0
    name = ''
    lastname = ''
    favorites = []        # избранные монеты
    messages = []
    is_add_favorites = False

    def __init__(self, name, lastname, id):
        self.id = id
        self.name = name
        self.lastname = lastname
