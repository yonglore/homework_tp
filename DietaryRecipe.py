from Recipe import Recipe


class DietaryRecipe(Recipe):
    def __init__(self, title, diet_type, ingredients=None):
        super().__init__(title, ingredients)
        self.diet_type = diet_type

    def scale(self, ratio: float):
        old_scale = super().scale(ratio)
        return DietaryRecipe(old_scale.title, self.diet_type, old_scale.ingredients)

    def __str__(self):
        old_str = super().__str__()
        return old_str.replace(f"Рецепт: {self.title}", f"[{self.diet_type}] Рецепт: {self.title}", 1)
