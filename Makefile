DC = docker compose

run:
	${DC} --env-file .env up --build -d

stop:
	${DC} down