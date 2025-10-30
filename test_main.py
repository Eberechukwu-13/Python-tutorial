"""Test main.py."""

from collections.abc import Callable, Sequence

import pytest

import main

type Numeric = int | float | complex

type NumericOrSequence = Numeric | Sequence


class TestAdd:
    """Test add function."""

    @pytest.fixture(scope="class")
    def add(
        self,
    ) -> Callable[
        [NumericOrSequence, NumericOrSequence, NumericOrSequence],
        NumericOrSequence,
    ]:
        """Generate add function."""
        return main.add

    @pytest.mark.parametrize("expected", [-2.1 - 1j])
    def test_add_default_values(
        self,
        add: Callable[[], Numeric],
        expected: Numeric,
    ) -> None:
        """Test add function with default values."""
        assert add() == expected

    def test_add_type_error(
        self,
        add: Callable[
            [NumericOrSequence, NumericOrSequence, NumericOrSequence],
            NumericOrSequence,
        ],
    ) -> None:
        """Test add function type error."""
        with pytest.raises(TypeError) as exception_info:
            add("1", 2, ())
        assert exception_info.type is TypeError

    @pytest.mark.parametrize(
        ("arg1", "arg2", "arg3", "expected"),
        [
            (10, -2, 50, 58),
            (0.111, 0.3, -0.02, 0.381),
            (True, False, True, 2),
            (100 + 20j, -100 - 20j, -32 + 75j, -32 + 75j),
            ((1,), (2,), (3,), (1, 2, 3)),
            ("i ", "love ", "python & git", "i love python & git"),
            (0, 0, 0, 0),
            (["python"], ["git"], ["github"], ["python", "git", "github"]),
            pytest.param(1, 1, 1, 1, marks=pytest.mark.xfail),
        ],
        ids=[
            "int",
            "float",
            "bool",
            "complex",
            "turple",
            "str",
            "zero",
            "list",
            "xfail",
        ],
    )
    def test_add(
        self,
        add: Callable[
            [NumericOrSequence, NumericOrSequence, NumericOrSequence],
            NumericOrSequence,
        ],
        arg1: NumericOrSequence,
        arg2: NumericOrSequence,
        arg3: NumericOrSequence,
        expected: NumericOrSequence,
    ) -> None:
        """Test add function with multiple arguments.

        Args:
            add (Callable[[NumericOrSequence, NumericOsequence, NumericOrSequence], NumericOrSequence]): _description_.
            arg1 (NumericOrSequence): _description_.
            arg2 (NumericOrSequence): _description_.
            arg3 (NumericOrSequence): _description_.
            expected (NumericOrSequence): expected of the addition of a, b, and c.

        """
        if isinstance(expected, float):
            assert add(arg1, arg2, arg3) == pytest.approx(expected, abs=1e-2)
        else:
            assert add(arg1, arg2, arg3) == expected
