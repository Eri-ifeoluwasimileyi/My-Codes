import java.util.Scanner;
public class Multiplication{
    public static void main(String[] args){
	Scanner input = new Scanner(System.in);

	System.out.print("Enter first integer: ");
	int number1 = input.nextInt();

	System.out.print("Enter second integer: ");
	int number2 = input.nextInt();

	int multiply = number1 * number2;

	System.out.printf("Answer is %f%n", multiply);
    }
}