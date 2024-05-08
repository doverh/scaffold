install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

lint:
	pylint **/*.py

test:  
	pytest -m pytest -vv 
	
format:
	black *.py
	
clean:	
	rm -rf build
	
# Call with `make lint` etc