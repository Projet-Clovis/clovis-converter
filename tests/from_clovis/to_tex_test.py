from typing import Final

from src.from_clovis.to_tex import clovis_to_tex
from ..utils import check_files

folder_exclude_list: Final = []


def test_files():
    check_files(clovis_to_tex, "clovis.html", "tex.tex", folder_exclude_list)
