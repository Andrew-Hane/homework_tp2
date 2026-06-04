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
    
class ShoppingList:
    def __init__(self):
        self._items = []

    def add_recipe(self, recipe: Recipe, portions: float):
        if portions <= 0:
            raise ValueError("Количество должно быть положительным")
        
        scaled_recipe = recipe.scale(portions)
        for ing in scaled_recipe.ingredients:
            self._items.append((ing, recipe.title))

    def remove_recipe(self, title: str):
        new_items = []
        for item in self._items:
            if item[1] != title:
                new_items.append(item)
        
        self._items = new_items

    def get_list(self):
        sum_ing = {}
        
        for item in self._items:
            ing = item[0]
            key = (ing.name, ing.unit)
            
            if key in sum_ing:
                sum_ing[key] += ing.quantity
            else:
                sum_ing[key] = ing.quantity
                
        final_list = []
        for key, quantity in sum_ing.items():
            name = key[0]
            unit = key[1]
            final_list.append(Ingredient(name, quantity, unit))
            
        def get_name(ingredient):
            return ingredient.name

        final_list.sort(key=get_name)
        
        return final_list

    def __add__(self, other):
        new_shopping_list = ShoppingList()
        for item in self._items:
            new_shopping_list._items.append(item)
            
        if isinstance(other, ShoppingList):
            for item in other._items:
                new_shopping_list._items.append(item)
                
        return new_shopping_list
    
class DietaryRecipe(Recipe):
    def __init__(self, title: str, diet_type: str, ingredients: list = None):
        super().__init__(title, ingredients)
        self.diet_type = diet_type

    def scale(self, ratio: float):
        scaled_recipe = super().scale(ratio)
        return DietaryRecipe(scaled_recipe.title, self.diet_type, scaled_recipe.ingredients)

    def __str__(self):
        parent_str = super().__str__()
        return f"[{self.diet_type}] {parent_str}"