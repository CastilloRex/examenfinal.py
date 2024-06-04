def contar_ocurrencias(palabra):
    try:
        archivo = open('input.txt', 'r')
        lineas = archivo.readlines()
        archivo.close()
        
        ocurrencias = 0
        buscar_palabra = []

        num_linea = 1 
        for linea in lineas:
            if palabra in linea:
                ocurrencias += linea.count(palabra)
                buscar_palabra.append("{} - {}".format(num_linea, linea.strip()))
            num_linea += 1  

        return ocurrencias, buscar_palabra
    except ValueError:
        print("El archivo input.txt no esta creado.")
        return 0, []

def resultado(buscar_palabra):
    result = open('result.txt', 'w')
    for linea in buscar_palabra:
        result.write(linea + ' ')
    result.close()

def main():
    palabra = input("Ingrese la palabra a buscar: ")
    ocurrencias, buscar_palabra = contar_ocurrencias(palabra)
    print("Ocurrencias:", ocurrencias)
    resultado(buscar_palabra)

main()

