from src.from_clovis.to_tex import clovis_to_tex

from tests.utils import check_files


def test_files() -> None:
    check_files(clovis_to_tex, "clovis.html", "tex.tex")
