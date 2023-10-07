.PHONY: run-grand-agent
run-grand-agent:
	pipenv run python3 main.py

.PHONY: run-qr-generator
run-qr-generator:
	pipenv run python3 qr_generator.py

.PHONY: run-csv-analyzer
run-csv-analyzer:
	pipenv run python3 csv_analyzer.py

.PHONY: format
format:
	black .