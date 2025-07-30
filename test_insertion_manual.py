#!/usr/bin/env python3

import sys

sys.path.append(".")

from DataStructures.List import single_linked_list as sll

order_function = sll.insertion_sort


def sort_criteria_increasing(a, b):
    return a < b


def print_list(my_list):
    elements = []
    for i in range(sll.size(my_list)):
        elements.append(sll.get_element(my_list, i))
    return elements


def test_insertion_sort():
    print("=== Probando insertion_sort ===\n")

    # Caso 1: Lista desordenada
    print("1. Lista desordenada [5, 2, 8, 1, 9]:")
    lista1 = sll.new_list()
    for elem in [5, 2, 8, 1, 9]:
        lista1 = sll.add_last(lista1, elem)

    print(f"   Antes:  {print_list(lista1)}")
    lista1_sorted = order_function(lista1, sort_criteria_increasing)
    print(f"   Después: {print_list(lista1_sorted)}")
    print()

    # Caso 2: Lista ya ordenada
    print("2. Lista ya ordenada [1, 2, 3, 4, 5]:")
    lista2 = sll.new_list()
    for elem in [1, 2, 3, 4, 5]:
        lista2 = sll.add_last(lista2, elem)

    print(f"   Antes:  {print_list(lista2)}")
    lista2_sorted = order_function(lista2, sort_criteria_increasing)
    print(f"   Después: {print_list(lista2_sorted)}")
    print()

    # Caso 3: Lista con elementos duplicados
    print("3. Lista con duplicados [3, 1, 4, 1, 5, 9, 2, 6, 5]:")
    lista3 = sll.new_list()
    for elem in [3, 1, 4, 1, 5, 9, 2, 6, 5]:
        lista3 = sll.add_last(lista3, elem)

    print(f"   Antes:  {print_list(lista3)}")
    lista3_sorted = order_function(lista3, sort_criteria_increasing)
    print(f"   Después: {print_list(lista3_sorted)}")
    print()

    # Caso 4: Lista con un solo elemento
    print("4. Lista con un elemento [42]:")
    lista4 = sll.new_list()
    lista4 = sll.add_last(lista4, 42)

    print(f"   Antes:  {print_list(lista4)}")
    lista4_sorted = order_function(lista4, sort_criteria_increasing)
    print(f"   Después: {print_list(lista4_sorted)}")
    print()

    # Caso 5: Lista vacía
    print("5. Lista vacía []:")
    lista5 = sll.new_list()

    print(f"   Antes:  {print_list(lista5)}")
    lista5_sorted = order_function(lista5, sort_criteria_increasing)
    print(f"   Después: {print_list(lista5_sorted)}")


if __name__ == "__main__":
    test_insertion_sort()
