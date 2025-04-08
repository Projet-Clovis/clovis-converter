# Clovis Converter
A tool to convert Clovis study sheets and flashcards into popular formats (docx, pdf, ...)

# State of the project
## From Clovis to other formats
- [x] Latex
- [ ] Markdown
- [ ] docx
- [ ] PDF (via Latex)
- [ ] PDF (via docx)

## From other formats to Clovis
- [ ] Latex
- [ ] Markdown
- [ ] docx
- [ ] PDF (via Latex)
- [ ] PDF (via docx)

# User documentation
## Convert clovis to tex
```python
from src.from_clovis.to_tex import clovis_to_tex

clovis_to_tex('<h1 class="title">Some h1 title</h1>')
# '\\section{Some h1 title}'

clovis_to_tex('<div class="katex-container"><p class="katex-code">5x+3</p></div>')
# '\\[5x+3\\]'
```

# Developer documentation
## Folder organization

This is the folder organization of the project.

[`📂 src`](https://github.com/Projet-Clovis/clovis-converter/tree/main/src)    
> Contains the source code of the project.

[`📂 tests`](https://github.com/Projet-Clovis/clovis-converter/tree/main/tests)    
> Contains the tests.

## Run tests
Run `uv run pytest`.

## Create stubs for mypy
Use `uv run stubgen file.py` to create stubs (`.pyi` files) for mypy.
