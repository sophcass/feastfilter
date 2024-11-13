# feastfilter
A Django app that helps you find your perfect restaurant using GenAI

## Setup Instructions

### Join our Discord

Join our Discord [here](https://discord.gg/CCuyvffe)!

You can use this Discord server to share insights, ask questions, post links etc.

We will also post some helpful tips and tricks here during the workshop.

### Prerequisites
Ensure you have Python 3.12 installed. If not, you can download and install it from [Python's official website](https://www.python.org/downloads/release/python-3120/).

### Cloning the Repository
1. Open your terminal.
2. Clone the repository using Git:
   ```bash
   git clone https://github.com/yourusername/feastfilter.git
   cd feastfilter

### Setting Up the Virtual Environment
3. Create a virtual environment to manage your project's dependencies:
   ```bash
   python -m venv venv

4. Activate the virtual environment:

  - **Windows**:
  ```
  .\venv\Scripts\activate
  ```

  - **MacOS/Linux**:
  ```
  source venv/bin/activate
  ```

5. Install the project dependencies from requirements.txt:
    ```bash
    pip install -r requirements.txt

6. Set the Django settings module environment variable:
  - **Windows**:
  ```
  set DJANGO_SETTINGS_MODULE=feastfilter.settings
  set PYTHONPATH=%cd%
  ```

  - **MacOS/Linux**:
  ```
  export DJANGO_SETTINGS_MODULE=feastfilter.settings
  export PYTHONPATH=$(pwd)
  ```

7. Start the Django Development Server

 ```
   django-admin runserver
 ```

Visit `http://127.0.0.1:8000/admin/` to view and explore the existing data in the Django admin.

Log in with the following:

 - User: `pyconsweden`
 - Password: `aiworkshop`

## Your Challenge
1. Tag each review with the sentiment of the review, i.e., if it’s positive, negative, or neutral.
2. Tag each review with a theme (e.g. "Service", "Ambiance", "Location").
3. Create an enhanced short description for each restaurant (e.g. “Cocotte Shoreditch - Brunch and Cocktails with Unmatched Hospitality”).
4. Create a chatbot that gives you a recommendation of a restaurant based on your input.
5. Get creative!
