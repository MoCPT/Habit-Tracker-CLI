from datetime import datetime

class Habit:
    def __init__(self, name, description, periodicity, created_at=None, streak=0, last_completed=None):
        self.name = name
        self.description = description
        self.periodicity = periodicity
        self.created_at = created_at or datetime.now().isoformat()
        self.streak = streak
        self.last_completed = last_completed

    def mark_complete(self):
        """Marks the habit as complete and updates the streak."""
        today = datetime.now().date().isoformat()
        if self.last_completed != today:
            self.streak += 1
            self.last_completed = today

    def reset_streak(self):
        """Resets the streak."""
        self.streak = 0

    @staticmethod
    def from_row(row):
        """Converts a database row into a Habit object."""
        return Habit(
            name=row[1],
            description=row[2],
            periodicity=row[3],
            created_at=row[4],
            streak=row[5],
            last_completed=row[6],
        )
