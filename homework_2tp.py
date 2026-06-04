class Ingredient:
    def __init__(self, name: str, quantity: float, unit: str):
        self.name = name
        self.quantity = quantity
        self.unit = unit
    
    @property
    def quantity(self):
        return self._quantity
    
    @quantity.setter
    def quantity(self, value):
        float_value = float(value)
        if float_value <= 0:
            raise ValueError("Количество должно быть положительным")
        self._quantity = float_value

    def __str__(self):
        return f"{self.name}: {self.quantity} {self.unit}"
    
    def __repr__(self):
        return f"Ingredient('{self.name}', {self.quantity}, '{self.unit}')"
    
    def __eq__(self, other):
        if isinstance(other, Ingredient):
            return self.name == other.name and self.unit == other.unit
        return False
    
class Recipe:
    def __init__(self, title: str, ingredients: list = None):
        self.title = title
        self.ingredients = []
        
        if ingredients is not None:
            for ing in ingredients:
                self.add_ingredient(ing)

    def add_ingredient(self, ingredient: Ingredient):
        ingr = False
        
        for existing in self.ingredients:
            if existing == ingredient:
                existing.quantity += ingredient.quantity
                ingr = True
                break
        
        if not ingr:
            new_ing = Ingredient(ingredient.name, ingredient.quantity, ingredient.unit)
            self.ingredients.append(new_ing)

    @staticmethod
    def is_valid_ratio(ratio):
        if type(ratio) in (int, float):
            if ratio > 0:
                return True
        return False

    def scale(self, ratio: float):
        if not self.is_valid_ratio(ratio):
            raise ValueError("Коэффициент должен быть положительным числом")
        
        new_ingredients = []
        for ing in self.ingredients:
            new_quantity = ing.quantity * ratio
            new_ing = Ingredient(ing.name, new_quantity, ing.unit)
            new_ingredients.append(new_ing)
        
        return Recipe(self.title, new_ingredients)

    def __len__(self):
        return len(self.ingredients)

    def __str__(self):
        result = f"Рецепт: {self.title}\nИнгредиенты:\n"
        for ing in self.ingredients:
            result += f"  - {ing}\n"
        return result.strip()