bool CheckSum(List<int> numbers, int number_to_check) {
    numbers.Sort();

    if (number_to_check < numbers[0]) {
        return false;
    }

    int i = 0;
    int j = numbers.Count - 1;
    int sum;

    while(i != j) {
        if (numbers[j] > number_to_check) j--;

        sum = numbers[i] + numbers[j];

        if (sum == number_to_check) {
            Console.WriteLine(String.Format("{0} + {1} = {2}", numbers[i], numbers[j], number_to_check));
            return true;
        }

        else if (sum < number_to_check)
            i++;
        else
            j--;

    }

    return false;
}



List<int> numbers_list = new List<int>(){1, 2, 9};

Console.WriteLine(CheckSum(numbers_list, 5));
