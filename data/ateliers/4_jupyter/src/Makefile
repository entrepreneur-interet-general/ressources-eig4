build:
	docker-compose build

run:
	docker-compose up -d

logs:
	docker-compose logs -f

down:
	docker-compose down

restart-jupyter-base:
	docker-compose stop jupyter-base
	docker-compose rm jupyter-base
	docker-compose up -d jupyter-base
	docker-compose logs -f jupyter-base

restart-jupyter-spark:
	docker-compose stop jupyter-spark
	docker-compose rm jupyter-spark
	docker-compose up -d jupyter-spark
	docker-compose logs -f jupyter-spark
