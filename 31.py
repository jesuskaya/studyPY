import itertools
from collections import defaultdict
import pandas as pd

# Вхідні дані для варіанту 9
transactions = [
    {0, 2, 4, 6, 8},  # T1
    {2, 4, 6},  # T2
    {0, 2, 6, 8},  # T3
    {2, 4},  # T4
    {0, 2, 6, 8},  # T5
    {0, 2, 4, 6, 8}  # T6
]
items = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
min_support = 0.5
min_confidence = 0.75
total_transactions = len(transactions)


def get_frequent_itemsets(transactions, items, min_support):
    """
    Знаходження частих наборів за алгоритмом Apriori
    """
    item_counts = defaultdict(int)
    frequent_itemsets = []

    # Крок 1: 1-елементні набори
    for item in items:
        for transaction in transactions:
            if item in transaction:
                item_counts[frozenset([item])] += 1
    frequent_itemsets.append({
        itemset: count / total_transactions
        for itemset, count in item_counts.items()
        if count / total_transactions >= min_support
    })

    # Крок 2+: Генерація k-елементних наборів
    k = 2
    while True:
        prev_frequent = frequent_itemsets[-1]
        if not prev_frequent:
            break
        candidates = set()
        for itemset1 in prev_frequent:
            for itemset2 in prev_frequent:
                union_set = itemset1 | itemset2
                if len(union_set) == k:
                    candidates.add(union_set)

        # Підрахунок підтримки для кандидатів
        candidate_counts = defaultdict(int)
        for candidate in candidates:
            for transaction in transactions:
                if candidate.issubset(transaction):
                    candidate_counts[candidate] += 1
        frequent = {
            itemset: count / total_transactions
            for itemset, count in candidate_counts.items()
            if count / total_transactions >= min_support
        }
        if not frequent:
            break
        frequent_itemsets.append(frequent)
        k += 1

    return frequent_itemsets


def generate_association_rules(frequent_itemsets, min_confidence):
    """
    Генерація асоціативних правил із частих наборів
    """
    rules = []
    for k, itemsets in enumerate(frequent_itemsets[1:], start=1):
        for itemset in itemsets:
            for i in range(1, len(itemset)):
                for antecedent in itertools.combinations(itemset, i):
                    antecedent = frozenset(antecedent)
                    consequent = itemset - antecedent
                    support_itemset = frequent_itemsets[k][itemset]
                    support_antecedent = next(
                        (s for fs, s in frequent_itemsets[i - 1].items() if fs == antecedent),
                        0
                    )
                    if support_antecedent == 0:
                        continue
                    confidence = support_itemset / support_antecedent
                    if confidence >= min_confidence:
                        support_consequent = next(
                            (s for fs, s in frequent_itemsets[len(consequent) - 1].items() if fs == consequent),
                            0
                        )
                        lift = confidence / support_consequent if support_consequent != 0 else 0
                        leverage = support_itemset - support_antecedent * support_consequent
                        improvement = support_itemset / (
                                    support_antecedent * support_consequent) if support_antecedent * support_consequent != 0 else 0
                        rules.append({
                            'rule': f"{set(antecedent)} -> {set(consequent)}",
                            'support': support_itemset,
                            'confidence': confidence,
                            'lift': lift,
                            'leverage': leverage,
                            'improvement': improvement
                        })
    return rules


# Виконання алгоритму
frequent_itemsets = get_frequent_itemsets(transactions, items, min_support)
rules = generate_association_rules(frequent_itemsets, min_confidence)

# Виведення результатів
print("Часті набори:")
for k, itemsets in enumerate(frequent_itemsets, start=1):
    print(f"{k}-елементні набори:")
    for itemset, support in itemsets.items():
        print(f"{set(itemset)}: підтримка = {support:.3f}")

print("\nАсоціативні правила:")
df = pd.DataFrame(rules)
if not df.empty:
    df = df.round(3)
    print(df.to_string(index=False))
else:
    print("Немає правил, що задовольняють умови.")