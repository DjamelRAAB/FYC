IMAGE := loger-filebeat
REL := 8
VERSION := 6
TAG := $(VERSION).$(REL)
DOCKER_REGISTRY := localhost
FORGE_REGISTRY := # your registry adresse like containerRegistryFYC.azurecr.io
ADMIN_USERNAME := # your user for registry like containerRegistryFYC
ADMIN_PASSWORD := # your password fot registry like 53qtDS2FObvCu3oax8xqixj7/SICx86m
CURRENT_PATH := $(shell pwd)

.PHONY: build run clean push

clean:
	docker rmi $(DOCKER_REGISTRY)/$(IMAGE)

build : 
	docker build --rm=false -t $(DOCKER_REGISTRY)/$(IMAGE):$(TAG) .

run : build
	docker run -d --name agent-filebeat -v $(CURRENT_PATH)/logs/:/logs/ -v $(CURRENT_PATH)/config/:/etc/filebeat/ $(DOCKER_REGISTRY)/$(IMAGE):$(TAG) 

push:
	docker login $(FORGE_REGISTRY) --username $(ADMIN_USERNAME) --password $(ADMIN_PASSWORD)
	docker tag $(DOCKER_REGISTRY)/$(IMAGE):$(TAG) $(FORGE_REGISTRY)/$(IMAGE):$(TAG)
	docker push $(FORGE_REGISTRY)/$(IMAGE):$(TAG)
