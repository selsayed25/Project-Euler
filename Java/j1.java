// Title: 
// Description: If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
// Goal: Find the sum of all the multiples of 3 or 5 below 1000.

public final class j1 {
    public static void main(String[] args) {
        System.out.println(new j1().solution());
    }

    public String solution() {
        int sum = 0;
        
        for (int index = 0; index < 1000; index++) {
            if (index % 3 == 0 || index % 5 == 0) {
                sum += index;
            }
        }

        return Integer.toString(sum);
    }
}