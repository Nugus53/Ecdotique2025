.PHONY: all fr grc la

all: fr grc la

fr:
	@echo "Installing SpaCy models for French..."
	pip install "fr_core_news_sm @ https://huggingface.co/spacy/fr_core_news_sm/resolve/main/fr_core_news_sm-any-py3-none-any.whl"
	pip install "fr_core_news_md @ https://huggingface.co/spacy/fr_core_news_md/resolve/main/fr_core_news_md-any-py3-none-any.whl"
	pip install "fr_core_news_lg @ https://huggingface.co/spacy/fr_core_news_lg/resolve/main/fr_core_news_lg-any-py3-none-any.whl"

grc:
	@echo "Installing SpaCy models for Ancient Greek..."
	pip install "grc_odycy_joint_sm @ https://huggingface.co/chcaa/grc_odycy_joint_sm/resolve/main/grc_odycy_joint_sm-any-py3-none-any.whl"
	pip install "grc_proiel_sm @ https://huggingface.co/Jacobo/grc_proiel_sm/resolve/main/grc_proiel_sm-any-py3-none-any.whl"
	pip install "grc_proiel_lg @ https://huggingface.co/Jacobo/grc_proiel_lg/resolve/main/grc_proiel_lg-any-py3-none-any.whl"
	pip install "grc_perseus_sm @ https://huggingface.co/Jacobo/grc_perseus_sm/resolve/main/grc_perseus_sm-any-py3-none-any.whl"
	pip install "grc_perseus_lg @ https://huggingface.co/Jacobo/grc_perseus_lg/resolve/main/grc_perseus_lg-any-py3-none-any.whl"

la:
	@echo "Installing SpaCy models for Latin..."
	pip install "la_core_web_sm @ https://huggingface.co/latincy/la_core_web_sm/resolve/main/la_core_web_sm-any-py3-none-any.whl"
	pip install "la_core_web_md @ https://huggingface.co/latincy/la_core_web_md/resolve/main/la_core_web_md-any-py3-none-any.whl"
	pip install "la_core_web_lg @ https://huggingface.co/latincy/la_core_web_lg/resolve/main/la_core_web_lg-any-py3-none-any.whl"

install:
	tlmgr init-usertree
	tlmgr install xtabular
	tlmgr install bibleref
	tlmgr install bibleref-french
	tlmgr install ekdosis

process:
	lualatex -interaction=batchmode $(files)