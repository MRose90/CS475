#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <omp.h>


#ifndef NUMPAD
#define NUMPAD		 0
#endif
#ifndef NUMT
#define NUMT	  	4
#endif
#ifndef ADDITIONS
#define ADDITIONS	100000000
#endif

struct s
{
	float value;
} Array[4];



int
main( int argc, char *argv[ ] )
{
#ifndef _OPENMP
	fprintf( stderr, "OpenMP is not available\n" );
	return 1;
#endif

	omp_set_num_threads( NUMT );
	int numProcessors = omp_get_num_procs( );

	double time0 = omp_get_wtime( );

	#pragma omp parallel for
	for( int i = 0; i < 4; i++ )
	{
		float tmp = Array[ i ].value;
		for( unsigned int j = 0; j < ADDITIONS; j++ )
		{
			tmp = tmp + 2.;
		}
		Array[ i ].value = tmp;
	}

	double time1 = omp_get_wtime( );
	double time = time1-time0;
	printf("%d,%f\n", NUMT, (double)ADDITIONS/time/(double)1000000);
	
	return 0;
}
