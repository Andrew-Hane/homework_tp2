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

 