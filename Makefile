install:
	pip install --upgrade pip

lint:
	pylint *.py

test:
	python -m pytest -vv testPwdGen.py
	
format:
	black *.py
	
clean:	
	rm -rf build
	
# Call with `make lint` etc
