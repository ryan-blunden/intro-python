run:
	# Use Make to figure out the current directory
	docker container run --rm -it -v "$(CURDIR)":/usr/src/app rabbitbird/python:1.0 bash


FLAKE8_PATH=./
lint:
	flake8 $(FLAKE8_PATH) \
		--exclude=folder_name,filename.py \
		--max-complexity 12 \
		--ignore=E501
