# django-custom-user

This repository is used as a dummy project to demonstrate how to migrate to a custom Django user model mid-project.

The repository is split into two branches:

1. `base` - starting point (using Django's default user model)
2. `master` - end point (using custom user model)

To learn how it's done check out the [article](https://testdriven.io/blog/django-custom-user-model-migration/).

## Want to use this project?

1. Fork/Clone (make sure to clone the right branch).

2. Create and activate a virtual environment:

    ```sh
    $ python3 -m venv venv && source venv/bin/activate
    ```

3. Install the requirements:

    ```sh
    (venv)$ pip install -r requirements.txt
    ```
   
4. Spin up a Postgres container or use [locally installed PostgreSQL](https://www.postgresql.org/download/):

    ```sh
    $ docker run --name django-todo-postgres -p 5432:5432 \
        -e POSTGRES_USER=django-todo -e POSTGRES_PASSWORD=complexpassword123 \
        -e POSTGRES_DB=django-todo -d postgres
    ```

   If you're going to use locally installed PostgreSQL, make sure to go to *core/settings.py* and change `DATABASES` credentials accordingly.


6. Apply the migrations:

    ```sh
    (venv)$ python manage.py migrate
    ```
   
7. (Optional) Fill the database with sample data:

    ```sh
    $ (venv) python manage.py loaddata fixtures/auth.json --app auth
    $ (venv) python manage.py loaddata fixtures/todo.json --app todo
    ```
   
    These two fixtures also create a superuser with the following credentials:

    ```
    username:  admin
    password:  password
    ```

8. Run the server:

    ```sh
    (venv)$ python manage.py runserver
    ```
    
9. Navigate to [http://localhost:8000/admin/](http://localhost:8000/admin/) in your favorite web browser and login. 
