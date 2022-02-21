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


def traducIngFrance():
    txtIng = input("Introduce texto en ingles: ")
    txtFrances = input("Introduce texto en frances: ")
    txtFinalIng = ""
    txtFinalFrance = ""
    encontrado = false

    #convertimos el texto en una lista
    listIng = txtIng.split(" ")
    listFrances = txtFrances.split(" ")
    #recorremos la lista en ingles 
    for palabra in listIng:
        palabraAlmn = ""
        #buscamos si la palabra aparece en el dic esp-ing
        for clave, valor in traductor.espa_ingles.items():
            #comprobamos si la palabra se encuentra en el dicc
            if palabra == valor:
                #ahora comprobamos si la palabra esta en el dic esp-aleman
                if clave in traductor.espa_aleman:
                    palabraAlmn = traductor.espa_aleman[clave]
                    break
        #comprobamos si hemos encontrado la palabra que queriamos en aleman
        if palabraAlmn in traductor.aleman_frances:
            txtFinalIng += traductor.aleman_frances[palabraAlmn]
        else:
            #recorremos la palabra entera para reemplazar el num de caracteres
            numCaracteres = ""
            for _ in palabra:
                numCaracteres += "*"
            txtFinalIng += numCaracteres

        txtFinalIng += " "
    
    #recorremos la lista en frances
    for palabra in listFrances:
        palabraEsp = ""
        encontrado = false
        #buscamos si la palabra aparece en el dic almn-france
        for clave, valor in traductor.aleman_frances.items():
            if palabra == valor:
                #recorremos el dic esp-almn para encontrar la palabra
                for clave2, valor2 in traductor.espa_aleman.items():
                    if clave == valor2:
                        palabraEsp = clave2
                        encontrado = true
                        break
                    else:
                        encontrado = false
            elif encontrado == true:
                break
        #ahora comprobamos si la palabra en esp esta en el dic esp-ing
        if palabraEsp in traductor.espa_ingles:
            txtFinalFrance += traductor.espa_ingles[palabraEsp]
        else:
            #recorremos la palabra entera para reemplazar el num de caracteres
            numCaracteres = ""
            for _ in palabra:
                numCaracteres += "*"
            txtFinalFrance += numCaracteres
        
        txtFinalFrance += " "


    print(f"ingles-frances:  '{txtIng}' --> '{txtFinalIng}'")
    print(f"frances-ingles:  '{txtFrances}' --> '{txtFinalFrance}'")    

#ejecutamos funciones
traducEspIng()
traducEspFrace()
traducIngFrance()