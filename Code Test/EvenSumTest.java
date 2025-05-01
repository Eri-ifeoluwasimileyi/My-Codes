 import java.util.Scanner;

public class EvenSumTest {
    public static void main(String[] args) {
     Scanner input = new Scanner(System.in);

	int evenSum = 0;
	int oddSum = 0;
	int evenSumCounter = 0;
	
	

	for(int counter = 0; counter < 5; counter = counter + 1) {
	System.out.print("Enter another integer: ");
	int number = input.nextInt();	

	if(number % 2 == 0) {
	evenSum = evenSum + number;
	evenSumCounter = evenSumCounter + 1;
	}
	if(number % 2 != 0) {
	oddSum = oddSum + number;
	}
	
	}
	
	int average = evenSum / evenSumCounter;

	System.out.println("Sum of even integers: " + evenSum);
	System.out.println("Sum of odd integers: " + oddSum);
   	System.out.println("Average of even integers: " + average);
  
   }
}