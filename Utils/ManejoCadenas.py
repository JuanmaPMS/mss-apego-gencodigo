class Cadenas:
    def eliminar_lineas(self, cadena):
        lineas = cadena.splitlines()
        if len(lineas) > 2:
            return "\n".join(lineas[1:-1])
        return ""