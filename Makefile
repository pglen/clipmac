# Makefile

all:
	@echo "Targets: help clean install pack git docs"

help:
	@echo "Targets:"
	@echo "  make help       -- This screen"
	@echo "  make git        -- Check in to repo"
	@echo "  make clean      -- Clean temporaies"
	@echo "  make install    -- Install  "
	@echo "  make pack       -- Package to gz"
	@echo "  make docs       -- Create documentation"

install:
	@./install.py

pack:
	@./pack.sh

git:
	-git add .
	-git commit -m autocheck
	git push

clean:
	rm -f  *.pyc
	rm -rf __pycache__
	rm -rf build
	rm -rf dist

pipinstall:
	pip install .

pipuninstall:
	pip uninstall clipmac

docs:
	@mkdir -p clipmac/html
	@PYTHONPATH=clipmac pdoc --html -f -o clipmac/html clipmacro.py
	@PYTHONPATH=clipmac pdoc --html -f -o clipmac/html clipmac/chrisdlg.py
	@PYTHONPATH=clipmac pdoc --html -f -o clipmac/html clipmac/chrissql.py
	@PYTHONPATH=clipmac pdoc --html -f -o clipmac/html clipmac/config.py
	@PYTHONPATH=clipmac pdoc --html -f -o clipmac/html clipmac/chrispane.py
	@PYTHONPATH=clipmac pdoc --html -f -o clipmac/html clipmac/chriswin.py

pipup: #pipbuild
	@./pip-upload.sh

pipbuild:
	@# Gather a copy of main README
	@./pip-build.py

# End of Makefile
