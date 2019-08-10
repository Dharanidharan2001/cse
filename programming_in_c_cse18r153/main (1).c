/******************************************************************************

                            Online C Compiler.
                Code, Compile, Run and Debug C program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <stdio.h>

int main()
{
    int num1,num2,num3;
    printf("enter three numbers");
    scanf("%d%d%d",&num1,&num2,&num3);
    if(num1>num2&&num1>num3)
    printf("%d is maximum",num1);
    else if(num2>num1&&num2>num3)
    printf("%d is maximum",num2);
    else if(num3>num1&&num3>num2)
    printf("%d is maximum",num3);
    return 0;
}