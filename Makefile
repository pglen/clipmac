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

pipinstall:
	pip install .

pipuninstall:
	pip uninstall clipmac

docs:
	@PYTHONPATH=clipmac pdoc --html -f clipmacro.py
	@PYTHONPATH=clipmac pdoc --html -f clipmac/chrisdlg.py
	@PYTHONPATH=clipmac pdoc --html -f clipmac/chrissql.py
	@PYTHONPATH=clipmac pdoc --html -f clipmac/config.py
	@PYTHONPATH=clipmac pdoc --html -f clipmac/chrispane.py
	@PYTHONPATH=clipmac pdoc --html -f clipmac/chriswin.py

# End of Makefile
