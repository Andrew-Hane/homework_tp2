from homework_2tp import Ingredient, Recipe
import pytest

def test_ingredient_init():
    ing = Ingredient("Мука", 500.0, "г")
    assert ing.name == "Мука"
    assert ing.quantity == 500.0
    assert ing.unit == "г"

def test_ingredient_str():
    ing = Ingredient("Мука", 500.0, "г")
    assert str(ing) == "Мука: 500.0 г"

def test_ingredient_eq_quantity():
    ing1 = Ingredient("Мука", 100.0, "г")
    ing2 = Ingredient("Мука", 200.0, "г")
    
    assert ing1 == ing2

def test_ingredient_eq_name():
    ing1 = Ingredient("Мука", 100.0, "г")
    ing2 = Ingredient("Сахар", 100.0, "г")
    
    assert ing1 != ing2

def test_ingredient_eq_unit():
    ing1 = Ingredient("Мука", 1.0, "кг")
    ing2 = Ingredient("Мука", 1000.0, "г")
    
    assert ing1 != ing2

def test_recipe_init():
    ing1 = Ingredient("Гречневая мука", 600.0, "г")
    recipe = Recipe("Грешники", [ing1])

    assert recipe.title == "Грешники"
    assert len(recipe.ingredients) == 1
    assert recipe.ingredients[0].name == "Гречневая мука"
    assert recipe.ingredients[0].quantity == 600.0

def test_recipe_add_new_ingredient():
    recipe = Recipe("Грешники")
    ing = Ingredient("Гречневая мука", 200.0, "г")
    recipe.add_ingredient(ing)

    assert len(recipe.ingredients) == 1
    assert recipe.ingredients[0].name == "Гречневая мука"

def test_recipe_add_sum_ingredient():
    recipe = Recipe("Грешники")
    ing1 = Ingredient("Гречневая мука", 900.0, "г")
    ing2 = Ingredient("Гречневая мука", 200.0, "г")
    recipe.add_ingredient(ing1)
    recipe.add_ingredient(ing2)
    
    assert len(recipe.ingredients) == 1
    assert recipe.ingredients[0].quantity == 1100.0

def test_recipe_scale():
    ing = Ingredient("Гречневая мука", 600.0, "г")
    recipe = Recipe("Грешники", [ing])
    scaled_recipe = recipe.scale(2.0)
    
    assert scaled_recipe is not recipe
    assert scaled_recipe.ingredients[0].quantity == 1200.0
    assert recipe.ingredients[0].quantity == 600.0

def test_recipe_scale_error():
    recipe = Recipe("Грешники")
    with pytest.raises(ValueError):
        recipe.scale(-1)
        
    with pytest.raises(ValueError):
        recipe.scale(0)

def test_recipe_len():
    recipe = Recipe("Грешники")
    recipe.add_ingredient(Ingredient("Гречневая мука", 666.0, "г"))
    recipe.add_ingredient(Ingredient("Вода", 333.0, "мл"))
    recipe.add_ingredient(Ingredient("Вода", 333.0, "мл"))
    
    assert len(recipe) == 2

 
