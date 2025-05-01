import java.util.Scanner;

public class ForLoopTest {
    public static void main(String[] args) {
	Scanner operator = new Scanner(System.in);

	System.out.print("Enter a number: ");
	int number = operator.nextInt();


	for(int counter = 0; counter < 5; counter = counter + 1) {
	System.out.print("Enter second number: ");
	int number2 = operator.nextInt();
	
	System.out.println(number +  " and " + number2);
	

		
		

	}
	
   } 
}






/*Every loop has these three things to run,
the initialized variable = which give the variable an initial value e.g. int var = 0;
the condition = which check if the statement is true or false
the increment = this works by adding 1 to the counter */
