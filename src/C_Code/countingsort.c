 /* =====================================================================================
 *
 *       Filename:  countingsort.c
 *
 *    Description:  
 *
 *        Version:  1.0
 *        Created:  Saturday 09 January 2016 10:30:54  IST
 *       Compiler:  gcc
 *
 *         Author:  Gaurav Joshi , contactgaurav27@gmail.com
 *   Organization:  University of Hyderabad
 *   help        :  use shortcuts \if \im \ \isf \ii \io \cfr \cfu 
                    \csc for adding comment history
										\rc is for compiling code
										\rr is for running code for vim only
 *
 * =====================================================================================*/

#include<stdlib.h>
#include<stdio.h>
#include<string.h>

/*===  FUNCTION  ======================================================================
 *  Name:  main
 *  Description:  
 *=====================================================================================*/

int main ( int argc, char *argv[] )
{
				int n;
				scanf("%d",&n);
				int i=0;
				int no;
				int arr[100];
				for(i=0;i<100;i++)
								arr[i]=0;

				for (i=0;i<n;i++)
				{
								scanf("%d",&no);
								arr[no]=arr[no]+1;
				}

				for(i=0;i<100;i++){
								printf("%d ",arr[i]);
				}

				printf("\n");
				return 0;
}
/* ----------  end of function main  ---------- */
