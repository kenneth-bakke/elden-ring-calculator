from logging import error
from functools import reduce
from math import *

# runes needed = (0.02 * level ^ 3) + (3.06 * level ^ 2) + (105.6 * level) - 895
one_through_eleven = {
  1: 673,
  2: 689,
  3: 706,
  4: 723,
  5: 740,
  6: 757,
  7: 775,
  8: 793,
  9: 811,
  10: 829,
  11: 847
}

def calculate_runes_needed_by_level(current_level, runes_held, goal_level):
  if current_level > goal_level:
    raise ValueError(f'Current level ({current_level}) cannot be more than goal level ({goal_level})')
  if current_level == goal_level:
    return 0

  runes_needed_until_twelve = 0
  runes_needed_for_goal_level = 0
  level_diff = goal_level - current_level

  if current_level < 12:
    try:
      runes_needed_until_twelve = calculate_up_to_eleven(current_level)
      current_level = 12
    except(ValueError):
      runes_needed_until_twelve = 0
      current_level = 12


  if goal_level <= 12:
    return runes_needed_until_twelve - runes_held

  for i in range(level_diff):
    current_level += 1
    level = (((current_level ** 3) * .02) + ((current_level ** 2) * 3.06) + (105.6 * current_level) - 895)
    runes_needed_for_goal_level += floor(level)

  total_runes_needed = runes_needed_for_goal_level + runes_needed_until_twelve - runes_held
  return floor(total_runes_needed)

def calculate_up_to_eleven(current_level=None):
  if not current_level or type(current_level) is not int or current_level >= 12:
    raise ValueError(f'LevelError: Not an acceptable level\nlevel {current_level} must be of type int, above 0 and less than 12\n')
  all_early_rune_quantities = list(one_through_eleven.values())
  start_index = current_level - 1 # Off-by-one fix
  necessary_levels = all_early_rune_quantities[start_index:]
  runes_needed_until_twelve = reduce(lambda a, b: a+b, necessary_levels)
  return runes_needed_until_twelve


actual = calculate_runes_needed_by_level(12, 0, 15)
expected = 3721
if actual == expected:
  print(f'PASS:::Actual matches expected\nActual: {actual}\nExpected: {expected}\n')
else:
  print(f'FAIL:::Actual does not match expected\nActual: {actual}\nExpected: {expected}\nDiff: {abs(actual-expected)}\n')

actual = calculate_runes_needed_by_level(12, 0, 20)
expected = 14329
if actual == expected:
  print(f'PASS:::Actual matches expected\nActual: {actual}\nExpected: {expected}\n')
else:
  print(f'FAIL:::Actual does not match expected\nActual: {actual}\nExpected: {expected}\nDiff: {abs(actual-expected)}\n')

actual = calculate_up_to_eleven(1)
expected = 8343
if actual == expected:
  print(f'PASS:::Actual matches expected\nActual: {actual}\nExpected: {expected}\n')
else:
  print(f'FAIL:::Actual does not match expected\nActual: {actual}\nExpected: {expected}\nDiff: {abs(actual-expected)}\n')