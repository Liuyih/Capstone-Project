.PHONY: test clean diff

clean:
	rm -f *.csv

run: parse_list_mode_test.py 160513_DU2.txt
	python3 parse_list_mode_test.py 160513_DU2.txt

diff: run
	diff -qr original/ output/

lint:
	pipenv run flake8 .

test:
	pipenv run mypy .
	pipenv run pytest tests/
