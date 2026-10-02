import mysql.connector


class BaseDatos:

    def __init__(self):
        self.conexion = None
        self.cursor = None

    def conectar(self):

        self.conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="ejercicio2"
        )

        self.cursor = self.conexion.cursor()

    def cerrar(self):

        if self.cursor:
            self.cursor.close()

        if self.conexion:
            self.conexion.close()

    def guardar_tabla(self, numero, resultados):

        self.conectar()

        sql = """
            INSERT INTO tablas_multiplicar
            (numero, multiplicador, resultado)
            VALUES (%s, %s, %s)
        """

        for fila in resultados:

            valores = (
                numero,
                fila["multiplicador"],
                fila["resultado"]
            )

            self.cursor.execute(sql, valores)

        self.conexion.commit()

        self.cerrar()