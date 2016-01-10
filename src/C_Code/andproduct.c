 /* =====================================================================================
 *
 *       Filename:  andproduct.c
 *
 *    Description:  
 *
 *        Version:  1.0
 *        Created:  Saturday 09 January 2016 12:27:49  IST
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
#include<math.h>

/*===  FUNCTION  ======================================================================
 *  Name:  main
 *  Description:  
 *=====================================================================================*/

int main ( int argc, char *argv[] )
{
//printf("%f\n",log2(9));
				int T;
				scanf("%d",&T);
				while(T-->0)
				{
								int num1,num2;
								scanf("%d %d",&num1,&num2);
								if(num2&num2-1==0){
												printf("0\n");
												continue;
								}
								int logv=(int)log2(num2);
								int val=1  << logv;
								//printf("val :%d \n",val);
								if(num1<val && val <=num2)
												printf("0\n");
								else
												printf("%d\n",num1);


				}
				return EXIT_SUCCESS;
}
/* ----------  end of function main  ---------- */
