from colorama import Fore, Back, Style
from additional import get_neighbours, update_pole, inputValues

cycle = 0


def print_pole(pole, count):
    if count == 0:
        print("\n  ╔═ Початкове поле:")
    else:
        print(f"  ╔═ Крок {count}:")
    for row in pole:
        print("  ║ ", end="")
        for cell in row:
            if cell == 1:
                print("🔴 ", end="")
            else:
                print("  ", end="")
        print()
    print("  ╚═", end="")


<<<<<<< HEAD
def inputValues(size):
    pole = []
    if input("   1 - ручний\n   2 - автоматичний\nВиберіть метод введення: ") == "1":
        print(f"  => Введіть початкову конфігурацію поля {size}x{size} (1 - жива клітина, 0 - мертва клітина):")
        pole = []
        for i in range(size):
            print("  -> ", end="")
            ryad = list(map(int, input().split()))
            pole.append(ryad)
    else:
        pass #

    return pole


=======
>>>>>>> 51bbbc3722f32259a55e3fc36c48a502182f678b
def start_game():
    global cycle
    count = 0

    print(" " * 23 + Fore.LIGHTYELLOW_EX + "\033[1m｡☆✼★━━━━━━━━━━━━►▬ Вітаємо! ▬◄━━━━━━━━━━━━★✼☆｡\n" + Fore.RESET + Fore.RED +
          " " * 32 + "▓▓" + Fore.RESET + " Це гра про життя клітин " + Fore.GREEN + "▓▓" + Fore.CYAN + """
    ╔──────────────────────────────────── ¤ Правила ¤ ───────────────────────────────────╗
    ║ 1. Клітина вмирає якщо вона має менше двох, або більше трьох живих клітин сусідів; ║
    ║ 2. Жива клітина, яка має дві або три живі клітин сусідів, продовжує жити;          ║
    ║ 3. Мертва клітина, у якій рівно три живі клітини серед сусідів, стає живою.        ║
    ╚═─────────────────────────────────── ¤¤¤¤¤¤¤¤¤¤¤ ──────────────────────────────────═╝
    \033[0m""" + Fore.RESET)

    size = int(input("  =───────> Введіть розмір поля: "))
<<<<<<< HEAD
=======
    print(
        f"  => Введіть початкову конфігурацію поля {size}x{size} (1 - жива клітина, 0 - мертва клітина):")
>>>>>>> 51bbbc3722f32259a55e3fc36c48a502182f678b

    pole = inputValues(size)

    print_pole(pole, count)
    print(' Для наступного кроку натисніть Enter. Для виходу введіть "0"')

    boards = []

    while input() != "0":
        count += 1
        boards.append(pole)
        pole = update_pole(pole)

        print_pole(pole, count)

        if all(cell == 0 for row in pole for cell in row):
            print(" Гру завершено! На полі немає живих клітин.")
            break
        elif pole in boards:
            print(" Гру завершено! На полі немає змін.")
            break

    print(Fore.CYAN+f"\n  Завершених життєвих циклів: " +
          Fore.GREEN+f"{cycle}"+Fore.RESET)


start_game()
