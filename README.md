# ToDo_Web_App_in_Python_Django
This GitHub repository houses a todo web application developed using Python's Django framework. The application serves as a versatile tool for users to organize and manage their tasks efficiently. Through an intuitive user interface, individuals can create, prioritize, and track their to-do lists seamlessly.

---------------------------------
### How to Run Locally:

To run this project locally on your machine, follow these steps:

#### Prerequisites:

1. **Python:** Ensure that Python is installed on your system. You can download and install Python from [here](https://www.python.org/downloads/).

2. **Virtual Environment (optional but recommended):** It's good practice to use a virtual environment to manage dependencies for your project. If you don't have `virtualenv` installed, you can install it using:

    ```bash
    pip install virtualenv
    ```

#### Setup:

1. **Clone the Repository:** 

    ```bash
    git clone <repository-url>
    ```

2. **Navigate to the Project Directory:**

    ```bash
    cd todo
    ```

3. **Create a Virtual Environment (optional):**

    ```bash
    virtualenv venv
    ```

4. **Activate the Virtual Environment (optional):**

    - On Windows:

    ```bash
    venv\Scripts\activate
    ```

    - On macOS/Linux:

    ```bash
    source venv/bin/activate
    ```

5. **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

6. **Run Migrations:**

    ```bash
    python manage.py migrate
    ```

#### Running the Server:

Now that the setup is complete, you can run the Django development server:

```bash
python manage.py runserver
```

Once the server is running, you can access the todo web application by opening your web browser and navigating to [http://localhost:8000/](http://localhost:8000/).
