// Insertion Sort
#include<stdio.h>
#define MAX 10
int main(){

   int i, j, key, count, number[MAX];

   printf("How many numbers u are going to enter?: ");
   scanf("%d",&count);

   printf("Enter %d elements: ", count);
   // Loop to get the elements stored in array
   for(i=0;i<count;i++)
      scanf("%d",&number[i]);
    for(i=1;i<count;i++)
        {
            key = number[i];
            j = i - 1;
            while(j >= 0 && number[j] >= key)
            {
                number[j+1] = number[j];
                j = j -1;
            }
            number[j+1] = key;
        }
    printf("Sorted elements: ");
    for(i=0;i<count;i++)
    printf(" %d",number[i]);
}
