from model import Model
from view import View
from controller import Controller


class App:

    model = Model()
    view = View()
    controller = Controller(model, view)
    view.controller = controller


if __name__ == '__main__':
    app = App()
    app.controller.menu_principal()
