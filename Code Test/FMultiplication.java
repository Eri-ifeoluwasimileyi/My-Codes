import java.util.Scanner;
public class Multiplication{
    public static void main(String[] args){
	Scanner input = new Scanner(System.in);

	System.out.print("Enter first integer: ");
	float number1 = input.nextfloat();

	System.out.print("Enter second integer: ");
	float number2 = input.nextfloat();

	float multiply = number1 * number2;

	System.out.printf("Answer is %f%n", multiply);
    }
}