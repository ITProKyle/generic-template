sync:
	PIPENV_VENV_IN_PROJECT=1 pipenv sync --dev

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
