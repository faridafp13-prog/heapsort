def radix_sort(arr):
    if not arr:
        return []
    negativos = [-x for x in arr if x < 0]
    positivos = [x for x in arr if x >= 0]

    def _radix_positivos(nums):
        if not nums:
            return []
        max_num = max(nums)
        exp = 1
        res = nums.copy()
        while max_num // exp > 0:
            salida = [0] * len(res)
            conteo = [0] * 10
            for num in res:
                indice = (num // exp) % 10
                conteo[indice] += 1
            for i in range(1, 10):
                conteo[i] += conteo[i - 1]
            for i in range(len(res) - 1, -1, -1):
                indice = (res[i] // exp) % 10
                salida[conteo[indice] - 1] = res[i]
                conteo[indice] -= 1
            res = salida
            exp *= 10
        return res

    neg_ordenados = [-x for x in reversed(_radix_positivos(negativos))]
    pos_ordenados = _radix_positivos(positivos)
    return neg_ordenados + pos_ordenados


def menu():
    while True:
        print("\n=== MENU RADIX SORT ===")
        print("1. Ordenar numeros con Radix Sort")
        print("2. Salir")

        opcion = input("Elige una opcion (1-2): ").strip()

        if opcion == "2":
            print("Saliendo del programa...")
            break

        if opcion != "1":
            print("Opcion no valida. Intenta de nuevo.")
            continue

        try:
            cantidad = int(input("Ingresa la cantidad de numeros: "))
            if cantidad <= 0:
                print("La cantidad debe ser mayor a 0.")
                continue

            numeros = []
            for i in range(cantidad):
                num = int(input(f"Ingresa el numero {i + 1}: "))
                numeros.append(num)
        except ValueError:
            print("Error: Ingresa solo numeros enteros.")
            continue

        print("Lista original:", numeros)
        print("Lista ordenada (Radix Sort):", radix_sort(numeros))


if __name__ == "__main__":
    menu()