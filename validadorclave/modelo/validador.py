from errores import ReglaValidacionGanimedesError, ReglaValidacionCalistoError

class ReglaValidacion:
    def __init__(self, longitud_esperada):
        self._longitud_esperada = longitud_esperada

    def _validar_longitud(self, clave):
        if len(clave) <= self._longitud_esperada:
            raise self.exception_class("La clave debe tener una longitud de más de {8} caracteres".format(self._longitud_esperada))

    def _contiene_mayuscula(self, clave):
        return any(c.isupper() for c in clave)

    def _contiene_minuscula(self, clave):
        return any(c.islower() for c in clave)

    def _contiene_numero(self, clave):
        return any(c.isdigit() for c in clave)

    def es_valida(self, clave):
        pass


