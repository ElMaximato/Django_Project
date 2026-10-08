class EstrategiaDescuento:
    """Interfaz comun para todas las estrategias de descuento."""

    def calcular(self, precio):
        raise NotImplementedError


class DescuentoElectronica(EstrategiaDescuento):
    """10% de descuento para productos de la categoria Electronica."""

    def calcular(self, precio):
        return precio * 0.90


class DescuentoRopa(EstrategiaDescuento):
    """20% de descuento para productos de la categoria Ropa."""

    def calcular(self, precio):
        return precio * 0.80


class SinDescuento(EstrategiaDescuento):
    """Estrategia por default: no aplica ningun descuento."""

    def calcular(self, precio):
        return precio


def obtener_estrategia(categoria_nombre):
    """
    Devuelve la estrategia de descuento que corresponde al nombre de
    categoria recibido. Si la categoria no esta en el diccionario,
    regresa SinDescuento() por default.
    """
    estrategias = {
        'Electronica': DescuentoElectronica(),
        'Ropa': DescuentoRopa(),
    }
    return estrategias.get(categoria_nombre, SinDescuento())