#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int linear_search(int arr[], int key, int size) {
    for (int i = 0; i < size; i++) {
        if (arr[i] == key) {
            return i;
        }
    }
    return -1;
}

void generateRandomArr(int arr[], int n) {
    for (int i = 0; i < n; i++) {
        arr[i] = rand() % 100000;
    }
}

int main() {
    printf("Enter number of elements: ");
    int n;
    scanf("%d", &n);

    int *arr = (int *)malloc(n * sizeof(int));
    if (arr == NULL) {
        printf("Memory allocation failed!\n");
        return 1;
    }

    generateRandomArr(arr, n);
    int key = arr[rand() % n];

    int repetitions = 1000000;

    clock_t start = clock();
    for (int i = 0; i < repetitions; i++) {
        linear_search(arr, key, n);
    }
    clock_t end = clock();

    double total_time = (double)(end - start) / CLOCKS_PER_SEC;
    double time_per_search = total_time / repetitions;

    printf("Time taken for %d elements is %e seconds\n", n, time_per_search);

    free(arr);
    return 0;
}
