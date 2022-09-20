namespace Tasks {

    static class Task1 {
        
        public static int CheckLengthTwoSubstrings(string str1, string str2){
            int substrings_count = 0;
            
            for (int i=0; i < str1.Length - 1; i++){
                int indexInStr2 = str2.IndexOf(str1[i]);
                if (indexInStr2 >= 0 & indexInStr2 < str2.Length - 1) {
                    if (str2[indexInStr2+1] == str1[i+1])
                        substrings_count++;
                }
            }
            return substrings_count;
        }

    }

    static class Task2 {
        public static bool CheckIfNumsEvenOrOdd(int num1, int num2){
            return (num1 + num2) % 2 == 0;
        }
    }
}