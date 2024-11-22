import click  # Importing Click to manage CLI commands
from habit_tracker import HabitTracker  # Import HabitTracker class for habit management
from habit import Habit  # Import Habit class for habit data
import analytics  # Import analytics module for habit analysis

# Initialize the HabitTracker instance
tracker = HabitTracker()

@click.group()
def cli():
    """Main command group for Habit Tracker CLI."""
    pass

@cli.command()
@click.option('--name', prompt='Habit name', help='The name of the habit')
@click.option('--description', prompt='Description', help='A brief description of the habit')
@click.option('--periodicity', type=click.Choice(['daily', 'weekly']), prompt='Periodicity (daily/weekly)')
def add_habit(name, description, periodicity):
    """Command to add a new habit."""
    habit = Habit(name, description, periodicity)
    tracker.add_habit(habit)
    click.echo(f"Habit '{name}' added.")

@cli.command()
@click.option('--name', prompt='Habit name', help='The name of the habit to delete')
def remove_habit(name):
    """Command to remove an existing habit."""
    tracker.remove_habit(name)
    click.echo(f"Habit '{name}' removed.")

@cli.command()
@click.option('--name', prompt='Habit name', help='The name of the habit to complete')
def complete_habit(name):
    """Command to mark a habit as complete."""
    tracker.mark_habit_complete(name)
    click.echo(f"Habit '{name}' marked as complete.")

@cli.command()
def view_habits():
    """Command to view all current habits."""
    habits = tracker.get_current_habits()
    for habit in habits:
        click.echo(f"{habit.name} - {habit.description} - {habit.periodicity}")

@cli.command()
def view_streaks():
    """Command to view streaks for all habits."""
    habits = tracker.get_current_habits()
    for habit in habits:
        click.echo(f"{habit.name}: {habit.streak} day(s)")

@cli.command()
@click.option('--name', prompt='Habit name', help='The name of the habit')
def view_streak_for_habit(name):
    """Command to view the streak for a specific habit."""
    streak = analytics.get_streak_for_habit(tracker, name)
    click.echo(f"{name} streak: {streak} day(s)")


@cli.command()
def find_longest_streak():
    """Command to find the habit with the longest streak."""
    longest_streak_habit = analytics.get_longest_streak(tracker)
    if longest_streak_habit:
        click.echo(f"The habit with the longest streak is '{longest_streak_habit.name}' with {longest_streak_habit.streak} day(s).")
    else:
        click.echo("No habits found.")


if __name__ == '__main__':
    cli()  # Initialize CLI
