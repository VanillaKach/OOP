import os
from typing import List

from src.category import Category
from src.product import Product
from src.utils import load_data_from_json

# -------------------------------------------------- homework 14.1 -----------------------------------------------------


def main() -> None:
    # Укажите путь к файлу products.json
    file_path = "../data/products.json"

    # Проверка наличия файла
    if not os.path.exists(file_path):
        print(f"Ошибка: Файл не найден по пути: {file_path}")
        return

    # Загружаем категории и продукты из JSON файла
    categories: List[Category] = load_data_from_json(file_path)

    # Перебираем и выводим информацию о категориях и продуктах
    for category in categories:
        print(f"Категория: {category.name}, Описание: {category.description}")
        for (
            product
        ) in (
            category.products
        ):  # category.products теперь возвращает список объектов Product
            print(
                f"  Продукт: {product.name}, Цена: {product.price}, Количество: {product.quantity}"
            )

    # Выводим общее количество категорий и продуктов
    print("Общее количество категорий:", Category.category_count)
    print("Общее количество товаров:", Category.product_count)

    # Пример создания продуктов и категорий вручную
    product1 = Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )

    print(category1.name == "Смартфоны")
    print(category1.description)
    print(len(category1.products))
    print(category1.category_count)
    print(category1.product_count)

    product4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    category2 = Category(
        "Телевизоры",
        "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
        [product4],
    )

    print(category2.name)
    print(category2.description)
    print(len(category2.products))
    print(category2.products)

    print("Общее количество категорий:", Category.category_count)
    print("Общее количество товаров:", Category.product_count)


if __name__ == "__main__":
    main()

# -------------------------------------------------- homework 14.2 -----------------------------------------------------


if __name__ == "__main__":
    product1 = Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )

    print(category1.products)

    product4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    print(f"Тип product4: {type(product4)}")  # Отладочное сообщение
    category1.add_product(product4)  # Убедитесь, что product4 - это экземпляр Product

    print(category1.products)
    print(category1.product_count)

    new_product = Product.new_product(
        {
            "name": "Samsung Galaxy S23 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 180000.0,
            "quantity": 5,
        }
    )

    print(new_product.name)
    print(new_product.description)
    print(new_product.price)
    print(new_product.quantity)

    new_product.price = 800  # Понижение цены
    print(new_product.price)

    new_product.price = -100  # Попытка установить отрицательную цену
    print(new_product.price)

    new_product.price = 0  # Попытка установить нулевую цену
    print(new_product.price)


# -------------------------------------------------- homework 15.1 -----------------------------------------------------


if __name__ == "__main__":
    product1 = Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    print(str(product1))
    print(str(product2))
    print(str(product3))

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )

    print(str(category1))

    print(category1.products)

    print(product1 + product2)  # Сложение стоимости
    print(product1 + product3)
    print(product2 + product3)
