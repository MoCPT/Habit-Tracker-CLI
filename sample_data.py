from datetime import datetime, timedelta
from habit import Habit

def get_sample_habits():
    """Create and return a list of 5 predefined habits with sample tracking data."""
    habits = [
        Habit("Exercise", "Daily exercise routine", "daily"),
        Habit("Read", "Read 20 minutes daily", "daily"),
        Habit("Meditate", "Daily meditation session", "daily"),
        Habit("Weekly Cleaning", "Weekly house cleaning", "weekly"),
        Habit("Groceries", "Buy groceries once a week", "weekly")
    ]
    
    # Generate sample tracking data for 4 weeks
    for habit in habits:
        for days_ago in range(28):  # Generate 28 days (4 weeks) of data
            habit.last_completed = datetime.now() - timedelta(days=days_ago)
            habit.mark_complete()  # Update streak based on completion

    return habits
