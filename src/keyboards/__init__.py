class MainMenu:
    choose_product: str = 'Обрати товар'
    invite: str = 'Запросити друга'
    help: str = 'Допомога'


class Unregistered:
    register: str = 'Ввести ключ-запрошення'


class AdminMenu:
    add_product: str = 'Додати продукт'


class Buttons:
    menu = MainMenu()
    unregistered = Unregistered()
    admin_menu = AdminMenu()
