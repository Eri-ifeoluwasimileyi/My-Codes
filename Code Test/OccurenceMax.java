import java.util.Scanner;

public class OccurenceMax {
    public static void main(String[] args) {
	Scanner input = new Scanner(System.in);

	int counter = 0;
	int largestNumber = -23456678;
	int number = 1;

	do {
		System.out.print("Enter a number and enter 0 to stop: ");
		number = input.nextInt();

		if(number > largestNumber) {
		largestNumber = number;
		counter = 1;
		}
		else
		if(number == largestNumber) {
		counter = counter + 1;
		}

	}
	while(number != 0);
	
	System.out.println("The largest number is: "+ largestNumber);
	System.out.println("The occurence of the largest number is: " + counter);	



   }
}