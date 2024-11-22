# Habit Tracker CLI App

## Overview
The Habit Tracker CLI App is a command-line tool designed to help users build and maintain positive habits. By tracking daily and weekly habits, users can stay consistent and monitor their progress over time. With robust analytics and data storage powered by SQLite, this app provides all the tools needed to develop productive routines.

## Key Features
- Add, delete, and complete habits with a simple CLI.
- Track daily and weekly habits.
- Analyze habit streaks and completion history.
- Persistent data storage using SQLite.

## Installation

### Prerequisites
- Python 3.7 or later installed on your system.

### Steps
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd HabitTrackerProject
2. Create and activate a virtual enviroment:
   ```bash
   python -m venv env
   .\env\Scripts\activate # On Windows
   source env/bin/activate # On macOS/Linux
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt

## Usage
   To run the application, use the following command:
   ```bash
   python main.py
   ```
### Available Commands
- Add Habit:
   ```bash
   python main.py add-habit
Follow the prompts to add a habit with a name, description, and periodicity.

- View Habits:
   ```bash
   python main.py view-habits
   
- Complete a Habit:
   ```bash
   python main.py complete-habit

- Find Longest Streak:
   ```bash
   python main.py find-longest-streak

### Example
To add a daily habit:
   ```bash
   python main.py add-habit
   ```
Enter the following when prompted:
- Habit name: Exercise
- Description: 30-minute workout
- Periodicity: daily

## Testing
Unit tests are included to ensure the functionality of the app. To run the tests:
   ```bash
   pytest tests/
  ```

### Predefined Test Data
The app comes with 4 weeks of sample habit data for testing streak calculations and analytics functionality.

### Project Structure
   ```bash
      HabitTrackerProject/
│
├── main.py            # Entry point for the CLI
├── habit.py           # Defines the Habit class
├── habit_tracker.py   # Manages database interactions
├── analytics.py       # Provides analytics functions
├── tests/             # Unit tests for app functionality
├── README.md          # Project documentation
├── requirements.txt   # Dependencies
```
## Design Decisions
- Modular design using Object-Oriented Programming.
- Persistent habit data storage with SQLite.
- Functional programming principles in the analytics module.

## Conclusion
The Habit Tracker CLI App is a powerful tool to help users stay consistent and achieve their goals. By combining simplicity with robust functionality, it provides everything needed to develop productive routines.

## Contributing
Pull requests are welcome! If you'd like to contribute, please open an issue to discuss changes.

## License
This project is licensed under the MIT License.

Thank you for exploring the Habit Tracker CLI App!

