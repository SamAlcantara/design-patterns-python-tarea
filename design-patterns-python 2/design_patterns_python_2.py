'''
Facade design pattern
'''
class Cocinar(object):
    '''
    Facade class
    Desc: Proporciona una interfaz sencilla para preparar un plato en lugar de llamar a tres
           diferentes clases
    '''
    def prepararPlato(self):
        self.cortar = Cortar()
        self.cortar.cortarVegetales()

        self.caldero = Caldero()
        self.caldero.hervirVegetales()

        self.freidora = Freidora()
        self.freidora.freir()


class Cortar(object):
    '''
    System class
    '''
    def cortarVegetales(self):
        print("Todas las verduras estan cortadas")


class Caldero(object):
    '''
    System class
    '''
    def hervirVegetales(self):
        print("Todas las verduras se hierven")


class Freidora(object):
    '''
    System class
    '''
    def freir(self):
        print("Todas las verduras se mezclan y se frien.")


if __name__ == "__main__":
    # Uso de la clase de facade para preparar el plato
    cocinar = Cocinar()
    cocinar.prepararPlato()
  
    input()
