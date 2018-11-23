data:
	mkdir data
	python generate_data.py

prepare:
	cd src/ && make

test:
	python run_tests.py

clean:
	rm data/*.out
	rm data/*.ok
