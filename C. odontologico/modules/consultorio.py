from datetime import datetime
from modules.cliente import Cliente
from modules.tarifas import calcular_valor
import unicodedata

class Consultorio:
    def __init__(self):
        self.lista_clientes = []

    def normalizar_texto(self, texto):
        return ''.join(c for c in unicodedata.normalize('NFD', texto.lower()) if unicodedata.category(c) != 'Mn')

    def agregar_cliente(self):
        try:
            # --- Cédula ---
            while True:
                dni = input("Ingrese cédula del cliente: ").strip()
                if not dni.isdigit() or len(dni) < 5:
                    print("Cédula inválida.")
                else:
                    break

            # --- Nombre ---
            while True:
                nombre_completo = input("Ingrese nombre completo: ").strip().title()
                if not nombre_completo.replace(" ", "").isalpha():
                    print("Nombre inválido.")
                else:
                    break

            # --- Teléfono ---
            while True:
                telefono_contacto = input("Ingrese teléfono: ").strip()
                if not telefono_contacto.isdigit() or len(telefono_contacto) < 7:
                    print("Teléfono inválido.")
                else:
                    break

            # --- Tipo de cliente ---
            tipos = ["PARTICULAR", "EPS", "PREPAGADA"]
            while True:
                tipo_cliente = input(f"Tipo de cliente ({'/'.join(tipos)}): ").strip().upper()
                if tipo_cliente not in tipos:
                    print(f"Opciones válidas: {', '.join(tipos)}")
                else:
                    break

            # --- Tipo de servicio ---
            servicios = ["Limpieza", "Calzas", "Extracción", "Diagnóstico"]
            while True:
                tipo_servicio_input = input(f"Tipo de atención ({'/'.join(servicios)}): ").strip()
                encontrado = False
                for s in servicios:
                    if self.normalizar_texto(tipo_servicio_input) == self.normalizar_texto(s):
                        tipo_servicio = s
                        encontrado = True
                        break
                if not encontrado:
                    print(f"Opciones válidas: {', '.join(servicios)}")
                else:
                    break

            # --- Cantidad ---
            if tipo_servicio in ["Limpieza", "Diagnóstico"]:
                cantidad_servicio = 1
            else:
                while True:
                    cantidad_input = input(f"Ingrese cantidad de {tipo_servicio}: ").strip()
                    if not cantidad_input.isdigit() or int(cantidad_input) <= 0:
                        print("Cantidad inválida.")
                    else:
                        cantidad_servicio = int(cantidad_input)
                        break

            # --- Prioridad ---
            prioridades = ["Normal", "Urgente"]
            while True:
                prioridad_input = input(f"Prioridad de atención ({'/'.join(prioridades)}): ").strip().capitalize()
                if prioridad_input not in prioridades:
                    print(f"Opciones válidas: {', '.join(prioridades)}")
                else:
                    prioridad_servicio = prioridad_input
                    break

            # --- Fecha ---
            while True:
                fecha_cita = input("Fecha de la cita (dd-mm-yyyy): ").strip()
                try:
                    datetime.strptime(fecha_cita, "%d-%m-%Y")
                    break
                except ValueError:
                    print("Formato de fecha inválido. Use dd-mm-yyyy.")

            # --- Calcular valor ---
            valor_total = calcular_valor(tipo_cliente, tipo_servicio, cantidad_servicio)

            # --- Crear cliente y agregar ---
            cliente = Cliente(dni, nombre_completo, telefono_contacto, tipo_cliente, tipo_servicio,
                              cantidad_servicio, prioridad_servicio, fecha_cita, valor_total)
            self.lista_clientes.append(cliente)
            print(f"\nCita registrada. Valor a pagar: ${valor_total:,}\n")

        except Exception as e:
            print(f"Error inesperado: {e}")

    # --- Mostrar resumen ---
    def mostrar_resumen(self):
        if not self.lista_clientes:
            print("No hay citas registradas.")
            return

        total_clientes = len(self.lista_clientes)
        ingresos = sum(c.valor_total for c in self.lista_clientes)
        extracciones = sum(1 for c in self.lista_clientes if self.normalizar_texto(c.tipo_servicio) == "extraccion")

        print(f"\nTotal de clientes: {total_clientes}")
        print(f"Ingresos totales: ${ingresos:,}")
        print(f"Número de clientes con extracción: {extracciones}")

    # --- Listar ordenado por valor ---
    def listar_ordenado(self):
        return sorted(self.lista_clientes, key=lambda c: c.valor_total, reverse=True)

    # --- Buscar por cédula ---
    def buscar_por_cedula(self, dni):
        return [c for c in self.lista_clientes if c.dni == dni]

    # --- Eliminar cita ---
    def eliminar_cita(self):
        dni = input("Ingrese cédula para eliminar cita: ").strip()
        encontrados = self.buscar_por_cedula(dni)
        if not encontrados:
            print("Cliente no encontrado.")
            return

        print("Seleccione la cita a eliminar:")
        for idx, c in enumerate(encontrados, 1):
            print(f"{idx}. {c.tipo_servicio} - Fecha: {c.fecha_cita} - Valor: ${c.valor_total:,}")

        while True:
            op = input("Número de cita a eliminar: ").strip()
            if not op.isdigit() or int(op) < 1 or int(op) > len(encontrados):
                print("Selección inválida.")
            else:
                self.lista_clientes.remove(encontrados[int(op)-1])
                print("Cita eliminada correctamente.\n")
                break
