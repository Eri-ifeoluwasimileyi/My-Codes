import java.util.Scanner;

public class Occurence {
   public static void main(String[] args) {
	Scanner input = new Scanner(System.in); 

	int occurence = 0;

	int largestNumber = -23466;
	int count = 0;
	

	while(count != 7887) {	
	System.out.print("Please enter a number: ");
	int number = input.nextInt();
	input.nextLine();
	if(number > largestNumber) {
	largestNumber = number;
	occurence = 1;
	}
	
	else if (number == largestNumber) {
	occurence ++;
	}
	count ++;
	System.out.println("Do you want to continue? press no to end and Enter to continue");
	String no = input.nextLine();

	if(no.equals("no")|| no.equals("No") || no.equals("NO")) {
	break;
}
}
	System.out.println("The largest number is: " + largestNumber);
	if( occurence != 0) {
	System.out.println("The number of occurence is: " + occurence);
}



  }
}