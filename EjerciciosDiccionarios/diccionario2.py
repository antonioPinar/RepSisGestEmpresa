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
    #recorremos la lista en ingles
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


def traducEspFrace():
    txtEsp = input("Introduce texto en español: ")
    txtFrances = input("Introduce texto en frances: ")
    txtFinalEsp = ""
    txtFinalFrance = ""
    encontrado = false

    #convertimos el texto en una lista
    listEsp = txtEsp.split(" ")
    listFrances = txtFrances.split(" ")
    #recorremos la lista en español 
    for palabra in listEsp:
        #buscamos si la palabra aparece en el dic asociado al aleman, para poder hacer la conversion
        if palabra in traductor.espa_aleman:
            palabraAleman = traductor.espa_aleman[palabra]
            #entonces abrimos el dic donde se encuentran las palabras en frances
            if palabraAleman in traductor.aleman_frances:
                txtFinalEsp += traductor.aleman_frances[palabraAleman]
                encontrado = true
            else:
                encontrado = false
        else:
            encontrado = false

        if encontrado == false:
            #recorremos la palabra entera para reemplazar el num de caracteres
            numCaracteres = ""
            for _ in palabra:
                numCaracteres += "*"
            txtFinalEsp += numCaracteres
        txtFinalEsp += " "

    #recorremos la lista en frances
    for palabra in listFrances:
        encontrado = false
        #buscamos si la palabra aparece en el dic
        for clave, valor in traductor.aleman_frances.items():
            #comprobamos si la palabra se encuentra en el diccionario
            if palabra == valor:
                #volvemos a comprobar si esta en el dic donde encontramos la palabra en español
                for clave2, valor2 in traductor.espa_aleman.items():
                    if clave == valor2:
                        txtFinalFrance += clave2
                        encontrado = true
                        break
                    else:
                        encontrado = false
            elif encontrado == true:
                break
            else:
                encontrado = false
        if encontrado == false:
            #recorremos la palabra entera para reemplazar el num de caracteres
            numCaracteres = ""
            for _ in palabra:
                numCaracteres += "*"
            txtFinalFrance += numCaracteres
        txtFinalFrance += " "


    print(f"español-frances:  '{txtEsp}' --> '{txtFinalEsp}'")
    print(f"frances-español:  '{txtFrances}' --> '{txtFinalFrance}'")

#ejecutamos funciones
#traducEspIng()
traducEspFrace()