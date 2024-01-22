SHELL=/bin/bash
LOCATION=Canada

include .env

setup:
	@pre-commit install -c .pre-commit-config.yaml
	@pip install -r requirements.txt

who:
	@echo "I am $(DEVELOPER_NAME) from $(LOCATION)"

show:
	@chmod +x ./scripts/list_files.sh
	@./scripts/list_files.sh

where:
	@echo $(shell pwd)

run: who
	@python main.py
