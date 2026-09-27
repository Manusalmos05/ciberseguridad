from langdetect import detect
import string
ALFABETO=string.ascii_lowercase


def algoritmo_des(texto_cifrado, clave_des):
    """Esta funcion recive el texto y la clave para descifrar el texto ya encriptado"""

    texto_plano=""
    for letra in texto_cifrado:
        if letra not in ALFABETO:
            texto_plano +=letra
        else:
            indice_letra_cifrada=ALFABETO.index(letra)
            indice_letra_des= indice_letra_cifrada-clave_des
            texto_plano+=ALFABETO[indice_letra_des]
    return texto_plano

def fuerza_bruta(texto_cifrado):

    espacio_claves=range(len(ALFABETO))
    for clave in espacio_claves:
        texto_plano=algoritmo_des(texto_cifrado, clave)
        lenguaje=detect(texto_plano)
        if lenguaje=="es":
            print(f"el texto descifrado es: {texto_plano}")
            print (f" la clave es: {clave}")
            return


if __name__ =="__main__":
    
    texto_cifrado=input("introduce el texto cifrado: ").lower()
    


    fuerza_bruta(texto_cifrado)
