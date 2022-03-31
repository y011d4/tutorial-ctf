default:
	cp src/app.py dist/app.py
	# sed -i -E "s|(app.secret_key = ).*|\1b\"FAKE{this_is_a_fake_flag}\"|" dist/app.py
clean:
	$(RM) dist/*
