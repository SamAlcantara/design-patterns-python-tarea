'''
Template method Pattern
'''
import abc


class tresdiasdeviaje(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def transporte(self):
        pass

    @abc.abstractmethod
    def dia1(self):
        pass

    @abc.abstractmethod
    def dia2(self):
        pass

    @abc.abstractmethod
    def dia3(self):
        pass

    @abc.abstractmethod
    def casa(self):
        pass

    def itinerario(self):
        print("El viaje ha comenzado")
        self.transporte()
        self.dia1()
        self.dia2()
        self.dia3()
        self.casa()
        print("El viaje ha terminado")


class viajealsur(tresdiasdeviaje):
    def transporte(self):
        print("Ir en guagua y registrarse en el hotel")

    def dia1(self):
        print("Dia-1: disfrutar en el hotel y compartir con los familiares")

    def dia2(self):
        print("Dia-2: Visitar lugares historicos")

    def dia3(self):
        print("Dia-3: Ir de comprar y disfrutar con la familia")

    def casa(self):
        print("Volver a casa")


class viajealnorte(tresdiasdeviaje):
    def transporte(self):
        print("Ir en carro y registrarse en el hotel")

    def dia1(self):
        print("Dia-1: Ir a la playa y disfrutar del lugar")

    def dia2(self):
        print("Dia-2: Ir al rio y en la noche cenar bastante")

    def dia3(self):
        print("Dia-3: Ir de comprar y disfrutar con la familia")

    def casa(self):
        print("Volver a casa")


if __name__ == "__main__":
    lugar = input("Donde quieres ir? (norte o sur) ")
    if lugar == 'norte':
        trip = viajealnorte()
        trip.itinerario()
    elif lugar == 'sur':
        trip = viajealsur()
        trip.itinerario()
    else:
        print("Lo siento, no tenemos ningun viaje hacia ese lugar!")
   
    input()
