 /* =====================================================================================
 *
 *       Filename:  finddigits.c
 *
 *    Description:  
 *
 *        Version:  1.0
 *        Created:  Saturday 09 January 2016 12:59:04  IST
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

				while(T-->0)
				{
								int num=0;
								scanf("%d",&num);

								int tmp=num;
								int digit=0;
								int cnt=0;
								while(tmp!=0)
								{
												digit=tmp%10;
												tmp=tmp/10;
												if(digit==0)
																continue;
												if(num%digit==0)
																cnt++;
								}
								printf("%d\n",cnt);

				}
				return EXIT_SUCCESS;
}
/* ----------  end of function main  ---------- */
