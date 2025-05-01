import java.util.Scanner;

public class SecondHighestScore {
   public static void main(String[] args) {
	Scanner input = new Scanner(System.in);



	String highestScoreName = " "; 
	int  largestNumber = -23456678;

	String secondHighestScoreName = " ";
	int secondLargestNumber = -23456678;
	 

try{
	System.out.print("Enter the number of students: ");
	int number = input.nextInt();
		

	for(int counter = 1; counter <= number; counter = counter + 1) {
		
		
		System.out.print("Enter the student's name: ");
		String name = input.next();

		System.out.print("Score: ");
		int score = input.nextInt();

		if (score > largestNumber) {

			secondLargestNumber = largestNumber;
			secondHighestScoreName = highestScoreName;

			largestNumber = score;
			highestScoreName = name;
		}
		else
		if(score == largestNumber) {
			 largestNumber = score;
			 highestScoreName = highestScoreName + " and " + name;

		}
		else
		if(largestNumber > secondLargestNumber) {
			secondLargestNumber = score;
			secondHighestScoreName = name; 
		}
		else
		if(score == secondLargestNumber)
			 secondLargestNumber = score;
			 secondHighestScoreName = secondHighestScoreName;
			
	}

	if(number <= 0) {
	System.out.println("Invalid input, Enter a valid input!");
	}
	else{	
		System.out.println("The highest score is: " + largestNumber);
		System.out.println("The second highest score is: " + secondLargestNumber);


		System.out.println("Student with the highest score is: "+ highestScoreName);
		System.out.println("Student with the second highest score is: "+ secondHighestScoreName);
	}




}
catch(Exception e) {
		System.out.println("Invalid input, Enter a valid input!");
}
//finally {
	//System.out.print("BITCH FUCKING STOP!!!");
//}	


   }
}