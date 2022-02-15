GIT_TAG ?= experimental-v21
IMG ?= quay.io/mroman_redhat/jh-web-app
DOCKERFILE ?= jupyter/Dockerfile

docker-build:
	cd ../ && podman build -t ${IMG}:${GIT_TAG} -f ${DOCKERFILE} .

docker-push:
	podman push $(IMG):$(GIT_TAG)

image: docker-build docker-push
