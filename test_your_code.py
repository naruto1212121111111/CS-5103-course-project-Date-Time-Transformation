import unittest
from date_timezone import transform_datetime


class TestTransformDateTime(unittest.TestCase):

    def test_transform_datetime_london_to_ny(self):
        result = transform_datetime("2023-03-11 08:30:00", "Europe/London",
                                    "US/Eastern")
        expected = "03/11/2023 Saturday 03:30"
        self.assertEqual(result, expected)

    def test_transform_datetime_sydney_to_berlin(self):
        result = transform_datetime("2023-03-12 14:30:00", "Australia/Sydney",
                                    "Europe/Berlin")
        expected = "03/12/2023 Sunday 04:30"
        self.assertEqual(result, expected)

    def test_transform_datetime_newyork_to_losangeles(self):
        result = transform_datetime("2023-03-11 19:30:00", "US/Eastern",
                                    "US/Pacific")
        expected = "03/11/2023 Saturday 16:30"
        self.assertEqual(result, expected)

    def test_transform_datetime_pacific_to_kolkata(self):
        result = transform_datetime("2023-11-01 16:30:00", "US/Pacific",
                                    "Asia/Kolkata")
        expected = "11/02/2023 Thursday 05:00"
        self.assertEqual(result, expected)

    def test_transform_datetime_dst_outside_period(self):
        result = transform_datetime("2023-12-01 14:30:00", "Europe/London",
                                    "US/Eastern")
        expected = "12/01/2023 Friday 09:30"
        self.assertEqual(result, expected)

    def test_transform_datetime_no_dst(self):
        result = transform_datetime("2023-07-01 14:30:00", "Europe/London",
                                    "Asia/Kolkata")
        expected = "07/01/2023 Saturday 19:00"
        self.assertEqual(result, expected)

    def test_transform_datetime_timezone_abbreviation(self):
        result = transform_datetime("2023-07-01 14:30:00", "GMT",
                                    "Asia/Kolkata")
        expected = "07/01/2023 Saturday 20:00"
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
