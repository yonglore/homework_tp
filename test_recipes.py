import pytest

from Ingredient import Ingredient
from Recipe import Recipe
from ShoppingList import ShoppingList


# тесты Ingredient

def test_create_ingredient():
    i = Ingredient("Мука", 500, "г")

    assert i.name == "Мука"
    assert i.quantity == 500.0
    assert i.unit == "г"


def test_ingredient_to_string():
    i = Ingredient("Сахар", 2, "ложки")

    assert str(i) == "Сахар: 2.0 ложки"


def test_ingredients_equal():
    i1 = Ingredient("Молоко", 200, "мл")
    i2 = Ingredient("Молоко", 500, "мл")
    i3 = Ingredient("Молоко", 1, "л")
    i4 = Ingredient("Кефир", 200, "мл")

    assert i1 == i2
    assert i1 != i3
    assert i1 != i4


def test_bad_ingredient_quantity():
    with pytest.raises(ValueError):
        Ingredient("Соль", 0, "г")

    with pytest.raises(ValueError):
        Ingredient("Соль", -3, "г")

    with pytest.raises(ValueError):
        Ingredient("Соль", "много", "г")


# тесты Recipe

def test_create_recipe():
    r = Recipe("Блины")

    assert r.title == "Блины"
    assert r.ingredients == []


def test_add_ingredient_to_recipe():
    r = Recipe("Блины")

    r.add_ingredient(Ingredient("Мука", 200, "г"))
    r.add_ingredient(Ingredient("Яйцо", 2, "шт"))

    assert len(r) == 2


def test_same_ingredient_not_added_twice():
    r = Recipe("Каша")

    r.add_ingredient(Ingredient("Молоко", 100, "мл"))
    r.add_ingredient(Ingredient("Молоко", 200, "мл"))

    assert len(r) == 1
    assert r.ingredients[0].quantity == 300.0


def test_recipe_scale():
    r = Recipe("Чай")
    r.add_ingredient(Ingredient("Сахар", 10, "г"))
    r.add_ingredient(Ingredient("Вода", 200, "мл"))

    new_r = r.scale(2)

    assert new_r.title == "Чай"
    assert new_r.ingredients[0].quantity == 20.0
    assert new_r.ingredients[1].quantity == 400.0
    assert r.ingredients[0].quantity == 10.0


def test_recipe_scale_error():
    r = Recipe("Чай")

    with pytest.raises(ValueError):
        r.scale(0)


# тесты ShoppingList

def test_add_recipe_to_shopping_list():
    r = Recipe("Омлет")
    r.add_ingredient(Ingredient("Яйцо", 2, "шт"))

    s = ShoppingList()
    s.add_recipe(r, 3)

    products = s.get_list()

    assert len(products) == 1
    assert products[0].name == "Яйцо"
    assert products[0].quantity == 6.0


def test_add_recipe_bad_portions():
    r = Recipe("Омлет")
    s = ShoppingList()

    with pytest.raises(ValueError):
        s.add_recipe(r, -1)


def test_remove_recipe():
    r = Recipe("Омлет")
    r.add_ingredient(Ingredient("Яйцо", 2, "шт"))

    s = ShoppingList()
    s.add_recipe(r, 1)
    s.remove_recipe("Омлет")

    assert s.get_list() == []


def test_remove_recipe_that_does_not_exist():
    s = ShoppingList()

    s.remove_recipe("Пицца")

    assert s.get_list() == []


def test_shopping_list_sum_and_sort():
    r1 = Recipe("Салат")
    r1.add_ingredient(Ingredient("Помидор", 2, "шт"))
    r1.add_ingredient(Ingredient("Огурец", 1, "шт"))

    r2 = Recipe("Суп")
    r2.add_ingredient(Ingredient("Помидор", 3, "шт"))

    s = ShoppingList()
    s.add_recipe(r1, 1)
    s.add_recipe(r2, 1)

    products = s.get_list()

    assert products[0].name == "Огурец"
    assert products[1].name == "Помидор"
    assert products[1].quantity == 5.0


def test_two_shopping_lists_plus():
    r1 = Recipe("Чай")
    r1.add_ingredient(Ingredient("Сахар", 10, "г"))

    r2 = Recipe("Кофе")
    r2.add_ingredient(Ingredient("Сахар", 20, "г"))

    s1 = ShoppingList()
    s2 = ShoppingList()
    s1.add_recipe(r1, 1)
    s2.add_recipe(r2, 1)

    s3 = s1 + s2

    assert s3.get_list()[0].quantity == 30.0
    assert s1.get_list()[0].quantity == 10.0
    assert s2.get_list()[0].quantity == 20.0
