markdown-linter:
	@docker run -i --rm -v ${PWD}:/work tmknom/markdownlint *.md docs/*.md