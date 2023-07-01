import random
import timeit
import matplotlib.pyplot as plt

def k_select_random(array, k):
    """Finds the k-th largest element in an array using a random pivot.

    Args:
        array: The array to search.
        k: The index of the k-th largest element.

    Returns:
        The k-th largest element in the array.
    """
    start = timeit.default_timer()

    pivot = random.choice(array)
    left = [x for x in array if x < pivot]
    right = [x for x in array if x >= pivot]

    if len(left) == k:
        return pivot
    elif len(left) > k:
        return k_select_random(left, k)
    else:
        return k_select_random(right, k - len(left) - 1)

def k_select_median_of_medians(array, k):

    start = timeit.default_timer()

    n = len(array)
    if n <= 5:
        return sorted(array)[k - 1]

    medians = []
    for i in range(0, n, 5):
        medians.append(sorted(array[i:i + 5])[2])

    pivot = k_select_median_of_medians(medians, n // 5)
    left = [x for x in array if x < pivot]
    right = [x for x in array if x >= pivot]

    if len(left) == k:
        return pivot
    elif len(left) > k:
        return k_select_median_of_medians(left, k)
    else:
        return k_select_median_of_medians(right, k - len(left) - 1)

def main():

    array = [random.randint(0, 1000) for _ in range(10000)]

    runtimes_random = []
    runtimes_median_of_medians = []

    for i in range(1, 10001):
        start = timeit.default_timer()
        k_select_random(array, i)
        runtimes_random.append(timeit.default_timer() - start)

        start = timeit.default_timer()
        k_select_median_of_medians(array, i)
        runtimes_median_of_medians.append(timeit.default_timer() - start)

    plt.plot(runtimes_random, 'bo', label='Random')
    plt.plot(runtimes_median_of_medians, 'ro', label='Median of medians')
    plt.xlabel('Number of iterations')
    plt.ylabel('Runtime (s)')
    plt.legend()
    plt.show()

if __name__ == '__main__':
    main()
