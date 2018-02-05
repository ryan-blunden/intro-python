IMAGE_NAME=rabbitbird/python
VERSION=1.0

build:
	docker image build -t $(IMAGE_NAME):$(VERSION) .

run: build
	docker container run --rm -it -v $(CURDIR):/usr/src/app $(IMAGE_NAME):$(VERSION) bash
