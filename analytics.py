def get_streak_for_habit(tracker, habit_name):
    """
    Returns the streak for a specific habit by name.

    Parameters:
    - tracker (HabitTracker): The HabitTracker instance to query.
    - habit_name (str): The name of the habit to find.

    Returns:
    - int: The streak count for the specified habit, or 0 if not found.
    """
    habits = tracker.get_current_habits()
    for habit in habits:
        if habit.name == habit_name:
            return habit.streak
    return 0  # Return 0 if the habit is not found

def get_longest_streak(tracker):
    """
    Finds the habit with the longest streak.

    Parameters:
    - tracker (HabitTracker): The HabitTracker instance to query.

    Returns:
    - Habit: The Habit object with the longest streak, or None if no habits exist.
    """
    habits = tracker.get_current_habits()  # Fetch all current habits
    if not habits:
        return None
    return max(habits, key=lambda habit: habit.streak)  # Return the habit with the longest streak
