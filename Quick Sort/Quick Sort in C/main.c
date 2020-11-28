// Quick Sort in C
#include <stdio.h>
int partition(int arr[10], int low, int high)
{
    int i, pivot, temp, j;
    i = low-1;
    pivot = arr[high];
    for(j=low; j<high; j++)
    {
        if(arr[j]<pivot)
        {
            i++;
            temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
        }
    }
    temp = arr[i+1];
    arr[i+1] = arr[high];
    arr[high] = temp;
    return (i+1);

}

int sort(int arr[10], int low, int high)
{
    int pi;
    if (low < high)
    {
        pi = partition(arr, low, high);
        sort(arr, low, pi-1);
        sort(arr, pi+1, high);
    }
}
int main() {
    int arr[10]={9,8,7,6,5,4,3,2,1,0};
    sort(arr, 0, 9);
    for(int i=0; i<10; i++)
    {
        printf("%d ", arr[i]);
    }
    return 0;
}
