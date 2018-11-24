.PHONY: data prepare test clean

data:
	python generate_data.py

prepare:
	cd src/ && make

test:
	python run_tests.py

clean:
	rm -rf data/*.out
	rm -rf data/*.ok
	rm -rf data/*.err
