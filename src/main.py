import os
from typing import List

from class_for_prod import Category, Product, load_data_from_json


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
        for product in category.products:
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
