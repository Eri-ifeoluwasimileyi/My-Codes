 import java.util.Scanner;

public class EvenOddSum {
    public static void main(String[] args) {
     Scanner input = new Scanner(System.in);

	int evenSum = 0;
	int oddSum = 0;

	
    System.out.print("Enter first integer: ");
    int number1 = input.nextInt();

    System.out.print("Enter second integer: ");
    int number2 = input.nextInt();

    System.out.print("Enter third integer: ");
    int number3 = input.nextInt();

    System.out.print("Enter fourth integer: ");
    int number4 = input.nextInt();

    System.out.print("Enter fifth integer: ");
    int number5 = input.nextInt();

	if(number1 % 2 == 0) {
	   evenSum = evenSum + number1;
	} 
	if(number1 % 2 != 0) {
	   oddSum = oddSum + number1;
	}
	
	if(number2 % 2 == 0) {
	   evenSum = evenSum + number2;
	} 
	if(number2 % 2 != 0) {
	   oddSum = oddSum + number2;
	}
	
	if(number3 % 2 == 0) {
	   evenSum = oddSum + number3;
	} 
	if(number3 % 2 != 0) {
	   oddSum = oddSum + number3;
	}
	
	if(number4 % 2 == 0) {
	   evenSum = evenSum + number4;
	}
	if(number4 % 2 != 0) {
	   oddSum = oddSum + number4;
	}

	if(number5 % 2 == 0) {
	   evenSum = evenSum + number5;
	} 
	if(number5 % 2 != 0) {
	   oddSum = oddSum + number5;
	}

    System.out.println("Sum of even integers: " + evenSum);
    System.out.println("Sum of odd integers: " + oddSum);	
  
   }
}