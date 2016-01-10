 /* =====================================================================================
 *
 *       Filename:  maximisexor.c
 *
 *    Description:  
 *
 *        Version:  1.0
 *        Created:  Saturday 09 January 2016 12:16:10  IST
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
				int L,R;
				scanf("%d",&L);
				scanf("%d",&R);
				int i=0;
				int j=0;
				int Max=-1;
				int res=-1;
				for(i=L;i<=R;i++)
				{
								for(j=L;j<=R;j++)
								{
												res=i^j;
												if(res>Max)
																Max=res;
								}
				}

				printf("%d\n",Max);
				return EXIT_SUCCESS;
}
/* ----------  end of function main  ---------- */
