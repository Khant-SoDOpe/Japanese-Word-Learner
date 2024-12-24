# Japanese Word Learner

This is a simple web application to help users learn Japanese Hiragana and Katakana characters through quizzes. The application is built using Flask and provides a user-friendly interface for selecting and taking quizzes.

## Features

- Home page with an introduction to the quiz
- Selection page to choose between Hiragana and Katakana quizzes
- Quiz pages for Hiragana and Katakana characters
- About Us page with information about the benefits of learning Japanese

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/Japanese-Word-Learner.git
    cd Japanese-Word-Learner
    ```

2. Create a virtual environment and activate it:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install Flask
    ```

## Running the Application

1. Start the Flask application:
    ```bash
    python app.py
    ```

2. Open your web browser and go to `http://127.0.0.1:5000/` to access the application.

## Project Structure

- `app.py`: The main application file containing the Flask routes and logic.
- `templates/`: Directory containing HTML templates for different pages.
  - `index.html`: Home page template.
  - `select.html`: Selection page template.
  - `quiz.html`: Quiz page template.
  - `about_us.html`: About Us page template.
- `static/images/`: Directory containing static images used in the application.