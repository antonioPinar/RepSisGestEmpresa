from sqlalchemy import false, true
import dicionario as traductor


def traducEspIng():

    txtEsp = input("Introduce texto en español: ")
    txtIngles = input("Introduce texto en ingles: ")
    txtFinalEsp = ""
    txtFinalIngles = ""
    encontrado = false

    #convertimos el texto en una lista
    listEsp = txtEsp.split(" ")
    listIngles = txtIngles.split(" ")

    #recorremos la lista en español 
    for palabra in listEsp:
        #buscamos si la palabra aparece en el dic
        if palabra in traductor.espa_ingles:
            txtFinalEsp += traductor.espa_ingles[palabra]

        else:
            #recorremos la palabra entera para reemplazar el num de caracteres
            numCaracteres = ""
            for _ in palabra:
                numCaracteres += "*"
            
            txtFinalEsp += numCaracteres

        txtFinalEsp += " "

    for palabra in listIngles:
        #buscamos si la palabra aparece en el dic
        for clave, valor in traductor.espa_ingles.items():
            #comprobamos si la palabra se encuentra en el diccionario
            if palabra == valor:
                txtFinalIngles += clave
                encontrado = true
                break
            else:
                encontrado = false

        if encontrado == false:
            #recorremos la palabra entera para reemplazar el num de caracteres
            numCaracteres = ""
            for _ in palabra:
                numCaracteres += "*"
            
            txtFinalIngles += numCaracteres

        txtFinalIngles += " "

    print(f"español-ingles:  '{txtEsp}' --> '{txtFinalEsp}'")
    print(f"ingles-español:  '{txtIngles}' --> '{txtFinalIngles}'")

#ejecutamos funciones
traducEspIng()