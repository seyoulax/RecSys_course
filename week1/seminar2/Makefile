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

jupyter:
	@screen -dmS jupyter poetry run jupyter lab --no-browser --allow-root --ip 0.0.0.0 --port $(PORT)
