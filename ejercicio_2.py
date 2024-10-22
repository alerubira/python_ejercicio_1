class CuentaBancaria:
    def __init__(self, titular, numero_de_cuenta, saldo=0):
        self.titular = titular
        self.numero_de_cuenta = numero_de_cuenta
        self.saldo = saldo
        self.movimientos = []  # Lista para registrar los movimientos de la cuenta

    def hacer_ingreso(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            self.movimientos.append(f"Ingreso: ${cantidad}")
            print(f"Se han ingresado ${cantidad}. Nuevo saldo: ${self.saldo}")
        else:
            print("La cantidad a ingresar debe ser mayor que cero.")

    def retirar_dinero(self, cantidad):
        if cantidad <= 0:
            print("La cantidad a retirar debe ser mayor que cero.")
            return

        if self.saldo >= cantidad:
            self.saldo -= cantidad
            self.movimientos.append(f"Retiro: ${cantidad}")
            print(f"Se han retirado ${cantidad}. Nuevo saldo: ${self.saldo}")
        else:
            print("No se puede retirar dinero. Saldo insuficiente.")

    def consultar_saldo(self):
        print(f"El saldo actual de la cuenta es: ${self.saldo}")

    def movimientos_de_cuenta(self):
        if not self.movimientos:
            print("No hay movimientos registrados.")
        else:
            print("Movimientos de la cuenta:")
            for movimiento in self.movimientos:
                print(movimiento)


# Ejemplo de uso de la clase
if __name__ == "__main__":
    # Crear una cuenta bancaria
    cuentaDeJuan = CuentaBancaria("Juan Pérez", "123456789")

    # Hacer ingresos y retirar dinero
    cuentaDeJuan.hacer_ingreso(2000)
    cuentaDeJuan.consultar_saldo()
    cuentaDeJuan.retirar_dinero(500)
    cuentaDeJuan.consultar_saldo()
    cuentaDeJuan.retirar_dinero(600)  
    cuentaDeJuan.consultar_saldo()
    cuentaDeJuan.retirar_dinero(1500)# Intento de retirar más de lo que hay
    cuentaDeJuan.consultar_saldo()
    cuentaDeJuan.movimientos_de_cuenta()
