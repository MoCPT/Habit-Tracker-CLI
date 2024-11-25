import pytest
from habit import Habit

def test_habit_creation():
    habit = Habit("Exercise", "Daily workout", "daily")
    assert habit.name == "Exercise"
    assert habit.description == "Daily workout"
    assert habit.periodicity == "daily"
    assert habit.streak == 0

def test_mark_complete():
    habit = Habit("Exercise", "Daily workout", "daily")
    habit.mark_complete()
    assert habit.streak == 1
    assert habit.last_completed is not None

def test_reset_streak():
    habit = Habit("Exercise", "Daily workout", "daily")
    habit.mark_complete()
    habit.reset_streak()
    assert habit.streak == 0
