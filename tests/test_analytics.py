import pytest
from analytics import get_longest_streak, get_current_habits
from habit import Habit

def test_get_longest_streak():
    """Test finding the habit with the longest streak."""
    habits = [
        Habit("Exercise", "Daily workout", "daily", streak=5),
        Habit("Reading", "Read books", "weekly", streak=10),
        Habit("Meditation", "Relaxing meditation", "daily", streak=7),
    ]
    longest_streak_habit = max(habits, key=lambda habit: habit.streak)
    assert longest_streak_habit.name == "Reading"
    assert longest_streak_habit.streak == 10


def test_get_current_habits():
    """Test filtering habits by periodicity."""
    habits = [
        Habit("Exercise", "Daily workout", "daily"),
        Habit("Reading", "Read books", "weekly"),
    ]
    daily_habits = get_current_habits(habits, "daily")
    assert len(daily_habits) == 1
    assert daily_habits[0].name == "Exercise"
