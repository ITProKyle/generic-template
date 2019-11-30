sync:
	pipenv sync -d

deploy: sync
	DEPLOY_ENVIRONMENT=$(filter-out $@, $(MAKECMDGOALS)) \
	pipenv run runway deploy

destroy: sync
	DEPLOY_ENVIRONMENT=$(filter-out $@, $(MAKECMDGOALS)) \
	pipenv run runway destroy

plan: sync
	DEPLOY_ENVIRONMENT=$(filter-out $@, $(MAKECMDGOALS)) \
	pipenv run runway plan

%:
	@:
