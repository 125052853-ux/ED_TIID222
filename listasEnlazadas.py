
class Nodo:

    def __init__(self, numero):
        self.numero = numero
        self.siguiente = None


class ListEnlazada:

    def __init__(self):
        self.cabeza = None

    def insertar_nodo_al_inicio(self, numero):
        nuevo_nodo = Nodo(numero)

        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            return

        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo

    def Insertar_Nodo_al_Final(self, numero):

        nuevo_nodo = Nodo(numero)

        if self.cabeza == None:
            self.cabeza = nuevo_nodo
            return

        actual = self.cabeza

        # Avanzar mientras exista un nodo siguiente
        while actual.siguiente:
            # Avanzar al siguiente nodo
            actual = actual.siguiente

        # Conectar el último nodo al nuevo nodo
        actual.siguiente = nuevo_nodo

    # Método para imprimir nuestra lista enlazada
    def Imprimir_ListaEnlazada(self):

        actual = self.cabeza

        while actual:
            # Imprimir sin saltos de línea
            print(actual.numero, " → ", end=" ")

            # Avanzar al siguiente nodo
            actual = actual.siguiente

        # Indicar el final de la lista
        print("None")

    def eliminar_nodo_al_inicio(self):
        
        if self.cabeza is None:
            print("La lista está vacía.")
            return

        # Apuntar la cabeza al siguiente nodo
        self.cabeza = self.cabeza.siguiente

    def eliminar_nodo_al_final(self):
        
        if self.cabeza is None:
            print("La lista está vacía.")
            return

        
        if self.cabeza.siguiente is None:
            self.cabeza = None
            return

        
        actual = self.cabeza
        while actual.siguiente.siguiente:
            actual = actual.siguiente

        
        actual.siguiente = None


Mi_lista = ListEnlazada()
Mi_lista.insertar_nodo_al_inicio(2)
Mi_lista.insertar_nodo_al_inicio(1)
Mi_lista.Insertar_Nodo_al_Final(3)
Mi_lista.Insertar_Nodo_al_Final(4)

print("Lista Inicial:")
Mi_lista.Imprimir_ListaEnlazada()

Mi_lista.eliminar_nodo_al_inicio()
print("\nDespués de eliminar al inicio:")
Mi_lista.Imprimir_ListaEnlazada() 


Mi_lista.eliminar_nodo_al_final()
print("\nDespués de eliminar al final:")
Mi_lista.Imprimir_ListaEnlazada()
