# feastfilter
A Django app that helps you find your perfect restaurant using GenAI

## Setup Instructions

### Join our Discord
Join our Discord [here](https://discord.gg/CCuyvffe)!

You can use this Discord server to share insights, ask questions, post links, etc. We will also post some helpful tips and tricks here during the workshop.

### Prerequisites
Ensure you have at least **Python 3.9** installed. If not, download and install it from [Python's official website](https://www.python.org/downloads/release/python-3120/).

### Cloning the Repository
1. Open your terminal.
2. Clone the repository using Git:
   ```bash
   git clone https://github.com/yourusername/feastfilter.git
   cd feastfilter
   ```

### Setting Up the Virtual Environment
3. Create a virtual environment to manage your project's dependencies:
   ```bash
   python -m venv venv
   ```

4. Activate the virtual environment:

   - **Windows**:
     ```bash
     .\venv\Scripts\activate
     ```
   
   - **MacOS/Linux**:
     ```bash
     source venv/bin/activate
     ```

5. Install the project dependencies from `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

6. Set the Django settings module environment variable:

   - **Windows**:
     ```bash
     set DJANGO_SETTINGS_MODULE=feastfilter.settings
     set PYTHONPATH=%cd%
     ```

   - **MacOS/Linux**:
     ```bash
     export DJANGO_SETTINGS_MODULE=feastfilter.settings
     export PYTHONPATH=$(pwd)
     ```

7. Start the Django Development Server:
   ```bash
   django-admin runserver
   ```

Visit the [Django Admin Panel](http://127.0.0.1:8000/admin/) to view and explore the existing data in the Django admin.

**Log in with the following credentials:**
- **User**: `pyconsweden`
- **Password**: `aiworkshop`

## Your Challenge
1. Tag each review with the sentiment of the review (e.g., positive, negative, or neutral).
2. Tag each review with a theme (e.g., "Service," "Ambiance," "Location").
3. Create an enhanced short description for each restaurant (e.g., "Cocotte Shoreditch - Brunch and Cocktails with Unmatched Hospitality").
4. Create a chatbot that recommends a restaurant based on user input.
5. Get creative!

## Using AI Functions with Django

The code for each task is located in the following files:
- **`anthropic_functions.py`**: Functions leveraging the Anthropic AI model.
- **`openai_functions.py`**: Functions utilizing the OpenAI model.

### Available Commands

1. **Add Sentiment Analysis**
   ```bash
   django-admin add_sentiment
   ```

2. **Add Theme Extraction**
   ```bash
   django-admin add_theme
   ```

3. **Add Enhanced Naming**
   ```bash
   django-admin add_enhanced_name
   ```

### Choosing the AI Model

To specify the AI model you want to use, append one of the following flags:
- `--open-ai`: Use the OpenAI model.
- `--anthropic`: Use the Anthropic model.

**Example Usage:**
```bash
django-admin add_sentiment --open-ai
```
```bash
django-admin add_theme --anthropic
```

### Verifying the Results

Once you run a command, you can verify the data added to the database:

1. **Admin Interface**
   - Navigate to: [Django Admin Panel](http://127.0.0.1:8000/admin/)
   - Check the relevant data entries that have been created or updated.

2. **Chatbot Testing**
   - Visit: [Chatbot Interface](http://127.0.0.1:8000/chatbot/)
   - Interact with the chatbot to test the newly added functionalities.

### Notes
- Ensure your Django server is running when executing the commands and accessing the web interfaces.
- If you encounter issues, check that the appropriate dependencies for OpenAI and Anthropic are installed and properly configured.

---

Happy coding and enjoy leveraging AI capabilities in your Django projects!
