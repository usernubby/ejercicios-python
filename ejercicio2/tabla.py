class TablaMultiplicar:

    def __init__(self, numero):
        self.numero = numero

    def generar_tabla(self):

        resultados = []

        for i in range(1, 11):

            resultado = self.numero * i

            resultados.append({
                "multiplicador": i,
                "resultado": resultado
            })

        return resultados