
import unittest

from src.estimator import MaterialEstimator, ValidationError


class MaterialEstimatorTests(unittest.TestCase):
    def test_concrete_estimate(self) -> None:
        result = MaterialEstimator.concrete(10, 10, 4, 10)
        self.assertEqual(result.cubic_yards, 1.23)
        self.assertEqual(result.cubic_yards_with_waste, 1.36)
        self.assertGreater(result.bags_80_lb, 0)

    def test_aggregate_estimate(self) -> None:
        result = MaterialEstimator.aggregate(20, 10, 6, 10)
        self.assertEqual(result.cubic_yards, 3.7)
        self.assertEqual(result.cubic_yards_with_waste, 4.07)
        self.assertEqual(result.tons, 5.7)

    def test_soil_estimate(self) -> None:
        result = MaterialEstimator.soil(30, 20, 1, 10, 15)
        self.assertEqual(result.cubic_yards, 22.22)
        self.assertEqual(result.cubic_yards_with_waste, 24.44)
        self.assertEqual(result.compacted_cubic_yards, 20.78)

    def test_rejects_negative_values(self) -> None:
        with self.assertRaises(ValidationError):
            MaterialEstimator.concrete(-1, 10, 4)

    def test_rejects_invalid_compaction(self) -> None:
        with self.assertRaises(ValidationError):
            MaterialEstimator.soil(10, 10, 1, compaction_percent=100)


if __name__ == "__main__":
    unittest.main()
