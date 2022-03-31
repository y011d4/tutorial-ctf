default:
	gcc src/flag_checker.c -o src/flag_checker
	cp src/flag_checker dist/flag_checker
test:
	strings src/flag_checker | grep FLAG
clean:
	$(RM) dist/*
