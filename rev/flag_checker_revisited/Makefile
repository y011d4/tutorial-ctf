default:
	gcc src/flag_checker_revisited.c -o src/flag_checker_revisited
	cp src/flag_checker_revisited dist/flag_checker_revisited
test:
	strings src/flag_checker_revisited | grep FLAG
clean:
	$(RM) dist/*
