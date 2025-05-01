  import java.util.Scanner;

public class MortgageCalculator {
    public static void main(String[] args) {
    Scanner input = new Scanner(System.in);


	System.out.print("Enter principal amount: ");
	double principal = input.nextDouble();


	System.out.print("Enter the annual interest Rate: ");
	double annualInterestRate = input.nextDouble();

	System.out.print("Enter the duration in Years: ");
	double numberOfYears = input.nextDouble();
	
	double monthlyInterestRate = (annualInterestRate / 100)/12;
	double numberOfMonths = numberOfYears * 12;


	double part1 = monthlyInterestRate * Math.pow((1 + monthlyInterestRate),numberOfMonths);

	double part2 = Math.pow((1 + monthlyInterestRate), numberOfMonths) - 1;
	
	double mortgage = principal * (part1/part2);

	System.out.printf("Your monthly payment is $%.2f", mortgage);
	
   }
}