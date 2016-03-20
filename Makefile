PACKAGE=tergraw

run:
	python -m $(PACKAGE)

t:
	py.test $(PACKAGE) --doctest-module --failed-first --exitfirst

register:
	python setup.py sdist register

upload:
	python setup.py sdist upload

clear:
	rm -r edgelist.utf-8 grid.dot grid.edgelist __pycache__ test.edgelist test.edgelist.gz .cache tergraw.egg-info
