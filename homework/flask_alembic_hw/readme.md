## Steps of reproduction

-   navigate to folder `cd homework/flask_alembic_hw/al_api_hotel/`
-   remove folder withh all earlier versions 'alembic/versions/'
-   run a DB container `docker run --rm -p 5432:5432 --name some-postgres -e POSTGRES_PASSWORD=qwerty -e POSTGRES_USER=dilnix -d postgres`
-   check first DB table 'owner' is wrote good as a class in models file located models.py
-   start first revision automatically `alembic revision --autogenerate -m "Initial revision"`
-   apply it `alembic upgrade head`
-   check your autogenerated revision in folder alembic/versions/
-   create a new revision manually `alembic revision -m "Second revision"`
-   write down a creation rules of 'pet' table into newly created revision file at alembic/versions/ inside function upgrade()
-   apply it `alembic upgrade head` and check DB with manual connection if needed
-   create one more revision manually `alembic revision -m "Third revision"`
-   write down a creation rules of 'activity' table into newly created revision file at alembic/versions/ inside function upgrade()
-   apply it `alembic upgrade head` and check DB with manual connection if needed

#### Slides of lesson are at https://slides.com/cursor_edu/flask-practice