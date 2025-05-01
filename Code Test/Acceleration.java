import java.util.Scanner;

public class Acceleration {
    public static void main(String[] args) {
      Scanner input = new Scanner(System.in);

	System.out.print("Enter Starting Velocity: ");
	float velocity0 = input.nextFloat();

	System.out.print("Enter Ending Velocity: ");
	float velocity1 = input.nextFloat();

	System.out.print("Enter the time Span: ");
	float time = input.nextFloat();

	float acceleration = (v1 - v0)/t;

	System.out.println("The Average Accelaration is " + acceleration);


   }

}
   