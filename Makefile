install:
	pip install --upgrade pip
lint:
	pylint **/*.py

test:  
	pytest -m pytest -vv 
	
format:
	black *.py
	
clean:	
	rm -rf build
	
# Call with `make lint` etc
