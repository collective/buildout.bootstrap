pre:
	check-manifest
	pyroma .
	python setup.py test
	viewdoc
