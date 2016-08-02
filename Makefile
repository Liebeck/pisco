name = pisco
registry = hub.docker.com

build:
	docker build -t $(registry)/$(name) $(BUILD_OPTS) .

stop:
	docker rm -f $(name) || true

run: stop start_knife
	docker run -it --rm=true --link knife:knife -v $(shell pwd):/var/www \
	--name=$(name) $(registry)/$(name) bash -l

start: stop start_knife
	docker run -d --link knife:knife -v $(shell pwd):/var/www \
	--name=$(name) $(registry)/$(name)

start_knife: stop_knife
	docker pull pasmod/knife:latest
	docker run -d -p 4567:4567 --name=knife pasmod/knife

stop_knife:
	if docker inspect knife >/dev/null 2>&1; then docker stop knife; docker rm knife; fi
