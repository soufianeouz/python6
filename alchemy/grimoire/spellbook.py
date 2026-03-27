
def record_spell(spell_name: str, ingredients: str) -> str:
    from .validator import validate_ingredients
    tmp = validate_ingredients(ingredients)
    if "INVALID" in tmp:
        return f"Spell rejected: {spell_name} ({tmp})"
    else:
        return f"Spell recorded: {spell_name} ({tmp})"