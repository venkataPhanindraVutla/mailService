# Mail Service Microservice

This microservice is responsible for sending emails and logging email transactions. It uses FastAPI, SQLAlchemy, and RabbitMQ.

## Setup

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/venkataPhanindraVutla/mailService
    cd mailService
    ```

2.  **Create a virtual environment (recommended):**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up environment variables:**

    Create a `.env` file in the root directory of the project with the following variables:

    ```env
    PROJECT_NAME="Mail Service"
    SMTP_HOST="your_smtp_host"
    SMTP_PORT=your_smtp_port
    SMTP_USER="your_smtp_user"
    SMTP_PASS="your_smtp_password"
    FROM_EMAIL="your_from_email@example.com"
    RABBITMQ_URL="amqp://guest:guest@localhost/" # Or your RabbitMQ connection string
    SQLALCHEMY_DATABASE_URI="sqlite:///./sql_app.db" # Or your database connection string
    ```

    Replace the placeholder values with your actual configuration.

## Running the Application

The application consists of two main parts: the FastAPI web server and the RabbitMQ consumer worker.

1.  **Start the FastAPI server:**

    ```bash
    uvicorn main:app --reload
    ```

    The API documentation will be available at `http://127.0.0.1:8000/docs`.

2.  **Start the RabbitMQ consumer worker:**

    ```bash
    python worker.py
    ```

    This worker will consume messages from the "mail_queue" and send emails.

## Code Documentation

The codebase is documented using docstrings following common Python conventions.

-   **`app/consumers/mail_consumer.py`**: RabbitMQ consumer logic.
-   **`app/core/config.py`**: Application settings loaded from environment variables.
-   **`app/core/mailer.py`**: Mailer class for sending emails.
-   **`app/db/`**: Database related files (base class, session, models).
-   **`app/routes/mail.py`**: FastAPI routes for mail operations.
-   **`app/schemas/mail.py`**: Pydantic schemas for data validation.
-   **`app/services/mail.py`**: Service layer for mail sending and logging.
-   **`app/utils/exceptions.py`**: Custom exception handling.
-   **`main.py`**: Main FastAPI application entry point.
-   **`worker.py`**: Script to run the RabbitMQ consumer.