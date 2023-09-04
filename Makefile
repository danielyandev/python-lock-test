install_requirements:
	pip install -r requirements.txt

copy_env:
	cp .env.example .env

copy_counter_files:
	cp counter.txt.example counter1.txt && cp counter.txt.example counter2.txt

prepare: install_requirements copy_env copy_counter_files

start:
	python main.py
