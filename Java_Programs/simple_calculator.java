package Java_Programs;

import java.util.Scanner;

class Calculator{

    public static void main(String args[]){

        Scanner Uval =  new Scanner(System.in);
        
        double num1,num2;
        String operator;

        System.out.println("enter the first num");
        num1 = Uval.nextDouble();
        System.out.println("enter the second num");
        num2 = Uval.nextDouble();

        System.out.println("enter the operator");
        operator = Uval.next();
        
        double result = 0;
        switch (operator) {
            case "+":
                result = num1 + num2;
                break;
            case "-":
                result = num1 - num2;
                break;
            case "*":
                result = num1 * num2;
                break;
            case "/":
                if (num2 == 0) {
                    System.out.println("Error: cannot divide by 0");
                } else {
                    result = num1 / num2;
                }
                break;
            default:
                System.out.println("Error: invalid operator");
        }
        
        System.out.println("The result is: " + result);

    
        Uval.close();
    }
}