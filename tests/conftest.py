import pathlib

import pytest
from testbook import testbook

NOTEBOOK = pathlib.Path(__file__).resolve().parent.parent / "exercises.ipynb"


@pytest.fixture(scope="session")
def tb():
    """Execute exercises.ipynb once and share the kernel across all tests."""
    with testbook(
        str(NOTEBOOK),
        execute=True,
        resources={"metadata": {"path": str(NOTEBOOK.parent)}},
    ) as tb:
        yield tb
