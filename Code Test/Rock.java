import java.util.Scanner;
import java.util.Random;

public class Rock {
   public static void main(String[] args) {
	
	Scanner collect = new Scanner(System.in);
	Random random = new Random();

	System.out.print("Scissors (0), Rock (1), Paper (2): ");
	int you = collect.nextInt();
	int comGuess = random.nextInt(3);

	if(you < 0 || you > 2) {
	System.out.print("DUMBASS!!!");
	}
	else{

	if(comGuess == 0){
	System.out.print("Computer is Scissors. ");
	}
	if(comGuess == 1){
	System.out.print("Computer is Rock. ");
	}
	if(comGuess == 2){
	System.out.print("Computer is Paper. ");
	}

	if(you == 0){
	System.out.print("You are Scissors. ");
	}
	if(you == 1){
	System.out.print("You are Rock. ");
	}
	if(you == 2){
	System.out.print("You are Paper. ");
	}


	if(you == comGuess){
	System.out.print("Its a draw");
	}

	if(you == 0 && comGuess == 1){
	System.out.print("Computer won");
	}
	if(you == 1 && comGuess == 0){
	System.out.print("You won");
	}
	if(you == 1 && comGuess == 2){
	System.out.print("Computer won");
	}
	if(you == 2 && comGuess == 1){
	System.out.print("You won");
	}
	if(you == 2 && comGuess == 0){
	System.out.print("Computer won");
	}
	if(you == 0 && comGuess == 2){
	System.out.print("You won");
	}
	
	}
   }
}