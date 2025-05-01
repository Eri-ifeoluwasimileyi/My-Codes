import java.util.Scanner;

public class ComparingIntegers {
    public static void main(String[] args){
    Scanner input = new Scanner(System.in);

	System.out.print("Enter an integer: ");
	int number = input.nextInt();
	
	int square = number * number;
	
	System.out.println("Comparing " + number + " with 100: ");

	if(number > 100 && square > 100) {
	   System.out.println(number + " and " + square + " , is greater than 100");
	}
	else if(square == 100){
		System.out.println(square + " , is equal to 100");
	}
	if(number < 100 && square < 100) {
	   System.out.println(number + " and " + square + " , is less than 100");
	}
	else if(square == 100){
		System.out.println(square + " , is equal to 100"); 
	}
	if(number != 100 && square != 100) {
	   System.out.println(number + " and " + square + " , is not equal to 100");
	}
	else if(square == 100){
		System.out.println(square + " , is equal to 100");
	} 
	
	
    }
}