#

all:
	@echo "Targets: help clean install pack git"

#Type 'make help' for a list of targets"

help:
	@echo "Targets:"
	@echo "  make help       -- This screen"
	@echo "  make git        -- Check in to repo"
	@echo "  make clean      -- Clean temporaies"
	@echo "  make install    -- Install  "
	@echo "  make pack       -- Package to gz"

install:
	@./install.py

pack:
	@./pack.sh

git:
	git add .
	git commit -m autocheck
	git push

clean:
	rm -f  *.pyc
	rm -rf __pycache__

# End of Makefile
