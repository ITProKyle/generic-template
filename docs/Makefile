SPHINXOPTS    =
SPHINXBUILD   = poetry run sphinx-build
SOURCEDIR     = source
BUILDDIR      = build

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: Makefile clean docs help open requirements

clean:
	@rm -rf build/html/*
	@echo "Removed HTML files from previous build"
	@rm -rf source/apidocs/*
	@echo "Removed apidocs from previous build"

docs: clean html

open:
	@open build/html/index.html

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@rm -rf $(BUILDDIR) && \
	$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
