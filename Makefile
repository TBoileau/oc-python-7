.PHONY: tests

VENV_NAME?=venv
PYTHON=${VENV_NAME}/bin/python


freeze:
	${PYTHON} -m pip freeze > requirements.txt

prepare:
	python3 -m pip install --upgrade pip
	python3 -m venv $(VENV_NAME)

install:
	pip install --no-cache-dir wheel
	${PYTHON} -m pip install -r requirements.txt

fix:
	$(PYTHON) -m black --line-length 120 ./src
	$(PYTHON) -m autopep8 --recursive --in-place --aggressive --max-line-length=120 ./src/*

analyse:
	$(PYTHON) -m flake8 --max-line-length=120 ./src
	$(PYTHON) -m pylint ./src
	$(PYTHON) -m pycodestyle --max-line-length=120 ./src

tests:
	$(PYTHON) -m pytest --cov=./src --cov-report=html -s

run:
	make clean
	$(PYTHON) main.py
	make profile

clean:
	rm -rf __pycache__
	rm -rf .pytest_cache
	rm -rf htmlcov
	rm -rf profiles/dataset_*
	rm -rf profiles/*.json

profile:
	$(PYTHON) -m gprof2dot -f pstats profiles/dataset_0/greedy/profile.prof | dot -Tpng -o profiles/dataset_0/greedy/graph_calls.png
	$(PYTHON) -m gprof2dot -f pstats profiles/dataset_0/dynamic_programming/profile.prof | dot -Tpng -o profiles/dataset_0/dynamic_programming/graph_calls.png
	$(PYTHON) -m gprof2dot -f pstats profiles/dataset_0/optimized_dynamic_programming/profile.prof | dot -Tpng -o profiles/dataset_0/optimized_dynamic_programming/graph_calls.png
	$(PYTHON) -m gprof2dot -f pstats profiles/dataset_0/naive_recursive/profile.prof | dot -Tpng -o profiles/dataset_0/naive_recursive/graph_calls.png
	$(PYTHON) -m gprof2dot -f pstats profiles/dataset_0/memoization_technique/profile.prof | dot -Tpng -o profiles/dataset_0/memoization_technique/graph_calls.png

	$(PYTHON) -m gprof2dot -f pstats profiles/dataset_1/greedy/profile.prof | dot -Tpng -o profiles/dataset_1/greedy/graph_calls.png
	$(PYTHON) -m gprof2dot -f pstats profiles/dataset_1/dynamic_programming/profile.prof | dot -Tpng -o profiles/dataset_1/dynamic_programming/graph_calls.png
	$(PYTHON) -m gprof2dot -f pstats profiles/dataset_1/optimized_dynamic_programming/profile.prof | dot -Tpng -o profiles/dataset_1/optimized_dynamic_programming/graph_calls.png

	$(PYTHON) -m gprof2dot -f pstats profiles/dataset_2/greedy/profile.prof | dot -Tpng -o profiles/dataset_2/greedy/graph_calls.png
	$(PYTHON) -m gprof2dot -f pstats profiles/dataset_2/dynamic_programming/profile.prof | dot -Tpng -o profiles/dataset_2/dynamic_programming/graph_calls.png
	$(PYTHON) -m gprof2dot -f pstats profiles/dataset_2/optimized_dynamic_programming/profile.prof | dot -Tpng -o profiles/dataset_2/optimized_dynamic_programming/graph_calls.png

visualization:
	$(PYTHON) -m cprofilev -f profiles/dataset_$(dataset)/$(algorithm).prof

