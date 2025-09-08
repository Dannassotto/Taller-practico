from modules.consultorio import Consultorio

def menu():
    consultorio = Consultorio()
    while True:
        print("""
===============================
   CONSULTORIO ODONTOLÓGICO
===============================
1. Agendar cita
2. Mostrar resumen
3. Listar clientes por valor
4. Buscar cliente por cédula
5. Cancelar cita
6. Salir
""")
        opcion = input("Seleccione opción: ").strip()
        if opcion == "1":
            consultorio.agregar_cliente()
        elif opcion == "2":
            consultorio.mostrar_resumen()
        elif opcion == "3":
            lista = consultorio.listar_ordenado()
            for c in lista:
                print(f"{c.dni} - {c.nombre_completo} - {c.tipo_cliente} - {c.tipo_servicio} - Valor: ${c.valor_total:,}")
        elif opcion == "4":
            dni = input("Ingrese cédula: ")
            clientes = consultorio.buscar_por_cedula(dni)
            if clientes:
                for c in clientes:
                    print(f"{c.dni} - {c.nombre_completo} - {c.tipo_cliente} - {c.tipo_servicio} - Valor: ${c.valor_total:,}")
            else:
                print("Cliente no encontrado.")
        elif opcion == "5":
            consultorio.eliminar_cita()
        elif opcion == "6":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    menu()
