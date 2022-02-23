GIT_TAG ?= $(shell git describe --tags --always)
IMG ?= quay.io/mroman_redhat/jh-web-app
DOCKERFILE ?= jupyter/Dockerfile

docker-build:
	cd ../ && podman build -t ${IMG}:${GIT_TAG} -f ${DOCKERFILE} .

docker-push:
	docker push $(IMG):$(GIT_TAG)

image: docker-build docker-push
