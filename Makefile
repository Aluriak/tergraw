PACKAGE=tergraw

run:
	python3 -m $(PACKAGE)

t:
	py.test $(PACKAGE) --doctest-module --failed-first --exitfirst

register:
	python3 setup.py sdist register

upload:
	python3 setup.py sdist upload

clear:
	rm -r edgelist.utf-8 grid.dot grid.edgelist __pycache__ test.edgelist test.edgelist.gz .cache tergraw.egg-info
