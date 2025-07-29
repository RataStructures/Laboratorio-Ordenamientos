import os


def execute_pytest_test(test_name):
    commands = [
        f'pytest -v -k "{test_name}"',
        f'py -m pytest -v -k "{test_name}"',
        f'python -m pytest -v -k "{test_name}"',
        f'python3 -m pytest -v -k "{test_name}"',
    ]

    index = 0
    executed_successfully = False

    while index < len(commands) and not executed_successfully:
        cmd = commands[index]
        print(f"Trying: {cmd}")
        return_code = os.system(cmd)
        executed_successfully = return_code == 0
        index += 1


def print_test_options():
    print(" Bienvenido a las pruebas de EDA ".center(80, "="))
    print("1. Todas las estructuras")
    print("2. Listas")
    print("     2.A Lista de arreglos")
    print("     2.B Lista encadenadas")
    print("3. Colas (Queues)")
    print("4. Pilas (Stacks)")
    print("5. Métodos de Ordenamiento")
    print("     5.A Ordenamientos Iterativos")
    print("     5.B Ordenamientos Recursivos")
    print("0. Salir")


def execute_all_tests():
    """Ejecuta todas las pruebas disponibles"""
    execute_list_tests("2")
    execute_queue_tests()
    execute_stack_tests()
    execute_sorting_tests("5")


def execute_list_tests(input_option):
    """Ejecuta pruebas relacionadas con listas"""
    tests_names = []
    if input_option.lower() == "2.a" or input_option == "2":
        tests_names.append("test_array_list")
    if input_option.lower() == "2.b" or input_option == "2":
        tests_names.append("test_single_linked_list")
    for test_name in tests_names:
        execute_pytest_test(test_name)


def execute_sorting_tests(input_option):
    tests_names = []
    if input_option.lower() == "5.a" or input_option == "5":
        tests_names.append("test_iterative_sort_array_list")
        tests_names.append("test_iterative_sort_single_linked_list")
    if input_option.lower() == "5.b" or input_option == "5":
        tests_names.append("test_recursive_sort_array_list")
        tests_names.append("test_recursive_sort_single_linked_list")
    for test_name in tests_names:
        execute_pytest_test(test_name)


def execute_queue_tests():
    """Ejecuta las pruebas de la cola (queue)"""
    execute_pytest_test("test_queue")


def execute_stack_tests():
    """Ejecuta las pruebas de la pila (stack)"""
    execute_pytest_test("test_stack")


if __name__ == "__main__":
    """Menú principal de pruebas"""
    runned = False
    print_test_options()
    input_option = str(input("Ingrese el número de la opción que desea ejecutar: \n"))

    if input_option == "1":
        execute_all_tests()
        runned = True

    if input_option.startswith("2"):
        execute_list_tests(input_option)
        runned = True

    if input_option == "3":
        execute_queue_tests()
        runned = True

    if input_option == "4":
        execute_stack_tests()
        runned = True

    if input_option.startswith("5"):
        execute_sorting_tests(input_option)
        runned = True

    if input_option == "0":
        print("Saliendo de las pruebas")

    elif not runned:
        print("Opción no válida")

    print(" Gracias por ejecutar las pruebas ".center(80, "="))
