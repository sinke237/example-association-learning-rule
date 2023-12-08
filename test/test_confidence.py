import unittest

from src.confidence import confidence as calculate_confidence
from src.support import support as calculate_support


class TestConfidenceCalculation(unittest.TestCase):

    def test_calculate_confidence(self):
        # Mock dataset
        dataset = [
            ['bread', 'milk'],
            ['bread', 'diaper', 'beer', 'eggs'],
            ['milk', 'diaper', 'beer', 'cola'],
            ['bread', 'milk', 'diaper', 'beer'],
            ['bread', 'milk', 'diaper', 'cola']
        ]
        rule = (['bread'], ['milk'])  # Rule: Bread -> Milk

        # Calculate support values
        support_bread_milk = calculate_support(dataset, ['bread', 'milk'])
        support_bread = calculate_support(dataset, ['bread'])

        # Expected confidence
        expected_confidence = support_bread_milk / support_bread if support_bread != 0 else 0.0

        # Calculate confidence
        confidence = calculate_confidence(dataset, rule)

        # Assert
        self.assertAlmostEqual(confidence, expected_confidence)


if __name__ == '__main__':
    unittest.main()
