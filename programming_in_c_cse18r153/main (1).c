/******************************************************************************

                            Online C Compiler.
                Code, Compile, Run and Debug C program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <stdio.h>

int main()
{
int a[3][3],b[3][3],c[3][3],r,c,i,j,r1,c1;
printf("enter the no of rows and columns in first matrix");
scanf("%d%d",&r,&c);
printf("enter the no of ros and columns in second matrix");
sacnf("%d%d",&r1,&c1);
for(i=0;i<r;i++)
for(j=0;j<c;j++)
scanf("%d",&a[i][j]);
}
for(i=0;i<r1;i++)
for(j=0;j<c1;j++)
{
    scanf("%d",&b[i][j]);
}
if(r==r1&&c==c1)
for(i=0;i<r;i++)
for(j=0;j<c;j++)
{
    c[i][j]=a[i][j]+b[i][j]
}
for(i=0;i<r;i++
for(j=0;j<c;j++)
{
    printf("%d",c[i][j]);
}
}
}
}
