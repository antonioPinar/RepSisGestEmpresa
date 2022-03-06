#creamos una excepcion personalizada
class ListaMayorError(Exception):
    pass


def sumaListas(lista1, lista2):
    listaD = []
    #comprobamos si alguna lista es mayor
    if len(lista1) > len(lista2):
        raise ListaMayorError("Error, primera lista mayor tamaño que la segunda.")
    elif len(lista1) < len(lista2):
        raise ListaMayorError("Error, segunda lista mayor tamaño que la primera.")
    else:
        for i in range(len(lista1)):
            listaD.append(lista1[i]/lista2[i])

    return listaD
    