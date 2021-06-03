# Lints the Markdown file and report the errors
markdown-linter:
	@docker run -i --rm -v ${PWD}:/work tmknom/markdownlint *.md docs/*.md

# Needs git version >= 2.9
install-git-hooks:
	@git config --get core.hooksPath