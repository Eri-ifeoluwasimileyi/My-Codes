import java.util.Scanner;

public class Nokia3310Menu {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int choice;

        do {
            scanner = printMenu();
            System.out.print("Enter your choice: ");
            choice = scanner.nextInt();
            scanner.nextLine(); // Consume newline

            switch (choice) {
                case 1:
                    System.out.println("Calling...");
                    break;
                case 2:
                    handleMessagesMenu(scanner);
                    break;
                case 3:
                    System.out.println("Contacts...");
                    break;
                case 4:
                    System.out.println("Settings...");
                    break;
                case 0:
                    System.out.println("Exiting menu.");
                    break;
                default:
                    System.out.println("Invalid choice. Please try again.");
            }
        } while (choice != 0);

        scanner.close();
}
}