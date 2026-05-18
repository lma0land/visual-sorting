import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# Настройки цветов
COLOR_DEFAULT = '#4C9BE8'   # синий — обычный столбец
COLOR_COMPARE = '#E85C4C'   # красный — сравниваемые элементы
COLOR_SORTED  = '#4CE87A'   # зелёный — элемент на своём месте

# Задержка между кадрами (секунды)
DELAY = 0.05

def draw(array, comparing=[], sorted_indices=[], title="", step_count=0):
    """
    Рисует текущее состояние массива в виде столбчатой диаграммы.

    Параметры:
    - array          : текущий список чисел
    - comparing      : индексы элементов, которые сейчас сравниваются (красный)
    - sorted_indices : индексы элементов, уже стоящих на месте (зелёный)
    - title          : название алгоритма
    - step_count     : номер текущего шага
    """
    plt.cla()  # очищаем предыдущий кадр

    n = len(array)

    # Назначаем цвет каждому столбцу
    colors = []
    for i in range(n):
        if i in comparing:
            colors.append(COLOR_COMPARE)
        elif i in sorted_indices:
            colors.append(COLOR_SORTED)
        else:
            colors.append(COLOR_DEFAULT)

    # Рисуем столбцы
    bars = plt.bar(range(n), array, color=colors, edgecolor='white', linewidth=0.5)

    # Подписи значений над столбцами (только если элементов немного)
    if n <= 20:
        for bar, val in zip(bars, array):
            plt.text(
                bar.get_x() + bar.get_width() / 2,
                bar.get_height() + 0.5,
                str(val),
                ha='center', va='bottom',
                fontsize=8, color='white'
            )

    # Заголовок и подпись шагов
    plt.title(f'{title}', fontsize=14, color='white', pad=10)
    plt.xlabel(f'Шагов: {step_count}', fontsize=11, color='#aaaaaa')

    # Убираем лишние оси
    plt.xticks([])
    plt.yticks([])
    plt.ylim(0, max(array) + 10)

    # Легенда
    legend = [
        mpatches.Patch(color=COLOR_DEFAULT, label='Обычный'),
        mpatches.Patch(color=COLOR_COMPARE, label='Сравнение'),
        mpatches.Patch(color=COLOR_SORTED,  label='На месте'),
    ]
    plt.legend(handles=legend, loc='upper left',
               facecolor='#2a2a2a', edgecolor='#555', labelcolor='white', fontsize=9)

    plt.pause(DELAY)  # пауза — именно она создаёт анимацию


def setup_figure(title="Визуальная сортировка"):
    """Создаёт и настраивает окно matplotlib."""
    plt.figure(figsize=(12, 6))
    plt.gcf().patch.set_facecolor('#1a1a2e')   # тёмный фон окна
    plt.gca().set_facecolor('#16213e')          # тёмный фон графика
    plt.ion()  # включаем интерактивный режим (нужен для анимации)
    plt.tight_layout()


def finish():
    """Вызывается в конце — оставляет окно открытым до закрытия пользователем."""
    plt.ioff()
    plt.show()