# Flask Email Collection App

This is a simple Flask application that collects email addresses from users and stores them in an SQLite database.

## Project Structure

```
flask-email-app
├── app.py                  # Main entry point of the Flask application
├── templates
│   └── collect_email.html  # HTML form for collecting email addresses
├── static
│   └── style.css           # CSS styles for the HTML form
├── requirements.txt        # List of dependencies for the project
├── README.md               # Documentation for the project
└── database
    └── emails.db          # SQLite database for storing collected emails
```

## Requirements

To run this application, you need to have Python installed on your machine. You also need to install the required packages listed in `requirements.txt`.

## Installation

1. Clone the repository or download the project files.
2. Navigate to the project directory.
3. Install the required packages:

```
pip install -r requirements.txt
```

## Running the Application

1. Start the Flask application:

```
python app.py
```

2. Open your web browser and go to `http://127.0.0.1:5000/` to access the email collection form.

## Usage

- Enter your email address in the form and click the submit button.
- The email address will be stored in the SQLite database.

## License

This project is open source and available under the MIT License.