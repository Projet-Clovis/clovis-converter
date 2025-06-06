from typing import Final

from src.from_clovis.to_clovis import clovis_to_clovis

from tests.utils import check_files

folder_exclude_list: Final[list[str]] = ["block/subject"]


def test_files() -> None:
    check_files(clovis_to_clovis, "clovis-old.html", "clovis.html", folder_exclude_list)
