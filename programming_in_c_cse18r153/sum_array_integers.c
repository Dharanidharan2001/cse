/******************************************************************************

                            Online C Compiler.
                Code, Compile, Run and Debug C program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <stdio.h>

int
main ()
{
  int array[10] = { 10, 2, 30, 4, 5, 6, 70, 8, 9, 10 };

  int sum = 0;
  int i;

  for (i = 0; i < 10; i++)
    {
      printf ("%d\n", i);
    }
  
  printf ("Sum of the array is %d\n", sum);

  for (i = 0; i < 10; i++)
    {
      printf("array[%d] = %d\n", i, array[i]);
      sum = sum + array[i];
      printf ("intermediate sum = %d\n", sum);
    }

/* sum now contains a[0] + a[1] + ... + a[9] */
  printf ("Sum of the array is %d\n", sum);
  return 0;
}
