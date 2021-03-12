## Please run/do a postgres docker command before starting

-   `docker run --rm -p 5432:5432 --name some-postgres -e POSTGRES_PASSWORD=qwerty -e POSTGRES_USER=dilnix -d postgres`

-   write your DB models in homework/flask_alembic_hw/al_api_hotel/models.py

-   `cd homework/flask_alembic_hw/al_api_hotel/ && alembic revision --autogenerate -m "Initial revision"`

#### Slides of lesson are at https://slides.com/cursor_edu/flask-practice
