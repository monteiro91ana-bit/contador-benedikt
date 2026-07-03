def mostrar_menu():
    print("\n--- CONTADOR contador---")
    print(f"  Valor actual: {contador}")
    print("  [1] Incrementar (+1)")
    print("  [2] Restablecer (0)")
    print("  [3] Establecer valor inicial")
    print("  [4] Salir")


contador = 0

while True:
    mostrar_menu()
    opcion = input("\nElige una opción: ").strip()

    if opcion == "1":
        contador += 1
        print(f"✓ Incrementado → {contador}")
    elif opcion == "2":
        contador = 0
        print("✓ Restablecido a 0")
    elif opcion == "3":
        entrada = input("Ingresa el valor inicial: ").strip()
        if entrada.lstrip("-").isdigit():
            contador = int(entrada)
            print(f"✓ Valor establecido → {contador}")
        else:
            print("✗ Entrada inválida. Ingresa un número entero.")
    elif opcion == "4":
        print("¡Hasta luego!")
        break
    else:
        print("✗ Opción no válida. Elige entre 1 y 4.")
