# plane_seat.js

# Latoya Boland
# CSCI 77800 Fall 2022
# collaborators: 
# consulted: https://coderanch.com/t/642227/java/Loop-airplane-seating-reservations-seats


import java.util.*;
public class plane_seating {
    public static void main(String[] args) {
    System.out.println("Welcome to the seat reservation system!");

//Create Seating Chart (like creating a board for a game)
        char[][] seats = new char [8][6];
        ArrayList<String> reservedSeats = new ArrayList<>();
        for (int i=0;i<8;i++){
            seats[i][0] = 'A';
            seats[i][1] = 'B';
            seats[i][2] = 'C';
            seats[i][3] = 'D';
            seats[i][4] = 'E';
            seats[i][5] = 'F';
    }


// Selecting seating
    Scanner console = new Scanner(System.in);
    int filled = 0;
    printSeats(seats);
    System.out.println("Enter seat (e.g. 1A) or zero to quit the program.");
			
    String input = console.nextLine();
    while ((filled <48) &&(input.length() >0)) {
            int row = input.charAt(0) - '1';
            int col = input.charAt(1) - 'A';
            if (row<0 || row>8 || col<0 || col>6) {
                System.out.println("Input error. Enter seat to assign (e.g., '1A'), " + 
                    "or zero to quit."); //How to make 0 the exit key?
                input = console.nextLine(); 
            } else {
                if (seats[row][col] != 'X') {
                    seats[row][col] = 'X';
                    filled++;
                    System.out.println();
                printSeats(seats);
            }
 //Loop until filled
            if (filled < 48) { 
                System.out.println("Enter seat to assign (e.g., '1A'), " + 
                    "or zero to quit:"); 
                input = console.nextLine(); 
            } 
        }
    }
        System.out.println("Final seat assignments: "); 
        printSeats(seats); 
    }
    private static void printSeats(char[][] seats) {
        for (int i = 0; i < seats.length; i++) { 
            System.out.println((i + 1) + "   " + 
                seats[i][0] + seats[i][1] + seats[i][2] + " " +
                seats[i][3] + seats[i][4] + seats[i][5]);
            }
            System.out.println("There are XX number of seats available."); //Program counts available seats everytime the seating chart is updated.
        }
    } 