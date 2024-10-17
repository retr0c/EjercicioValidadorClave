
from validadorclave.modelo.validador import Validador, ReglaValidacionGanimedes, ReglaValidacionCalisto

def validar_clave(clave, reglas):
    for regla in reglas:
        validador = Validador(regla)
        try:
            validador.es_valida(clave)
            print(f"La clave es válida para la regla {regla.__class__.__name__}.")
        except Exception as e:
            print(f"Error: {regla.__class__.__name__}: {str(e)}")

def main():
    clave_a_validar = input("Introduce la clave a validar: ")
    reglas = [ReglaValidacionGanimedes(), ReglaValidacionCalisto()]
    validar_clave(clave_a_validar, reglas)

if __name__ == "__main__":
    main()

