import java.util.Random;

public class Main {
    public static void main(String[] args) {
        Random random = new Random();
        int randomNumber = random.nextInt(100) + 1; // Generates a random number between 1 and 100
        System.out.println("The random number is: " + randomNumber);
    }
}
