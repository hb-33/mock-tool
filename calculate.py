def calculate_total(numbers):
    # TODO: Fix the bug where the sum is incorrect
    total = 0
    for n in numbers:
        total += n
    return total

if __name__ == "__main__":
    nums = [10, 20, 30]
    print("Total:", calculate_total(nums))
