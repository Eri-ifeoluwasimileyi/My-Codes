import java.util.Scanner;

public class Binary {
    public static void main(String[] args){
    Scanner input = new Scanner(System.in);
	
	System.out.print("Enter a number: ");
	int number = input.nextInt();

	System.out.print("Enter another number: ");
	int number2 = input.nextInt();

	int binaryNum = 0;
	String result = " ";

	while(number != 0) {

	binaryNum = number % 2;
	result = binaryNum + result;
	number = number + number2;
	 System.out.print(result);
	}
	
   }
}

	