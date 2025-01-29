# Contact Us Project

This is a Django mini-project for a "Contact Us" form.

## Setup Instructions

1. **Clone the repository:**
    ```sh
    git clone <repository_url>
    cd contact_us_Proj
    ```

2. **Create a virtual environment:**
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

4. **Apply migrations:**
    ```sh
    python manage.py migrate
    ```

5. **Run the development server:**
    ```sh
    python manage.py runserver
    ```

## Usage

- Access the application at `http://127.0.0.1:8000/`.
- Fill out the contact form and submit.

## Project Structure

- `contact_us_Proj/`: Main project directory.
- `contact_us_app/`: Django app for the contact form.
- `templates/`: HTML templates.
- `static/`: Static files (CSS, JavaScript).

## Contributing

Feel free to submit issues or pull requests.

