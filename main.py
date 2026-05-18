import random
import copy
from visualizer import setup_figure, finish, draw
from algorithms.bubble import bubble_sort
from algorithms.selection import selection_sort
from algorithms.insertion import insertion_sort
from stats import print_stats


while True:
    try:
        n = int(input("Введите количество элементов (от 2 до 100): "))
        if n < 2 or n > 100:
            print("Число должно быть от 2 до 100, попробуй снова.")
        else:
            break
    except ValueError:
        print("Ошибка: введи целое число!")


print("\nВыбери алгоритм:")
print("1 — Пузырёк")
print("2 — Выбор")
print("3 — Вставки")
print("4 — Все три")
choice = input("Твой выбор (1/2/3/4): ")


original = random.sample(range(1, 101), n)


results = {}

if choice in ("1", "4"):
    arr = copy.copy(original)
    setup_figure()
    steps = bubble_sort(arr, draw)
    finish()
    results["Пузырёк"] = steps

if choice in ("2", "4"):
    arr = copy.copy(original)
    setup_figure()
    steps = selection_sort(arr, draw)
    finish()
    results["Выбор"] = steps

if choice in ("3", "4"):
    arr = copy.copy(original)
    setup_figure()
    steps = insertion_sort(arr, draw)
    finish()
    results["Вставки"] = steps

# --- Блок 5: Статистика ---
if results:
    print_stats(n, results)