# Лабораторная работа №7
### Задание A 
```
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

```
## Выполненные тесты 
![im01.png](/images/lab07_1.png)
### Задание B 
```
import pytest
import json
import csv
import sys
import os
from pathlib import Path

current_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.dirname(current_dir)
sys.path.insert(0, src_dir)

from src.lab05.json_csv import json_to_csv, csv_to_json


class TestJsonToCsv:
    def test_basic_conversion(self, tmp_path):
        src = tmp_path / "test.json"
        dst = tmp_path / "test.csv"
        data = [
            {"name": "Alice", "age": 22, "city": "Moscow"},
            {"name": "Bob", "age": 25, "city": "SPb"},
        ]
        src.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
        json_to_csv(str(src), str(dst))
        with open(dst, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            rows = list(reader)
        assert len(rows) == 2
        assert set(rows[0].keys()) == {"name", "age", "city"}
        assert rows[0]["name"] == "Alice"
        assert rows[1]["name"] == "Bob"

    def test_file_not_found(self):
        with pytest.raises(FileNotFoundError):
            json_to_csv("nonexistent.json", "output.csv")

    def test_invalid_json(self, tmp_path):
        src = tmp_path / "invalid.json"
        dst = tmp_path / "output.csv"
        src.write_text("{ invalid json }", encoding="utf-8")
        with pytest.raises(ValueError):
            json_to_csv(str(src), str(dst))


class TestCsvToJson:
    def test_basic_conversion(self, tmp_path):
        src = tmp_path / "test.csv"
        dst = tmp_path / "test.json"
        csv_content = "name,age,city\nAlice,22,Moscow\nBob,25,SPb"
        src.write_text(csv_content, encoding="utf-8")
        csv_to_json(str(src), str(dst))
        with open(dst, "r", encoding="utf-8") as f:
            data = json.load(f)
        assert len(data) == 2
        assert data[0] == {"name": "Alice", "age": "22", "city": "Moscow"}
        assert data[1] == {"name": "Bob", "age": "25", "city": "SPb"}

    def test_file_not_found(self):
        with pytest.raises(FileNotFoundError):
            csv_to_json("nonexistent.csv", "output.json")

    def test_empty_csv(self, tmp_path):
        src = tmp_path / "empty.csv"
        dst = tmp_path / "output.json"
        src.write_text("", encoding="utf-8")
        with pytest.raises(ValueError):
            csv_to_json(str(src), str(dst))


class TestRoundTrip:
    def test_json_csv_json(self, tmp_path):
        original_data = [{"name": "Test", "value": 42}, {"name": "Demo", "value": 24}]
        json1 = tmp_path / "test1.json"
        csv_file = tmp_path / "test.csv"
        json2 = tmp_path / "test2.json"
        json1.write_text(
            json.dumps(original_data, ensure_ascii=False), encoding="utf-8"
        )
        json_to_csv(str(json1), str(csv_file))
        csv_to_json(str(csv_file), str(json2))
        with open(json2, "r", encoding="utf-8") as f:
            final_data = json.load(f)
        assert len(final_data) == len(original_data)
        assert final_data[0]["name"] == original_data[0]["name"]

```

## Выполненные тесты 
![im01.png](/images/lab07_2.png)

## Стиль кода
![im02.png](/images/lab07_black.png)
![im03.png](/images/lab07_check.png)

## Вывод:
Научилась писать модульные тесты на pytest и поддерживать единый стиль кода (black).
Протестировала функции из прошлых лабораторных работ