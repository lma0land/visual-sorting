def print_stats(n, results):
  

    print("=" * 44)
    print(f"  Сравнение алгоритмов (N = {n})")
    print("=" * 44)
    print(f"{'Алгоритм':<20} {'Шагов (сравнений)'}")
    print("-" * 44)

    for name, steps in results.items():
        print(f"{name:<20} {steps}")   

    print("=" * 44)


    winner = min(results, key=results.get)
    print(f"Победитель по шагам: {winner}")
    print("=" * 44)