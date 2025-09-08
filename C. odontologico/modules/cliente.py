class Cliente:
    def __init__(self, dni, nombre_completo, telefono_contacto, tipo, tipo_servicio, cantidad_servicio, prioridad_servicio, fecha_cita, valor_total):
        self.dni = dni
        self.nombre_completo = nombre_completo
        self.telefono_contacto = telefono_contacto
        self.tipo_cliente = tipo
        self.tipo_servicio = tipo_servicio
        self.cantidad = cantidad_servicio
        self.prioridad = prioridad_servicio
        self.fecha_cita = fecha_cita
        self.valor_total = valor_total
