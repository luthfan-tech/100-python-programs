# 65. Set Union & Intersection

def main():
    # Example sets; replace with input() if you want user input
    A = {1, 2, 3, 4}
    B = {3, 4, 5, 6}

    union_set = A | B          # or A.union(B)
    intersection_set = A & B   # or A.intersection(B)

    print("Set A:", A)
    print("Set B:", B)
    print("Union (A ∪ B):", union_set)
    print("Intersection (A ∩ B):", intersection_set)

if __name__ == "__main__":
    main()

# 66. Check Subset / Superset

def main():
    A = {1, 2, 3, 4, 5}
    B = {2, 3, 4}

    is_B_subset_of_A = B.issubset(A)      # or B <= A
    is_A_superset_of_B = A.issuperset(B)  # or A >= B

    print("Set A:", A)
    print("Set B:", B)
    print("Is B a subset of A?", is_B_subset_of_A)
    print("Is A a superset of B?", is_A_superset_of_B)

if __name__ == "__main__":
    main()

# 67. Symmetric Difference of Sets

def main():
    A = {1, 2, 3, 4}
    B = {3, 4, 5, 6}

    sym_diff = A ^ B  # or A.symmetric_difference(B)

    print("Set A:", A)
    print("Set B:", B)
    print("Symmetric Difference (A Δ B):", sym_diff)

if __name__ == "__main__":
    main()

# 68. Group List of Tuples into Dict

def group_tuples(pairs):
    result = {}
    for key, value in pairs:
        result.setdefault(key, []).append(value)
    return result

def main():
    data = [("a", 1), ("b", 2), ("a", 3), ("c", 4), ("b", 5)]

    grouped = group_tuples(data)

    print("Input list of tuples:", data)
    print("Grouped dictionary:", grouped)

if __name__ == "__main__":
    main()   