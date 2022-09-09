_install:
	@poetry config virtualenvs.in-project true

install-cpu: _install
	@poetry install
	@poetry run pip install torch==1.12.1 --default-timeout=1000
	@echo "[ \033[00;32mPoetry setup completed. You are good to go!\033[0m ]"

install-cuda: _install
	@poetry install
	@poetry run pip install torch=="1.12.1+cu116" --extra-index-url https://download.pytorch.org/whl/cu116
	@echo "[ \033[00;32mPoetry setup completed. You are good to go!\033[0m ]"

kill:
	@docker-compose kill

compose: kill
	@echo ""
	@echo "[ \033[00;32mRunning in docker-compose\033[0m ]"
	@docker-compose up --build --force-recreate --remove-orphans -d

jupyter:
	@screen -dmS jupyter poetry run jupyter lab --no-browser --allow-root --ip 0.0.0.0 --port $(PORT)
