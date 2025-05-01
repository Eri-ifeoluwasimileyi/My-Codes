import java.util.Scanner;

public class StudentGrade {
	public static void main(String[] args) {
	Scanner input = new Scanner(System.in);


int passedCounter = 0;
int failedCounter = 0;
int studentCounter = 1;

	while(studentCounter <= 10) {
	System.out.print("Enter Result: ");
	int examResult = input.nextInt();

	if(examResult == 1 ) {
		passedCounter = passedCounter + 1;
		}
	else

	if(examResult == 2) {
		failedCounter = failedCounter + 1;
		}

	else {
	System.out.print("INVALID INPUT NIGGA!!!");
	}

	studentCounter = studentCounter + 1;

	}

	System.out.println("Number of passes are " + passedCounter);
	System.out.println("Number of failures are " + failedCounter);

	if(passedCounter > 8){
	System.out.println("Bonus to Instructor! ");
	}



   }
}