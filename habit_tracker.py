import sqlite3
from habit import Habit

class HabitTracker:
    def __init__(self, db_file="habits.db"):
        """Initialize the HabitTracker and connect to the SQLite database."""
        self.db_file = db_file
        self._create_table()

    def _create_table(self):
        """Create the habits table if it doesn't exist."""
        with sqlite3.connect(self.db_file) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS habits (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    description TEXT,
                    periodicity TEXT NOT NULL,
                    created_at TEXT,
                    streak INTEGER,
                    last_completed TEXT
                )
            """)
            conn.commit()

    def add_habit(self, habit):
        """Add a new habit to the database."""
        with sqlite3.connect(self.db_file) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO habits (name, description, periodicity, created_at, streak, last_completed)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (habit.name, habit.description, habit.periodicity, habit.created_at, habit.streak, habit.last_completed))
            conn.commit()

    def remove_habit(self, habit_name):
        """Remove a habit from the database by name."""
        with sqlite3.connect(self.db_file) as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM habits WHERE name = ?", (habit_name,))
            conn.commit()

    def get_current_habits(self):
        """Retrieve all habits from the database."""
        with sqlite3.connect(self.db_file) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM habits")
            rows = cursor.fetchall()
            return [Habit.from_row(row) for row in rows]

    def mark_habit_complete(self, habit_name):
        """Mark a habit as complete and update its streak."""
        with sqlite3.connect(self.db_file) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM habits WHERE name = ?", (habit_name,))
            row = cursor.fetchone()
            if row:
                habit = Habit.from_row(row)
                habit.mark_complete()
                cursor.execute("""
                    UPDATE habits
                    SET streak = ?, last_completed = ?
                    WHERE name = ?
                """, (habit.streak, habit.last_completed, habit.name))
                conn.commit()
