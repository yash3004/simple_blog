

# Simple Flask Blog Site

This is a basic blogging website built using Flask, Flask-SQLAlchemy, and Jinja templating.

## Features

- **User Authentication:** Users can sign up, log in, and log out.
- **Create and Edit Posts:** Authenticated users can create new blog posts and edit their existing posts.
- **View and Comment:** Users can view blog posts and add comments.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yash3004/simple_flask.git
   ```

2. Navigate to the project directory:
   ```bash
   cd simple_blog
   ```

3. Install dependencies using pip:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Set up the database:
   - Modify the `config.py` file to configure your database settings.
   - Run the following commands to create database tables:
     ```bash
     python
     from app import db
     db.create_all()
     exit()
     ```

2. Run the Flask application:
   ```bash
   python app.py
   ```

3. Access the blog site:
   Open your web browser and navigate to `http://localhost:5000`.

## Configuration

Modify the `config.py` file to set up your database, secret key, and other configuration variables.

## Contributing

Contributions are welcome! Please create an issue or submit a pull request if you'd like to contribute to this project.

## Credits

This project was created by Yash Sehgal. Feel free to contact me at yashsehgal9253@gmail.com for any inquiries.

