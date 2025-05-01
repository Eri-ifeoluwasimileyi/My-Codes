import java.util.Scanner;

public class LoopTest {
    public static void main(String[] args) {
	Scanner operator = new Scanner(System.in);

	System.out.print("Enter a number: ");
	int number = operator.nextInt();

	int counter = 0;

	while(counter < 5) {
	System.out.print("Enter second number: ");
	int number2 = operator.nextInt();

		if(number > number2) {
		System.out.println(number + " is greater than " + number2);
		}
		else{
		System.out.println(number2  + " is greater than " + number);
		}


	counter = counter + 1;
	

	}
	
   } 
}






/*Every loop has these three things to run,
the initialized variable = which give the variable an initial value e.g. int var = 0;
the condition = which check if the statement is true or false
the increment = this works by adding 1 to the counter */
