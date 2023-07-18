def get_min_cost(num_array: list) -> int:
    num_array.sort(reverse=True)
    cost = 0
    for index in range(len(num_array)):
        cost += num_array[index] * (index + 1)
    return cost


try:
    nums_array = list(map(int, input("Enter integers separated by space : ").split()))
    print("Therefore, the minimum cost is : ", get_min_cost(nums_array))
except ValueError:
    print("Invalid Input. Please Enter only integers")
