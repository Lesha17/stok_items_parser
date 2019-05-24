MATERIAL = ['Материал']
MATERIAL2 = ['Материал рукоятки']

TYPE_MAIN = ['Тип', 'Тип болта']

TYPE1 = ['Тип головки', 'Тип цепи', 'Тип крепления']
TYPE2 = ['Резьба', 'Тип Заклепки', 'Тип анкера', 'Вид зажима', 'Звено']
TYPE3 = ['Наконечник', 'Тип Шплинта', 'Вид декорации']
TYPE_SIZE = ['Размер']

FORM = ['Форма', 'В комплекте']

TYPE_ATTRIBUTES = ['С наружными зубцами', 'Для бетона', 'Универсальный', 'Левая резьба',
                   'Серьга', 'Набор', 'Мелкий шаг резьбы', 'Клипса', 'Изоляции',
                   'Дюймовый крепеж', 'Со скобой', 'Оборудование', 'Высокопрочные',
                   'Хомут-стяжка', 'Антивандальные', 'Внутренняя резьба', 'Бортик',
                   'Для высоких нагрузок', 'Держатель труб', 'Насечка', 'Соединитель цепи',
                   'Устойчивость к УФ', 'С предохраняющей гайкой', 'Спиральная',
                   'Карабин', 'Асимметричный', 'С коушем', 'Открытый',
                   'С роликом', 'Защита от перегрева', 'Регулируемая скорость',
                   'Регулировка глубины строгания', 'Выборка четверти', 'Насадки в комплекте',
                   'Сменные сопла', 'Регулируемая температура', 'Клинья для молотка', 'Трещотка',
                   ]  # Yes / No values

MODEL = ['Модель', 'Стандарт', 'Бита', 'Тип скоб']

COLOR = ['Цвет', 'Полоса']

SIZE1 = ['Длина, мм', 'Длина', 'Высота', 'Длина, м', 'Длина шины, см', 'Минимальный размер, мм',
         'Посадочный квадрат', 'Максимальный захват, мм', 'Размер скобы', 'Размер, мм']

SIZE2 = ['Диаметр, мм', 'Диаметр резьбы, мм', 'Диаметр резьбы, М', 'Диаметр',
         'Минимальный диаметр, мм', 'Максимальный диаметр, мм', 'Диаметр стержня, мм',
         'Глубина строгания, мм', 'Глубина выборки четверти, макс, мм',
         'Максимальная рабочая высота', 'Высота в сложенном состоянии',
         'Ширина', 'Ширина, мм', 'Размер гайки, М', 'Ширина ножа, мм',
         'Максимальный Размер, мм', 'Ширина режущей части, мм']

WEIGHT = ['Вес', 'Объем']
PHYS = ['Грузоподъемность', 'Мощность', 'Число оборотов, макс', 'Рабочая температура, макс, град.',
        'Расход воздуха, л/мин', 'Обороты, макс', 'Производительность, г/мин', 'Время нагрева, мин',
        'Максимальное усилие, Нм', 'Max рабочая нагрузка, кг', 'Максимальная нагрузка',
        'Грузоподъёмность на 1 единицу, кг', 'Грузоподъёмность на пару, кг', 'Допустимый пусковой ток, А',
        ]

COUNT = ['Количество', 'Количество звеньев цепи', 'Количество ступеней', 'Количество ступеней в секции',
         'Количество секций', 'Количество клавиш']

SUPPLIER = ['Производитель']
SUPPLIER_COUNTRY = ['Страна производитель']

PURPOSE = ['Применение']
DESTINATION = ['Назначение']

TARGET_CHARACTERISTICS = {
    'MATERIAL': MATERIAL,
    'MATERIAL2': MATERIAL2,
    'TYPE_MAIN': TYPE_MAIN,
    'TYPE1': TYPE1,
    'TYPE2': TYPE2,
    'TYPE3': TYPE3,
    'TYPE_SIZE': TYPE_SIZE,
    'FORM': FORM,
    'MODEL': MODEL,
    'COLOR': COLOR,
    'SIZE1': SIZE1,
    'SIZE2': SIZE2,
    'WEIGHT': WEIGHT,
    'PHYS': PHYS,
    'COUNT': COUNT,
    'SUPPLIER': SUPPLIER,
    'SUPPLIER_COUNTRY': SUPPLIER_COUNTRY,
    'PURPOSE': PURPOSE,
    'DESTINATION': DESTINATION
}

ORIGNAL_TO_AGGREGATED = { orig : aggr for aggr, chars in TARGET_CHARACTERISTICS.items() for orig in chars }

CHARACTERISTICS = ['Материал', 'Материал рукоятки',
                   'Тип', 'Тип головки', 'Резьба', 'Наконечник', 'Тип Заклепки', 'Тип анкера', 'Тип болта',
                   'Тип Шплинта',
                   'В комплекте', 'Форма', 'Вид декорации', 'Вид зажима', 'Тип цепи', 'Звено', 'Тип крепления',
                   'Размер',
                   'Модель', 'Стандарт', 'Бита', 'Тип скоб',
                   'Цвет', 'Полоса',
                   'Длина, мм', 'Длина', 'Высота', 'Длина, м', 'Длина шины, см', 'Минимальный размер, мм',
                    'Посадочный квадрат', 'Максимальный захват, мм', 'Размер скобы', 'Размер, мм',
                    'Диаметр, мм', 'Диаметр резьбы, мм', 'Диаметр резьбы, М', 'Диаметр',
                    'Минимальный диаметр, мм', 'Максимальный диаметр, мм', 'Диаметр стержня, мм',
                    'Глубина строгания, мм', 'Глубина выборки четверти, макс, мм',
                    'Максимальная рабочая высота', 'Высота в сложенном состоянии',
                    'Ширина', 'Ширина, мм', 'Размер гайки, М', 'Ширина ножа, мм',
                    'Максимальный Размер, мм', 'Ширина режущей части, мм',
                   'Вес', 'Объем',
        'Грузоподъемность', 'Мощность', 'Число оборотов, макс', 'Рабочая температура, макс, град.',
        'Расход воздуха, л/мин', 'Обороты, макс', 'Производительность, г/мин', 'Время нагрева, мин',
        'Максимальное усилие, Нм', 'Max рабочая нагрузка, кг', 'Максимальная нагрузка',
        'Грузоподъёмность на 1 единицу, кг', 'Грузоподъёмность на пару, кг', 'Допустимый пусковой ток, А',
        'Количество', 'Количество звеньев цепи', 'Количество ступеней', 'Количество ступеней в секции',
         'Количество секций', 'Количество клавиш',
        'Производитель', 'Страна производитель', 'Применение', 'Назначение']

ATTRIBUTES = ['С наружными зубцами', 'Для бетона', 'Универсальный', 'Левая резьба',
                   'Серьга', 'Набор', 'Мелкий шаг резьбы', 'Клипса', 'Изоляции',
                   'Дюймовый крепеж', 'Со скобой', 'Оборудование', 'Высокопрочные',
                   'Хомут-стяжка', 'Антивандальные', 'Внутренняя резьба', 'Бортик',
                   'Для высоких нагрузок', 'Держатель труб', 'Насечка', 'Соединитель цепи',
                   'Устойчивость к УФ', 'С предохраняющей гайкой', 'Спиральная',
                   'Карабин', 'Асимметричный', 'С коушем', 'Открытый',
                   'С роликом', 'Защита от перегрева', 'Регулируемая скорость',
                   'Регулировка глубины строгания', 'Выборка четверти', 'Насадки в комплекте',
                   'Сменные сопла', 'Регулируемая температура', 'Клинья для молотка', 'Трещотка']

YES_VALUES = ['да']

NONE_CHAR = 'NONE_CHAR'
