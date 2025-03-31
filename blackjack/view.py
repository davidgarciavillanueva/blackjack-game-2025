from blackjack.model import Blackjack

class ConsolaBlackjack:


    def __init__(self):
        self.blackjack:Blackjack=Blackjack()
        self.opciones ={
            "1": self.iniciar_nuevo_juego,
            "0": self.salir

        }

    def mostrar_menu(self):
        print(f"\n{'BLACKJACK'}_^30")
        print("1. INICIAR JUEGO ")
        print("0. SALIR  ")
        print(f"\n{'_'}_^30")

    def ejecutar_app(self):
        print("\nBIENVENIDO A UN JUEGO DE BLACKJACK")
        self.registrar_usuario()
        while True:
            self.mostrar_menu()
            opcion = input("selecione una opcion: ")
            accion=self.opciones.get(opcion)
            if accion:
                accion()

            else:
                print("la opcion no es valida ")


    def registrar_usuario(self):
        nombre:str=input("como te llamas?")
        self.blackjack.registrar_jugador(nombre)


    def iniciar_nuevo_juego(self):
        if self.blackjack.jugador.tiene_fichas():
            print("no tenes fichaas")
            return

        apuesta: int= self.recibir_apuesta_jugador()
        self.blackjack.iniciar_juego(apuesta)
        self.mostar_manos(self.blackjack.cupier.mano, self.blackjack.jugador.mano)

        if not self.blackjack.jugador.mano.es_blackjack():
            self.hacer_jugada_de_jugador()

        else:
            self.finalizar_juego()


    def hacer_jugada_de_jugador(self):
        while not self.blackjack.jugador.mano.calcular_valor() > 21:
            respuesta =input("quieres otra carta s o n ?")
            if respuesta == "s":
                self.blackjack.repartir_carta_a_jugador()
                self.mostrar_manos(self.blackjack.cupier.mano, self.blackjack.jugador.mano)
            elif respuesta=="n":
                break


            if self.blackjack.jugador.mano.calcular_valor()> 21:
                self.finalizar_juego()
            else:
                self.hacer_jugada_de_la_casa()

    def hacer_jugada_de_la_casa(self):
        print()
        self.blackjack.destapar_mano_de_la_casa()
        self.mostrar_manos(self.blackjack.cupier.mano, self.blackjack.jugador.mano)

    def finalizar_juego(self):
        print("resultados ")
        nombres


    def mostrar_manos(self,mano_casa, mano_jugador):
        print(f"\n{'MANO CASA':<15}\n{str(mano_casa):<15}")
        print(f"{'VALOR: ' + str(mano_casa.calcular_valor())}")
        print(f"\n{'MANO JUGADOR ':<15}\n{str(mano_jugador):<15}")
        print(f"{'VALOR: ' + str(mano_jugador.calcular_valor())}")





    def recibir_apuesta_jugador(self):
        while True:
            apuesta = input("cuatas fichas desea ingresar")
            if apuesta.isdigit():
                apuesta = int(apuesta)
                if self.blackjack.jugador.tiene_fichas(apuesta):
                    return apuesta
                else:
                    print("no tines fichas para realizar esa apuesta ")
            else:
                print("ingresa un numero numerico ")



    @staticmethod
    def salir():
        print("gracias por jugar ")
        exit(0)