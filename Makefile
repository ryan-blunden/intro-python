IMAGE_NAME=rabbitbird/python
VERSION=1.0

build-docker:
	docker image build -t $(IMAGE_NAME):$(VERSION) .

run-docker: build-docker
	docker container run --rm -it -v $(CURDIR):/usr/src/app $(IMAGE_NAME):$(VERSION) bash

test:
	py.test -x -s --color=yes --junit-xml=junit-log.xml --verbose --spec --result-log=result.log $(target) -m "$(markers)"

test-debug:
	@$(eval CORES=`sysctl -n hw.physicalcpu`)
	py.test -x -s -n $(CORES) --ff --color=yes --junit-xml=junit-log.xml --verbose --spec --maxfail=999 --result-log=result.log $(target) -m "$(markers)"

lint:
	flake8 ./ \
	    --exclude=.git,slides,code-samples \
	    --max-complexity 12 \
	    --ignore=E501
