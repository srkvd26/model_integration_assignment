import pytest
from utils.normalize_time import normalize_time
from utils.excel_read import ExcelRead


excel_data = ExcelRead.read("data/testdata.xlsx")


@pytest.mark.parametrize("row", excel_data, ids=lambda row: f"input={row['input']}")
def test_validate_time_normalization(row, logger):
    input_value = row.get("input", "")
    expected = row.get("expected_output", "")

    try:
        actual = normalize_time.normalize_time_string(input_value)
    except Exception as e:
        actual = f"Error: {e}"

    if expected.startswith('"') and expected.endswith('"'):
        expected = expected[1:-1]

    logger.info(
        f"Running test case | input='{input_value}' | expected='{expected}' | actual='{actual}'"
    )

    assert actual == expected, (
        f"Mismatch for input '{input_value}': Expected='{expected}', Got='{actual}'"
    )
