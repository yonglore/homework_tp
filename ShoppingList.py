from Recipe import Recipe
from Ingredient import Ingredient


class ShoppingList:
    def __init__(self):
        self._items = []

    def add_recipe(self, recipe: Recipe, portions: float):
        if portions <= 0:
            raise ValueError("Количество порций должно быть положительным числом")

        for elem in recipe.scale(portions).ingredients:
            self._items.append((elem, recipe.title))

    def remove_recipe(self, title: str):
        res_items = []
        for elem in self._items:
            if elem[1] != title:
                res_items.append(elem)

        self._items = res_items

    def get_list(self):
        items_dict = {}

        for ingredient, title in self._items:
            key = (ingredient.name, ingredient.unit)
            items_dict[key] = items_dict.get(key, 0) + ingredient.quantity

        res = []
        for (name, unit), quantity in items_dict.items():
            res.append(Ingredient(name, unit, quantity))

        res.sort(key=lambda x: x.name)
        return res

    def __add__(self, other: ShoppingList):
        res = ShoppingList()
        res._items = list(self._items) + list(other._items)
        return res
