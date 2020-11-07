#include<stdio.h>
#define MAX 10

int main(){
    int n, arr[MAX];
    printf("How Many numbers do you want to push (MAX is %d): ", MAX);
    scanf("%d", &n);
    int i, num;
    for(i=0; i<n; i++)
    {
        printf("Enter number to be inserted: ");
        scanf("%d", &num);
        arr[i]=num;
    }
    printf("Enter Number you need to find: ");
    scanf("%d", &num);
        for(i=0; i<n; i++)
    {
        if (arr[i]==num)
        {
            printf("The number %d is at index %d OR position %d", num, i, i+1);
        }
        else
        {
            printf("Enter a number that you inserted in the array");
            break;
        }
    }
}
