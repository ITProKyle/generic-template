sync:
	pipenv sync -d

deploy: sync
	DEPLOY_ENVIRONMENT=$(filter-out $@, $(MAKECMDGOALS)) \
	pipenv run runway deploy

deploy: sync
	DEPLOY_ENVIRONMENT=$(filter-out $@, $(MAKECMDGOALS)) \
	pipenv run runway destroy

deploy: sync
	DEPLOY_ENVIRONMENT=$(filter-out $@, $(MAKECMDGOALS)) \
	pipenv run runway plan

%:
	@:
