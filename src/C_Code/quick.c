#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
#include <assert.h>
void swap ( int* a, int* b );
void partition(int ar_size, int *  ar);


void partition(int ar_size, int *  ar) {
   int pivot = ar[0];       // set the pivot as the first element in the partition
   int i=0;
    int k=ar_size-1;
                while (k > i)                   // while the scan indices from left and right have not met,
                {
                        while (ar[i] <= pivot && i <= ar_size-1 && k > i)  // from the left, look for the first
                                i++;                                    // element greater than the pivot
                        while (ar[k] > pivot && k >= 0 && k >= i) // from the right, look for the first
                            k--;                                        // element not greater than the pivot
                        if (k > i)                                       // if the left seekindex is still smaller than
                                swap(&ar[i],&ar[k]);                      // the right index, swap the corresponding elements
                }
                swap(&ar[0],&ar[k]);          // after the indices have crossed, swap the last element in
  
   return;
}

void swap ( int* a, int* b )
{
    int t = *a;
    *a = *b;
    *b = t;
}

int main(void) {
   
   int _ar_size;
scanf("%d", &_ar_size);
int _ar[_ar_size], _ar_i;
for(_ar_i = 0; _ar_i < _ar_size; _ar_i++) { 
   scanf("%d", &_ar[_ar_i]); 
}

partition(_ar_size, _ar);
   for(_ar_i = 0; _ar_i < _ar_size; _ar_i++) { 
   printf("%d ", _ar[_ar_i]); 
}

   
   return 0;
}

