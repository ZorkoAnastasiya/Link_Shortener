# Link Shortener  [![View project](https://img.shields.io/badge/VIEW-PROJECT-268BD2)](https://link-tiny.herokuapp.com/)

___

### _Installing and running the project:_

1. Install packages from requirements.txt file

2. Create a .env file in the superproject directory and add to it:

   - Set the environment variable DEBUG (True - for local launch)

   - Add the environment variable DATABASE_URL, indicating the url to the connected database

3. Run the following commands from the superproject directory:
            
    - Apply migrations

        ```
        python manage.py migrate
        ```
      
    - Create a superuser for access to project administration
        ```
        python manage.py createsuperuser
        ```    
   
    - Start the local server
        ```
        python manage.py runserver
        ```      
   
---	