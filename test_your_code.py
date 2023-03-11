import date_timezone


def test_transform_datetime():
    # First test case
    input_str = "2023-03-11 15:30:00"
    original_timezone_str = "US/Pacific"
    target_timezone_str = "Asia/Kolkata"
    expected_output_str = "2023-03-12 04:00:00 IST+0530"
    actual_output_str = date_timezone.transform_datetime(
        input_str, original_timezone_str, target_timezone_str)
    assert actual_output_str == expected_output_str, f"Expected {expected_output_str}, but got {actual_output_str}"

    # Second test case
    input_str = "2022-12-31 23:59:59"
    original_timezone_str = "America/New_York"
    target_timezone_str = "Asia/Kolkata"
    expected_output_str = "2023-01-01 10:29:59 IST+0530"
    actual_output_str = date_timezone.transform_datetime(
        input_str, original_timezone_str, target_timezone_str)
    assert actual_output_str == expected_output_str, f"Expected {expected_output_str}, but got {actual_output_str}"
