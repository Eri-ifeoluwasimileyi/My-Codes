import java.util.Scanner;
import java.util.Random;

public class MysteryGameLoop {
    public static void main(String... args) {
	
	Scanner collector = new Scanner(System.in);
	Random random = new Random();

	int guessNumber = 0;
	int computerGuess = random.nextInt(11);

	for(int mysteryCounter = 1; mysteryCounter <= 3; mysteryCounter = mysteryCounter + 1){

	System.out.print("Enter a number between 0-10: ");
	guessNumber = collector.nextInt();

	if(guessNumber < 0 || guessNumber > 10){
		System.out.println("BITCH, DON'T DO THAT");
		mysteryCounter = mysteryCounter + 3;
	}
	else 
	
	if(guessNumber > computerGuess) {
		System.out.println("TOO HIGH BABY, TRY AGAIN");
		}
	else
	
	if(guessNumber < computerGuess) {
		System.out.println("TOO LOW BABY, TRY AGAIN");
		}
	else

	if(guessNumber == computerGuess) {
		System.out.println("YOU WON SWEETIE");
		mysteryCounter = mysteryCounter + 3;
		}
	else{}

	
	}

	
	

	
	

	
























   }
} 