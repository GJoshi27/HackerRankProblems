 /* =====================================================================================
 *
 *       Filename:  flipbits.c
 *
 *    Description:  
 *
 *        Version:  1.0
 *        Created:  Saturday 09 January 2016 12:10:30  IST
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
				while(T-- >0){
				unsigned int num;
				scanf("%u",&num);
				printf("%u \n",~num);
				}
				return EXIT_SUCCESS;
}
/* ----------  end of function main  ---------- */
