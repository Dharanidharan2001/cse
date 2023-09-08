package Java_Programs;

import java.util.Scanner;

class Calculator{

    public static void main(String args[]){

        Scanner Uval =  new Scanner(System.in);
        
        double fnum,snum,output;

        System.out.println("enter the first num");
        fnum = Uval.nextDouble();
        System.out.println("enter the second num");
        snum = Uval.nextDouble();

        output = fnum+snum;
        System.out.println(output);
        

    }
}