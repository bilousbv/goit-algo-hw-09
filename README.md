Порівняння ефективності

1.	Часова складність:
•	Жадібний алгоритм: O(k), де k — кількість номіналів. Жадібний алгоритм проходить через список номіналів лише один раз, що робить його дуже швидким.
•	Динамічне програмування: O(amount * k), де amount — сума для видачі решти, а k — кількість номіналів. Цей алгоритм має більшу часову складність, оскільки він обчислює мінімальну кількість монет для кожного значення від 1 до amount.
2.	Просторова складність:
•	Жадібний алгоритм: O(1), оскільки він зберігає лише кількість монет кожного номіналу в словнику.
•	Динамічне програмування: O(amount) для збереження кількості монет для кожної суми в масиві min_coins та coin_used.
3.	Переваги та недоліки:
•	Жадібний алгоритм: Працює швидше та є оптимальним для конкретного набору монет, де номінали є кратними. Однак, для загальних наборів номіналів він не завжди дає мінімальну кількість монет.
•	Динамічне програмування: Гарантовано знаходить мінімальну кількість монет для будь-якого набору номіналів, але споживає більше пам’яті та часу, особливо для великих значень amount.


Жадібний алгоритм є оптимальним та швидким для набору номіналів, кратних один одному, як у нашій задачі. Він має часову складність O(k) і виконується дуже швидко для великих значень суми, коли номінали дотримуються цього правила. Однак, жадібний алгоритм може давати неоптимальне рішення для загальних випадків, де номінали монет не є кратними.

Алгоритм динамічного програмування, хоч і більш витратний за часом і пам’яттю (O(amount * k)), забезпечує гарантоване знаходження мінімальної кількості монет для будь-якого набору номіналів. Для загальних випадків або нестандартних наборів монет динамічний підхід буде кращим, хоча для дуже великих значень суми його продуктивність може бути повільнішою.

Обидва підходи мають свої переваги, і вибір залежить від вимог системи та властивостей набору монет.