from pathlib import Path

from qualiti import utils


def test_get_all_files_recursively():
    root_dir = Path("examples")
    file_list = utils.get_all_files_from_directory(root_dir)
    assert file_list == [Path("examples/StoreView.tsx"), Path("examples/SubComponents/StoreView copy.tsx")]
