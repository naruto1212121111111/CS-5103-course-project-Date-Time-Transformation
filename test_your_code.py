import unittest
from datetime import datetime
import pytz
from date_timezone import transform_datetime


class TestTransformDateTime(unittest.TestCase):

    def test_transform_datetime_utc_to_pacific(self):
        result = transform_datetime("2023-03-11 16:30:00", "UTC", "US/Pacific")
        expected = "03/11/2023 Saturday 08:30"
        self.assertEqual(result, expected)

    def test_transform_datetime_pacific_to_utc(self):
        result = transform_datetime("2023-03-11 16:30:00", "US/Pacific", "UTC")
        expected = "03/12/2023 Sunday 00:30"
        self.assertEqual(result, expected)

    def test_transform_datetime_utc_to_london(self):
        result = transform_datetime("2023-03-11 16:30:00", "UTC",
                                    "Europe/London")
        expected = "03/11/2023 Saturday 16:30"
        self.assertEqual(result, expected)

    def test_transform_datetime_london_to_ny(self):
        result = transform_datetime("2023-03-11 16:30:00", "Europe/London",
                                    "US/Eastern")
        expected = "03/11/2023 Saturday 11:30"  # Updated expected value
        self.assertEqual(result, expected)

    def test_transform_datetime_london_to_tokyo(self):
        result = transform_datetime("2023-03-11 16:30:00", "Europe/London",
                                    "Asia/Tokyo")
        expected = "03/12/2023 Sunday 01:30"
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
