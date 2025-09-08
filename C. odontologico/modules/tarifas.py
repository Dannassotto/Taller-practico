PRECIOS = {
    "PARTICULAR": {"base": 80000, "servicios": {"Limpieza": 60000, "Calzas": 80000, "Extracción": 100000, "Diagnóstico": 50000}},
    "EPS": {"base": 5000, "servicios": {"Limpieza": 0, "Calzas": 40000, "Extracción": 40000, "Diagnóstico": 0}},
    "PREPAGADA": {"base": 30000, "servicios": {"Limpieza": 0, "Calzas": 10000, "Extracción": 10000, "Diagnóstico": 0}}
}

def calcular_valor(tipo_cliente, servicio, cantidad):
    tipo_cliente = tipo_cliente.strip().upper()
    servicio = servicio.strip().capitalize()
    if tipo_cliente not in PRECIOS:
        return 0
    base = PRECIOS[tipo_cliente]["base"]
    valor_servicio = PRECIOS[tipo_cliente]["servicios"].get(servicio, 0)
    return base + (valor_servicio * cantidad)
