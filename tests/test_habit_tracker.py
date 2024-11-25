import pytest
import sqlite3
from habit_tracker import HabitTracker
from habit import Habit

@pytest.fixture
def tracker():
    connection = sqlite3.connect(":memory:")  # Use a single in-memory database connection
    tracker = HabitTracker(connection=connection)  # Pass the connection to HabitTracker
    habit = Habit("Exercise", "Daily workout", "daily")  # Create a Habit object
    tracker.add_habit(habit)  # Add the Habit object
    yield tracker
    connection.close()  # Close the connection after the tests

def test_add_habit(tracker):
    habits = tracker.get_current_habits()
    assert len(habits) == 1
    assert habits[0].name == "Exercise"
    assert habits[0].description == "Daily workout"
    assert habits[0].periodicity == "daily"

def test_remove_habit(tracker):
    tracker.remove_habit("Exercise")
    habits = tracker.get_current_habits()
    assert len(habits) == 0
