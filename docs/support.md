# Support

In association rules mining, the support of a rule is the proportion of 
transactions that contain the premise and the conclusion of the rule. 
The support of a rule is an indication of how frequently the rule occurs 
in the dataset.

## More Information

- https://en.wikipedia.org/wiki/Association_rule_learning#Support

## Pseudocode

```text
Algorithm: Calculate_Support
Input: Dataset (D), Itemset (I)
Output: Support value for Itemset

1. Initialize count = 0
2. For each transaction T in Dataset D:
    a. If Itemset I is a subset of Transaction T:
        i. Increment count by 1
3. Support = count / Total number of transactions in Dataset D
4. Return Support
```