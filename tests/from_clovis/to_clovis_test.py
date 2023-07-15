from typing import Final

from src.from_clovis.to_clovis import clovis_to_clovis
from ..utils import check_files

folder_exclude_list: Final = ["subject"]


def test_files():
    check_files(clovis_to_clovis, "clovis-old.html", "clovis.html", folder_exclude_list)
