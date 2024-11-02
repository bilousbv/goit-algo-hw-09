# Номінали монет
coins = [50, 25, 10, 5, 2, 1]

def find_coins_greedy(amount):
    """
    Жадібний алгоритм для видачі решти
    Параметри:
        amount (int): сума, яку потрібно видати
    Повертає:
        dict: словник із кількістю монет кожного номіналу
    """
    result = {}
    for coin in coins:
        if amount >= coin:
            count = amount // coin  # Кількість монет поточного номіналу
            amount -= count * coin  # Зменшуємо суму на вартість взятих монет
            result[coin] = count  # Додаємо до результату
    return result

def find_min_coins(amount):
    """
    Динамічний алгоритм для видачі решти з мінімальною кількістю монет
    Параметри:
        amount (int): сума, яку потрібно видати
    Повертає:
        dict: словник із кількістю монет кожного номіналу
    """
    # Ініціалізація масиву мінімальних монет для кожної суми до amount
    min_coins = [float('inf')] * (amount + 1)
    min_coins[0] = 0  # Для суми 0 потрібна 0 монет

    # Зберігаємо монети, які використовуються для досягнення кожної суми
    coin_used = [0] * (amount + 1)

    for i in range(1, amount + 1):
        for coin in coins:
            if i >= coin and min_coins[i - coin] + 1 < min_coins[i]:
                min_coins[i] = min_coins[i - coin] + 1
                coin_used[i] = coin

    # Відновлюємо шлях до оптимальної кількості монет
    result = {}
    while amount > 0:
        coin = coin_used[amount]
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        amount -= coin

    return result

# Приклад використання
rest_amount = 113
print("Жадібний алгоритм:", find_coins_greedy(rest_amount))
print("Алгоритм динамічного програмування:", find_min_coins(rest_amount))