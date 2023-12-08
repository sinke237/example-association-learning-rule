import unittest

from src.apriori import apriori as apriori_algorithm


class TestAprioriAlgorithm(unittest.TestCase):

    def test_apriori_frequent_itemsets(self):
        # Mock dataset
        dataset = [
            ['bread', 'milk'],
            ['bread', 'diaper', 'beer', 'eggs'],
            ['milk', 'diaper', 'beer', 'cola'],
            ['bread', 'milk', 'diaper', 'beer'],
            ['bread', 'milk', 'diaper', 'cola']
        ]
        min_support = 0.6  # 60% minimum support

        # Expected frequent itemsets
        expected_frequent_itemsets = {
            ('bread',): 4 / 5,
            ('milk',): 4 / 5,
            ('diaper',): 4 / 5,
            ('bread', 'milk'): 3 / 5,
            ('bread', 'diaper'): 3 / 5,
            ('milk', 'diaper'): 3 / 5
        }

        # Run Apriori algorithm
        frequent_itemsets, _ = apriori_algorithm(dataset, min_support)

        # Assert
        self.assertEqual(frequent_itemsets, expected_frequent_itemsets)

    def test_apriori_rules(self):
        # Mock dataset
        dataset = [
            ['bread', 'milk'],
            ['bread', 'diaper', 'beer', 'eggs'],
            ['milk', 'diaper', 'beer', 'cola'],
            ['bread', 'milk', 'diaper', 'beer'],
            ['bread', 'milk', 'diaper', 'cola']
        ]
        min_support = 0.6  # 60% minimum support
        min_confidence = 0.7  # 70% minimum confidence

        # Expected rules (adjust based on your logic and implementation)
        # Format: (antecedent, consequent): confidence
        expected_rules = {
            (frozenset(['bread']), frozenset(['milk'])): 0.75,  # Example confidence, adjust as needed
        }

        # Run Apriori algorithm
        _, generated_rules = apriori_algorithm(dataset, min_support, min_confidence)

        # Convert generated rules to a comparable format
        formatted_generated_rules = {(rule.antecedent, rule.consequent): rule.confidence for rule in generated_rules}

        # Assert that each generated rule is in the expected rules and has the correct confidence
        for rule, confidence in formatted_generated_rules.items():
            self.assertIn(rule, expected_rules)
            self.assertAlmostEqual(confidence, expected_rules[rule])


if __name__ == '__main__':
    unittest.main()
