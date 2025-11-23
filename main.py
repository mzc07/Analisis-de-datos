import os
from src.data_loader import cargar_dataset
from src.estadisticas import calcular_estadisticas
from src.tendencias import ver_tendencias
from src.comparacion import menu_comparaciones
from src.outliers import menu_outliers

def limpiar_pantalla():
    os.system('cls')

def menu_principal():
    print("=== Analisis de dataset ===")
    print("1. Cargar y validar dataset.")
    print("2. Estadistica del dataset.")
    print("3. Ver tendencias anuales.")
    print("4. Comparacion entre paises.")
    print("5. Variacion interna y estabilidad.")
    print("6. Outliders.")
    print("7. Segmentacion.")
    print("8. Visualizar datos.")
    print("0. Salir.")

if __name__ == '__main__':
    while True:
        limpiar_pantalla()
        menu_principal()
        try:
            opcion_usuario = int(input("Ingrese su opcion: "))
        except Exception as error:
            print(f'Error: {error}.')
        else: 
            match opcion_usuario:
                case 1:
                    cargar_dataset()
                case 2:
                    calcular_estadisticas()
                case 3:
                    ver_tendencias()
                case 4:
                    limpiar_pantalla()
                    menu_comparaciones() 
                case 5: 
                    None
                case 6:
                    limpiar_pantalla()
                    menu_outliers()
                case 7:
                    segmentacion_tendencia()
                case 8:
                    
                case 0:
                    print("Gracias por usar el programa.")
                    break
                case _:
                    print("Ingrese una opcion valida.")
        input("Presione enter para continuar.")
