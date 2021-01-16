#include<stdio.h>
#include<conio.h>
int main()
{
    int i,j,k;
    printf("Your pattern is below\n");
    printf("=====================\n");

    for(i=1;i<=5;i++)
    {
        for(j=0;j<5-i;j++)
        {
            printf(" ");
        }
        for(k=1;k<=2*i-1;k++)
        {
            printf("*");
        }
        printf("\n");
    }

    for(i=5;i<=5 && i>=0;i--)
    {
        for(j=0;j<=5-i;j++)
        {
            printf(" ");
        }
        for(k=0;k<2*(i-1)-1;k++)
        {
            printf("*");
        }
        printf("\n");
    }
    return 0;
}

