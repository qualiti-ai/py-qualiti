from pathlib import Path

import pytest
import typer

from qualiti import ai, attributer, utils


def test_get_all_files_recursively():
    root_dir = Path("examples")
    file_list = utils.get_all_files_from_directory(root_dir)
    assert file_list == [
        Path("examples/StoryView.tsx"),
        Path("examples/plans.component.html"),
        Path("examples/SubComponents/StoryView copy.tsx"),
    ]


def test_set_file_output_path():
    path = Path("examples/StoryView.tsx")
    output_path = attributer._set_output_path(path, inplace=True)
    assert output_path == path

    output_path = attributer._set_output_path(path, inplace=False)
    assert output_path == Path("examples/StoryView.testids.tsx")


def test_validate_file_path():
    path = Path("examples/StoryView.tsx")
    validated_path = utils.validate_path(path)
    assert validated_path == path


def test_validate_directory_path():
    path = Path("examples")
    validated_path = utils.validate_path(path)
    assert validated_path == path


def test_validate_path_is_not_provided():
    with pytest.raises(typer.BadParameter):
        utils.validate_path(None)


def test_validate_directory_does_not_exist():
    with pytest.raises(typer.BadParameter):
        utils.validate_path(Path("examples/StoryView"))


def test_validate_file_does_not_exist():
    with pytest.raises(typer.BadParameter):
        utils.validate_path(Path("examples/NonExistentFile.html"))
