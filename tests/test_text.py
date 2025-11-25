import pytest
import sys
import os


current_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.dirname(current_dir)
sys.path.insert(0, src_dir)

from src.lib.text import normalize, tokenize, count_freq, top_n


class TestNormalize:
    @pytest.mark.parametrize(
        "source, expected",
        [
            ("ПрИвЕт\nМИр\t", "привет мир"),
            ("ёжик, Ёлка", "ежик, елка"),
            ("Hello\r\nWorld", "hello world"),
            ("  двойные   пробелы  ", "двойные пробелы"),
            ("", ""),
            ("   ", ""),
            ("ТЕСТ123test", "тест123test"),
        ],
    )
    def test_normalize(self, source, expected):
        assert normalize(source) == expected


class TestTokenize:
    @pytest.mark.parametrize(
        "source, expected",
        [
            ("привет мир", ["привет", "мир"]),
            ("hello, world!", ["hello", "world"]),
            ("один два три", ["один", "два", "три"]),
            ("", []),
            ("   ", []),
            ("word", ["word"]),
        ],
    )
    def test_tokenize(self, source, expected):
        assert tokenize(source) == expected


class TestCountFreq:
    def test_basic(self):
        tokens = ["cat", "dog", "cat", "bird", "dog", "cat"]
        result = count_freq(tokens)
        expected = {"cat": 3, "dog": 2, "bird": 1}
        assert result == expected

    def test_empty(self):
        assert count_freq([]) == {}

    def test_single_word(self):
        assert count_freq(["test"]) == {"test": 1}


class TestTopN:
    def test_basic(self):
        freq = {"a": 1, "b": 2, "c": 3, "d": 4}
        result = top_n(freq, 2)
        expected = [("d", 4), ("c", 3)]
        assert result == expected

    def test_tie_breaker(self):
        freq = {"s": 3, "a": 3, "m": 3, "b": 2}
        result = top_n(freq, 3)
        expected = [("a", 3), ("m", 3), ("s", 3)]
        assert result == expected

    def test_n_larger_than_dict(self):
        freq = {"a": 1, "b": 2}
        result = top_n(freq, 5)
        expected = [("b", 2), ("a", 1)]
        assert result == expected

    def test_empty_dict(self):
        assert top_n({}, 5) == []
