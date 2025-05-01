import java.util.Scanner;
public class Multiplication{
    public static void main(String[] args){
	Scanner input = new Scanner(System.in);

	System.out.print("Enter first integer: ");
	double number1 = input.nextdouble();

	System.out.print("Enter second integer: ");
	double number2 = input.nextdouble();

	double multiply = number1 * number2;

	System.out.printf("Answer is %.2f%n", multiply);
    }
}