# Day 17: Quiz Game with OOP

## Project Description
A console-based trivia quiz game built using Object-Oriented Programming principles in Python. The game loads film trivia questions from a JSON file sourced from the Open Trivia Database, tracks user scores, and demonstrates class-based architecture with separate modules for question modeling, data handling, and quiz logic.

## Concepts Covered
- **Object-Oriented Programming in Python**: Creating and using custom classes (`Question`, `QuizBrain`)
- **Class Instances**: Instantiating objects from custom classes and using their methods
- **Modular Code Organization**: Separating concerns across multiple files (`question_model.py`, `data.py`, `quiz_brain.py`, `main.py`)
- **JSON Handling**: Reading and parsing JSON data using Python's `json` module
- **File I/O with Context Managers**: Using `with open()` for proper file handling
- **List Building**: Creating lists through loops and `.append()` method
- **While Loops with Object State**: Continuing game loop based on object method returns
- **API Data Integration**: Working with JSON output from Open Trivia Database
- **Encapsulation**: Object state management (score tracking, question progression)
- **Dictionary Access**: Extracting nested data from JSON structures (`data['results']`)

## Key Features
- Film trivia questions loaded from `film_trivia_OTD.json`
- Score tracking throughout the quiz
- Modular architecture with separate classes for different responsibilities
- Support for both hardcoded questions and JSON file input
- Final score display upon quiz completion
- Flexible question bank generation from external data sources

## What I Learned
This project demonstrates applying Object-Oriented Programming principles in Python. The architecture uses multiple custom classes working together: the `Question` class serves as a simple data model, while the `QuizBrain` class encapsulates all game logic. This separation of concerns is a software engineering best practice I'm reinforcing through Python implementation.

The JSON integration workflow demonstrates practical data source integration: I configured the Open Trivia Database API for film trivia questions, copied the JSON response into `film_trivia_OTD.json`, and implemented `generate_question_bank_from_json()` to parse the data structure and instantiate `Question` objects. This pattern of external data integration is common in production applications.

Python's context managers (`with open()`) provide clean file handling with automatic resource cleanup. The modular file structure demonstrates proper code organization, with each module having a single, clear responsibility - making the codebase maintainable and testable.

The implementation uses Python-specific patterns like the `json` module for deserialization and method-based control flow (`quiz.still_has_questions()`) to manage the game loop elegantly.

## How to Run
```bash