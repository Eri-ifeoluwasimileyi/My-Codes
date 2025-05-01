import java.util.Scanner;
import java.util.Random;

public class GameWhile {
    public static void main(String... args) {
	
	Scanner collector = new Scanner(System.in);
	Random random = new Random();

	int guessNumber = 0;
	int computerGuess = random.nextInt(11);
	int mysteryCounter = 1;

	while(mysteryCounter <= 3){

	System.out.print("Enter a number between 0-10: ");
	guessNumber = collector.nextInt();
	mysteryCounter = mysteryCounter + 1;

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