 /* =====================================================================================
 *
 *       Filename:  sherlockarray.c
 *
 *    Description:  
 *
 *        Version:  1.0
 *        Created:  Saturday 09 January 2016 10:55:40  IST
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
				int T;
				scanf("%d",&T);

				while(T-- >0)
				{
								int N;
								scanf("%d",&N);
								int i=0;
								int arr[N];
								for(i=0;i<N;i++)
												scanf("%d",&arr[i]);
								if(N==1){
												printf("YES\n");
												continue;
								}

								int suml=0;
								int sumr=0;
								int ind=0;
								for(i=1;i<N;i++){
												sumr=sumr+arr[i];
								}

								for(i=0;i<N;i++)
								{
												if(i==0)
																suml=0;
												else
												suml=suml+arr[i-1];
												sumr=sumr-arr[i];
												if(suml==sumr){
																ind=1;
																break;
												}
												sumr=0;
								}
								if(ind==1)
												printf("YES\n");
								else
												printf("NO\n");
				}
				return EXIT_SUCCESS;
}
/* ----------  end of function main  ---------- */
