ALEMBIC_CONFIG = alembic.ini

run:
	@uvicorn WorkoutAPI.main:app --reload

create-migrations:
	@alembic -c $(ALEMBIC_CONFIG) revision --autogenerate -m $(d)

run-migrations:
	@alembic -c $(ALEMBIC_CONFIG) upgrade head