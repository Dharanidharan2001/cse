/******************************************************************************

                            Online C Compiler.
                Code, Compile, Run and Debug C program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <stdio.h>

int main()
{
    int num1,num2;
    printf("enter two numbers");
    scanf("%d%d",&num1,&num2);
    if(num1>num2)
    printf("%d is maximum",num1);
    else if(num1<num2)
    printf("5d is maximum",num2);
    else if(num1==num2)
    printf("both are equal");
    return 0;
}
