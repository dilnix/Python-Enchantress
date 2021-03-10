## Lector asked to do:

-   Rewrite _login_app_ to act like an API. Remove templates and
    return JSON data in responses to all it's endpoints.
-   Add Order model with user_id and time of order
-   Add OrderLine model with products information (product name, and price)
-   Add additional _/orders_ endpoint to _login_app/main.py_ secured
    by _login_required_ decorator. This endpoint should return list of
    orders related to user.
-   Add create-database flask cli

## Student added some recomendations:

The Flask app is located in folder `api_app`.
To run it from current folder (where reading me) you need to just use command `flask run`.

Applicatio will not be fully functional, so you need to use flask cli to create a DB.
Use `flask create-db` to create it.
