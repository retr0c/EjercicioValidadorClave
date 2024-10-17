

from abc import ABC, abstractmethod
from validadorclave.modelo.errores import NoTieneLetraMayusculaError, NoTieneLetraMinusculaError, NoTieneNumeroError, NoTieneCaracterEspecialError, NoCumpleLongitudMinimaError, NoTienePalabraSecretaError

class ReglaValidacion(ABC):
    def __init__(self, longitud_esperada):
        self._longitud_esperada = longitud_esperada

    def _validar_longitud(self, clave):
        return len(clave) > self._longitud_esperada

    def _contiene_mayuscula(self, clave):
        return any(c.isupper() for c in clave)

    def _contiene_minuscula(self, clave):
        return any(c.islower() for c in clave)

    def _contiene_numero(self, clave):
        return any(c.isdigit() for c in clave)

    @abstractmethod
    def es_valida(self, clave):
        pass

class ReglaValidacionGanimedes(ReglaValidacion):
    def __init__(self):
        super().__init__(8)

    def contiene_caracter_especial(self, clave):
        return any(c in "'@','#', '_', '$', '%'" for c in clave)

    def es_valida(self, clave):
        if not self._validar_longitud(clave):
            raise NoCumpleLongitudMinimaError("La clave debe tener una longitud de más de 8 caracteres")
        if not self._contiene_mayuscula(clave):
            raise NoTieneLetraMayusculaError("La clave debe contener al menos una letra mayúscula")
        if not self._contiene_minuscula(clave):
            raise NoTieneLetraMinusculaError("La clave debe contener al menos una letra minúscula")
        if not self._contiene_numero(clave):
            raise NoTieneNumeroError("La clave debe contener al menos un número")
        if not self.contiene_caracter_especial(clave):
            raise NoTieneCaracterEspecialError("La clave debe contener al menos un caracter especial")
        return True

class ReglaValidacionCalisto(ReglaValidacion):
    def __init__(self):
        super().__init__(6)

    def contiene_calisto(self, clave):
        
        if "calisto" in clave.lower():
            
            mayusculas = sum(1 for c in clave if c.isupper())
            
            return mayusculas >= 2 and not clave.isupper()
        return False

    def es_valida(self, clave):
        if not self._validar_longitud(clave):
            raise NoCumpleLongitudMinimaError("La clave debe tener una longitud de más de 6 caracteres")
        if not self._contiene_numero(clave):
            raise NoTieneNumeroError("La clave debe contener al menos un número")
        if not self.contiene_calisto(clave):
            raise NoTienePalabraSecretaError("La palabra calisto debe estar escrita con al menos dos letras en mayúscula")
        return True


class Validador:
    def __init__(self, regla):
        self.regla = regla

    def es_valida(self, clave):
        return self.regla.es_valida(clave)
