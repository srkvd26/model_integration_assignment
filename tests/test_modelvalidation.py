import pytest
from utils.normalize_values import Normalizer
from utils.risk_calculation import risk_calculation
from utils.excel_read import ExcelRead


excel_data = ExcelRead.read("data/testdata.xlsx")


@pytest.mark.parametrize("row", excel_data, ids=lambda row: f"input={row}")
def test_model_prediction(row, logger):
    
    # Read input values
    is_diabetic = row.get("is_diabetic")
    spo2 = row.get("spo2")
    temp = row.get("temperature")
    age = row.get("age")
    heart_rate = row.get("heart rate")

    # Expected output values
    expected_probability = float(row.get("probability"))
    expected_label = row.get("label")

    # Normalizing the values
    n_dbt, n_spo2, n_temp, n_age, n_hrate = Normalizer.normalize_values(
        int(is_diabetic),
        float(spo2),
        float(temp),
        int(age),
        int(heart_rate)
    )

    # Passing normalized values to the model
    actual_probability, actual_label = risk_calculation(n_dbt, n_spo2, n_temp, n_age, n_hrate)

    logger.info(
        f"Running test case | input=({is_diabetic}, {spo2}, {temp}, {age}, {heart_rate}) "
        f"| expected=({expected_probability}, {expected_label}) "
        f"| actual=({actual_probability}, {actual_label})"
    )

    # Assertions
    assert actual_probability == expected_probability, (
        f"Mismatch in probability: Expected={expected_probability}, Got={actual_probability}"
    )
    assert actual_label == expected_label, (
        f"Mismatch in label: Expected={expected_label}, Got={actual_label}"
    )