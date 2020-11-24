
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
    int start = 0;
    int end = n;
    while(start <= end)
    {
        int mid = (start + end) / 2;
        if (arr[mid] == num)
        {
            printf("Found at loc %d \n",mid+1);
            return 0;
        }
        else if(num > arr[mid])
        {
            start = mid+1;
        }
        else
        {
            end = mid - 1;
        }
    }
    printf("Item not found\n");
    return 1;
}

