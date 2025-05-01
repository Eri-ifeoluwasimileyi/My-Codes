import java.util.Scanner;

public class SumOfDigit {
    public static void main(String[] args){
    Scanner input = new Scanner(System.in);
	
	System.out.print("Enter a number: ");
	int number = input.nextInt();


	if(number <= 0 || number >= 1000){
	System.out.print("Don't print");
	} 
	if(number > 0 && number < 1000){
	
	int digit1 = number % 10;
	int remainder = number / 10;

	int digit2 = remainder % 10;
	remainder = remainder / 10;

 	int digit3 = remainder % 10;
	remainder = remainder / 10;

	int sum = digit1 + digit2 + digit3;

	System.out.printf("The sum of the digits in %d is %d", number, sum); 
	}
  }

}