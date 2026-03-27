import alchemy.transmutation.basic
import alchemy.transmutation.advanced
import alchemy.transmutation


print()
print("=== Pathway Debate Mastery ===\n")
print("Testing Absolute Imports (from basic.py):")
print(f"lead_to_gold(): {alchemy.transmutation.basic.lead_to_gold()}")
print(f"stone_to_gem(): {alchemy.transmutation.basic.stone_to_gem()}")
print()

print("Testing Relative Imports (from advanced.py):")
print(f"philosophers_stone(): {alchemy.transmutation.advanced.philosophers_stone()}")
print(f"elixir_of_life(): {alchemy.transmutation.advanced.elixir_of_life()}")
print()

print("Testing Package Access:")
print(f"alchemy.transmutation.lead_to_gold(): {alchemy.transmutation.lead_to_gold()}")
print(f"alchemy.transmutation.philosophers_stone(): {alchemy.transmutation.philosophers_stone()}")
print()

print("Both pathways work! Absolute: clear, Relative: concise")