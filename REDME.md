# Acceptance Test + Pytest-bdd + Playwright

<details>

<summary> Setup </summary>

#### Clone the repo

`git clone ....`

`cd pytest_bdd_playwright`

Active a virtualenv to the project with Python 3+

#### Libs

Instale as Bibliotecas a baixo:

`pip install pytest-bdd pytest-playwright`

ou

`pip install -r requirements.txt`

Instalar Browsers of Playwright

A partir da execução do código-fonte:

`python playwright_install.py` (Neste caso selecione navegadores por CLI)

ou 

`plawright install`

</details>

<details>

<summary> Run Tests </summary>

**Executar todos os testes**

`pytest`

**Executar modo detalhado**

`pytest -v` 

da raiz do projeto.

#### Para executar um teste individual por marca de recuros

`pytest -k "tag1"`

Outro exemplo

`pytest -k "tag1 and tag2"`

</details>

<details>

<summary> Gerar passo de Features </summary>

`pytest-bdd generate <feature file name> .. <feature file nameN>`

Gerar etapas do arquivo (file)

`pytest-bdd generate features/some.feature > tests/steps/test_some.py`

Gerar apenas Steps ausentes

`pytest --generate-missing --feature tests/features`

Outro exemplo

`pytest --generate-missing --feature tests/features/pokedex.feature`

</details>

<details>

<summary> References </summary>

https://pytest-bdd.readthedocs.io/en/latest/#example

https://docs.pytest.org/en/6.2.x/

https://playwright.dev/python/docs/test-runners#usage

</details>