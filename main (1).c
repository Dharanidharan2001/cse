/******************************************************************************

                            Online C Compiler.
                Code, Compile, Run and Debug C program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include<stdio.h>
#include<stdlib.h>
int main()
{
     int i, num;
     float *data;

     printf("Enter total number of elements(1 to 100): ");
     scanf("%d",&num);

     //Allocates the memory for 'num' elements
     data=(float*)calloc(num,sizeof(float));

     if(data==NULL)
     {
         printf("Error! Memory not Allocated.");
         exit(0);
     }

     printf("\n");

     //Store the number entered by the User
     for(i=0;i<num;i++)
     {
         printf("Enter element %d:",i+1);
         scanf("%f",data+i);
     }

     //Store largest number at address data
     for(i=0;i<num;i++)
     {
         if( *data < *(data+i))
             *data = *(data+i);
     }

     printf("Largest Element = %.2f",*data);

     return 0;
    
}
