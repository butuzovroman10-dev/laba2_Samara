import random
import datetime
import os
from linked_list import LinkedList, Node

# ============================================================
# Вариант 14: Фантастический зоопарк
# ============================================================

# Константы
SPECIES_LIST = ["Дракон", "Грифон", "Единорог", "Феникс", "Кентавр", 
                "Минотавр", "Василиск", "Химера", "Гидра", "Сфинкс"]
DANGER_LEVELS = list(range(1, 11))
WEIGHT_RANGES = {
    "Дракон": (500, 2000),
    "Грифон": (200, 800),
    "Единорог": (100, 400),
    "Феникс": (50, 150),
    "Кентавр": (300, 700),
    "Минотавр": (400, 900),
    "Василиск": (100, 300),
    "Химера": (250, 600),
    "Гидра": (800, 2500),
    "Сфинкс": (300, 800)
}

def clear_screen():
    """Очистка экрана для Windows и Linux/Mac"""
    os.system('cls' if os.name == 'nt' else 'clear')

def wait_for_screenshot(step_name):
    """Останавливает программу и ждет нажатия Enter после скриншота"""
    current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print("\n" + "=" * 60)
    print(f"ЭТАП: {step_name}")
    print(f"ТЕКУЩЕЕ ВРЕМЯ: {current_time}")
    print("=" * 60)
    print("\nСДЕЛАЙ СКРИНШОТ ЭТОГО ЭКРАНА")
    print("(Убедись, что время в правом нижнем углу видно)")
    print("\nПосле того как скриншот сделан, нажми Enter для продолжения...")
    input()
    clear_screen()

def generate_creature(index):
    """Генератор одного фантастического существа"""
    species = random.choice(SPECIES_LIST)
    danger = random.choice(DANGER_LEVELS)
    
    # Генерация массы в зависимости от вида
    min_w, max_w = WEIGHT_RANGES[species]
    weight = round(random.uniform(min_w, max_w), 1)
    
    # Гарантируем, что хотя бы одно существо - Дракон (для варианта)
    if index == 3:  # Сделаем дракона на 4-й позиции
        species = "Дракон"
        danger = 9
        weight = 1800.5
    
    return {
        "вид": species,
        "опасность": danger,
        "масса": weight
    }

def print_creature(creature):
    """Вывод одного существа"""
    return f"{creature['вид']} (ур.опасности: {creature['опасность']}, масса: {creature['масса']} кг)"

def print_list_with_indexes(lst, title):
    """Вывод списка с порядковыми номерами"""
    print(f"\n{title}:")
    if not lst:
        print("  Список пуст")
        return
    for idx, c in enumerate(lst, 1):
        print(f"  {idx}. {print_creature(c)}")

# ============================================================
# Основная программа
# ============================================================

def main():
    clear_screen()
    print("=" * 60)
    print("ЛАБОРАТОРНАЯ РАБОТА №2")
    print("Вариант 14: Фантастический зоопарк")
    print("=" * 60)
    print("\nПрограмма будет останавливаться после каждого этапа,")
    print("чтобы вы могли сделать скриншот с текущим временем.")
    print("\nНажмите Enter для начала работы...")
    input()
    clear_screen()

    # ============================================================
    # ЭТАП 1: Создание исходного списка
    # ============================================================
    wait_for_screenshot("1. Исходный список существ")

    zoo = LinkedList()
    print("Генерация 12 фантастических существ...")
    for i in range(12):
        creature = generate_creature(i)
        zoo.append(creature)
    
    initial_list = zoo.to_list()
    print_list_with_indexes(initial_list, "ИСХОДНЫЙ СОСТАВ ЗООПАРКА")
    
    # Подсчет статистики для исходного списка
    dragons = sum(1 for c in initial_list if c["вид"] == "Дракон")
    print(f"\nСтатистика исходного списка:")
    print(f"  • Всего существ: {len(initial_list)}")
    print(f"  • Драконов: {dragons}")
    print(f"  • Средняя опасность: {sum(c['опасность'] for c in initial_list)/len(initial_list):.1f}")
    print(f"  • Средняя масса: {sum(c['масса'] for c in initial_list)/len(initial_list):.1f} кг")

    # ============================================================
    # ЭТАП 2: Поиск Дракона и вставка АЛЬФА-ДРАКОНА
    # ============================================================
    wait_for_screenshot("2. После вставки АЛЬФА-ДРАКОНА")
    
    print("Поиск первого Дракона...")
    current = zoo.head
    position = 1
    dragon_found = False
    
    while current:
        if current.data["вид"] == "Дракон":
            print(f"  Найден Дракон на позиции {position}: {print_creature(current.data)}")
            dragon_found = True
            
            # Создаем АЛЬФА-ДРАКОНА
            alpha_dragon = {
                "вид": "АЛЬФА-ДРАКОН",
                "опасность": 10,
                "масса": 5000.0
            }
            
            # Вставка после текущего узла
            new_node = Node(alpha_dragon)
            new_node.next = current.next
            current.next = new_node
            print("  Вставлен АЛЬФА-ДРАКОН (опасность 10, масса 5000 кг)")
            break
        current = current.next
        position += 1
    
    if not dragon_found:
        print("  Дракон не найден! Вставка в конец списка...")
        alpha_dragon = {
            "вид": "АЛЬФА-ДРАКОН",
            "опасность": 10,
            "масса": 5000.0
        }
        zoo.append(alpha_dragon)
    
    after_insert_list = zoo.to_list()
    print_list_with_indexes(after_insert_list, "СОСТАВ ПОСЛЕ ВСТАВКИ")

    # ============================================================
    # ЭТАП 3: Удаление безопасных существ (опасность < 3)
    # ============================================================
    wait_for_screenshot("3. После удаления безопасных существ")
    
    print("Удаление безопасных существ (уровень опасности < 3)...")
    deleted_count = 0
    
    # Обработка головы списка
    while zoo.head and zoo.head.data["опасность"] < 3:
        print(f"  Удалено из головы: {print_creature(zoo.head.data)}")
        zoo.head = zoo.head.next
        deleted_count += 1
    
    # Удаление в середине и конце
    current = zoo.head
    while current and current.next:
        if current.next.data["опасность"] < 3:
            print(f"  Удалено: {print_creature(current.next.data)}")
            current.next = current.next.next
            deleted_count += 1
        else:
            current = current.next
    
    print(f"\nУдалено существ: {deleted_count}")
    
    after_delete_list = zoo.to_list()
    print_list_with_indexes(after_delete_list, "СОСТАВ ПОСЛЕ УДАЛЕНИЯ")

    # ============================================================
    # ЭТАП 4: Расчет средней массы и реверсивный перебор
    # ============================================================
    wait_for_screenshot("4. Финальный развернутый список")
    
    # Расчет средней массы опасных особей
    remaining = zoo.to_list()
    if remaining:
        avg_weight = sum(c["масса"] for c in remaining) / len(remaining)
        print(f"\nСРЕДНЯЯ МАССА ОПАСНЫХ ОСОБЕЙ: {avg_weight:.1f} кг")
        
        # Дополнительная статистика
        print(f"\nДетальная статистика:")
        print(f"  • Всего опасных существ: {len(remaining)}")
        print(f"  • Суммарная масса: {sum(c['масса'] for c in remaining):.1f} кг")
        print(f"  • Максимальная масса: {max(c['масса'] for c in remaining)} кг")
        print(f"  • Минимальная масса: {min(c['масса'] for c in remaining)} кг")
    else:
        print("\nНет опасных особей для расчета средней массы")
    
    # Реверсивный перебор списка
    print("\nРЕВЕРСИВНЫЙ ПЕРЕБОР (разворот связей)...")
    
    # Разворот списка
    prev = None
    current = zoo.head
    steps = 0
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
        steps += 1
    zoo.head = prev
    print(f"  Список развернут ({steps} узлов обработано)")
    
    reversed_list = zoo.to_list()
    print_list_with_indexes(reversed_list, "ФИНАЛЬНЫЙ РАЗВЕРНУТЫЙ СПИСОК")

    # ============================================================
    # Классификация по уровням угрозы
    # ============================================================
    print("\n" + "=" * 60)
    print("КЛАССИФИКАЦИЯ ПО УРОВНЯМ УГРОЗЫ")
    print("=" * 60)
    
    threat_levels = {
        "Низкая (3-4)": [],
        "Средняя (5-7)": [],
        "Высокая (8-10)": []
    }
    
    for c in reversed_list:
        if 3 <= c["опасность"] <= 4:
            threat_levels["Низкая (3-4)"].append(c)
        elif 5 <= c["опасность"] <= 7:
            threat_levels["Средняя (5-7)"].append(c)
        elif 8 <= c["опасность"] <= 10:
            threat_levels["Высокая (8-10)"].append(c)
    
    for level, creatures in threat_levels.items():
        print(f"\n{level}: {len(creatures)} существ")
        if creatures:
            avg_danger = sum(c["опасность"] for c in creatures) / len(creatures)
            avg_weight = sum(c["масса"] for c in creatures) / len(creatures)
            print(f"  • Средняя опасность: {avg_danger:.1f}")
            print(f"  • Средняя масса: {avg_weight:.1f} кг")
            for c in creatures[:3]:  # Показываем максимум 3 примера
                print(f"  • {print_creature(c)}")
            if len(creatures) > 3:
                print(f"  • ... и еще {len(creatures) - 3} существ")

    # ============================================================
    # Итоговый вывод
    # ============================================================
    print("\n" + "=" * 60)
    print("ИТОГОВЫЙ РЕЗУЛЬТАТ РАБОТЫ")
    print("=" * 60)
    print(f"\nНачальное количество существ: 12")
    print(f"После вставки АЛЬФА-ДРАКОНА: {len(after_insert_list)}")
    print(f"После удаления безопасных: {len(after_delete_list)}")
    print(f"В финальном развернутом списке: {len(reversed_list)}")
    
    if remaining:
        print(f"\nСредняя масса опасных особей: {avg_weight:.1f} кг")
    
    print("\n" + "=" * 60)
    print("РАБОТА ПРОГРАММЫ ЗАВЕРШЕНА")
    print("Все 4 скриншота должны быть сделаны")
    print("=" * 60)
    
    print("\nНажмите Enter для выхода...")
    input()

if __name__ == "__main__":
    main()