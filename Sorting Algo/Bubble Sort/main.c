//BUBBLE SORT
#include<stdio.h>
#define MAX 10

int main(){
    int n, arr[MAX];
    printf("How Many numbers do you want to push (MAX is %d): ", MAX);
    scanf("%d", &n);
    int i, num, flag=0;
    for(i=0; i<n; i++)
    {
        printf("Enter number to be inserted: ");
        scanf("%d", &num);
        arr[i]=num;
    }
    for(int k=0; k<n-1; k++)
    {
        for(int i=0; i<=n-2; i++)
        {
            int temp;             // DOES NOT WORK
            if(arr[i]>arr[i+1])
            {
                temp=arr[i+1];
                arr[i+1]=arr[i];
                arr[i]=temp;
            }
        }
    }
    printf("Sorted Array is: ");
    for(i=0; i<n; i++)
    {
        printf("%d ", arr[i]);
    }
}
