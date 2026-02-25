"""Test main.py."""

from collections.abc import Callable, Iterator, Sequence
from typing import Final
from unittest.mock import MagicMock, call, patch

import pytest

import main

type Numeric = int | float | complex

type NumericOrSequence = Numeric | Sequence


class TestAdd:
    """Test add."""

    @pytest.fixture(scope="class")
    def add(
        self,
    ) -> Callable[
        [Numeric, Numeric, Numeric],
        Numeric,
    ]:
        return main.add

    def test_add_default_values(
        self,
        add: Callable[[], Numeric],
    ) -> None:
        expected: Final[Numeric] = -2.1 - 1j

        assert add() == expected

    def test_add_type_error(
        self,
        add: Callable[
            [Sequence, Numeric, Sequence],
            None,
        ],
    ) -> None:
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
        if isinstance(expected, float):
            assert add(arg1, arg2, arg3) == pytest.approx(expected, abs=1e-2)
        else:
            assert add(arg1, arg2, arg3) == expected


@patch("main.str_find", spec_set=True, autospec=True)
@patch("main.str_count", spec_set=True, autospec=True)
class TestFindSubstring:
    """Test find_substring."""

    @pytest.fixture(scope="class")
    def find_substring(
        self,
    ) -> Callable[[str, str, int | None, int | None], Iterator[int]]:
        return main.find_substring

    @pytest.fixture(params=[TypeError, AttributeError])
    def error(self, request: pytest.FixtureRequest) -> type[Exception]:
        return request.param

    def test_find_substring_default_values(
        self,
        mock_str_count: MagicMock,
        mock_str_find: MagicMock,
        find_substring: Callable[[], Iterator[int]],
    ) -> None:
        expected: Final[list[int]] = [9, 17, 25]

        mock_str_count.return_value = len(expected)
        mock_str_find.side_effect = expected

        assert list(find_substring()) == expected

        assert mock_str_count.call_count == 1
        assert mock_str_find.call_count == len(expected)

        mock_str_count.assert_called_once_with(
            sub="t",
            string="i love python, git and github.",
            start=0,
            end=None,
        )

        mock_str_find.assert_any_call(
            sub="t",
            string="i love python, git and github.",
            start=10,
            end=None,
        )

        mock_str_find.assert_called_with(
            sub="t",
            string="i love python, git and github.",
            start=18,
            end=None,
        )

        mock_str_count.assert_has_calls(
            [call(sub="t", string="i love python, git and github.", start=0, end=None)],
        )

        # mock_str_find.assert_has_calls(mock_str_find.call_args_list)
        mock_str_find.assert_has_calls(
            [
                call(
                    sub="t",
                    string="i love python, git and github.",
                    start=0,
                    end=None,
                ),
                call(
                    sub="t",
                    string="i love python, git and github.",
                    start=10,
                    end=None,
                ),
                call(
                    sub="t",
                    string="i love python, git and github.",
                    start=18,
                    end=None,
                ),
            ],
        )

    def test_find_substring_none_found(
        self,
        mock_str_count: MagicMock,
        mock_str_find: MagicMock,
        find_substring: Callable[[str, str], Iterator[int]],
    ) -> None:
        mock_str_count.return_value = 0
        mock_str_find.return_value = -1

        assert list(find_substring("2", "python")) == [-1]

        mock_str_count.assert_called_once_with("2", "python", start=0, end=None)
        mock_str_find.assert_not_called()

    def test_find_substring_error(
        self,
        mock_str_count: MagicMock,
        mock_str_find: MagicMock,
        error: type[Exception],
        find_substring: Callable[[], Iterator[int]],
    ) -> None:
        mock_str_count.side_effect = error
        mock_str_find.return_value = None

        with pytest.raises(error) as exception_info:
            assert list(find_substring()) == [None]
        assert exception_info.type is error

        if error is TypeError:
            assert "TypeError()" in str(exception_info)

        elif error is AttributeError:
            assert "AttributeError()" in str(exception_info)

        assert mock_str_count.call_count == 1
        mock_str_find.assert_not_called()

    @pytest.mark.parametrize(
        ("sub", "string", "start", "end", "expected"),
        [
            ("t", "test $A", 0, None, [0, 3]),
            ("$", "test $A", 0, None, [5]),
            (" ", "it is  $A", 2, 7, [2, 5, 6]),
            ("", "Where", 0, None, [0, 1, 2, 3, 4, 5, 6]),
            pytest.param("h", "the", 0, None, [1], marks=pytest.mark.xfail),
        ],
    )
    def test_find_substring(
        self,
        mock_str_count: MagicMock,
        mock_str_find: MagicMock,
        sub: str,
        string: str,
        start: int,
        end: int,
        expected: list[int],
        find_substring: Callable[[str, str, int | None, int | None], Iterator[int]],
    ) -> None:
        match expected:
            case [0, 3]:
                mock_str_count.return_value = len(expected)
                mock_str_find.side_effect = expected

                assert list(find_substring(sub, string, start, end)) == expected

                assert mock_str_count.call_count == 1
                assert mock_str_find.call_count == len(expected)

                mock_str_count.assert_has_calls(
                    [call(sub, string, start, end)],
                )
                mock_str_find.assert_has_calls(
                    [
                        call(sub, string, start, end),
                        call(sub, string, 1, end),
                    ],
                )

            case [5]:
                mock_str_count.return_value = 1
                mock_str_find.side_effect = expected

                assert list(find_substring(sub, string, start, end)) == expected

                assert mock_str_count.call_count == 1
                assert mock_str_find.call_count == 1

                mock_str_count.assert_called_once_with(
                    sub,
                    string,
                    start,
                    end,
                )
                mock_str_find.assert_called_once_with(
                    sub,
                    string,
                    start,
                    end,
                )

            case [2, 5, 6]:
                mock_str_count.return_value = len(expected)
                mock_str_find.side_effect = expected

                assert list(find_substring(sub, string, start, end)) == expected

                assert mock_str_count.call_count == 1
                assert mock_str_find.call_count == len(expected)

                assert mock_str_count.called
                assert mock_str_find.called

                mock_str_find.assert_any_call(sub, string, 6, end)

            case [0, 1, 2, 3, 4, 5, 6]:
                mock_str_count.return_value = len(expected)
                mock_str_find.side_effect = expected

                assert list(find_substring(sub, string, start, end)) == expected

                assert mock_str_count.call_count == 1
                assert mock_str_find.call_count == len(expected)

            case [1]:
                mock_str_count.return_value = 1
                mock_str_find.return_valuet = 0

                assert list(find_substring(sub, string, start, end)) == expected
