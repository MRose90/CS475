#include <omp.h>
#include <stdio.h>
#include <math.h>
#include <float.h>
#define ARRAYSIZE       1000000
#define NUMTRIES        1000

int
main( )
{
#ifndef _OPENMP
        fprintf( stderr, "OpenMP is not supported here -- sorry.\n" );
        return 1;
#endif

        float *A = new float[ARRAYSIZE];
        float *B = new float[ARRAYSIZE];
        float *C = new float[ARRAYSIZE];

        omp_set_num_threads( NUMT );
        fprintf( stderr, "Using %d threads\n", NUMT );

        double maxmmults = 0.;
        double summmults = 0.;
	double minmmults = DBL_MAX;
        for( int t = 0; t < NUMTRIES; t++ )
        {
                double time0 = omp_get_wtime( );

                #pragma omp parallel for
                for( int i = 0; i < ARRAYSIZE; i++ )
                {
                        C[i] = A[i] * B[i];
                }

                double time1 = omp_get_wtime( );
                double mmults = (double)ARRAYSIZE/(time1-time0)/1000000.;
                summmults += mmults;
                if( mmults > maxmmults )
                        maxmmults = mmults;
		if(mmults < minmmults)
			minmmults = mmults;
        }
        printf( "   Peak Performance = %8.2lf MegaMults/Sec\n", maxmmults );
	printf( "   Minimum Performance = %8.2lf MegaMults/Sec\n", minmmults );
        printf( "   Average Performance = %8.2lf MegaMults/Sec\n", summmults/(double)NUMTRIES );

        return 0;
}

