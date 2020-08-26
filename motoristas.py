class motoristas:

    def __init__(self, nome, cargo):
        self._nome = nome
        self._cargo = cargo

    @property
    def nome(self):
        return self._nome.title()

    def cargo(self):
        if self.cargo == 1:
            print('Jose Raimundo Barros de Araújo')