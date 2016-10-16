#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <omp.h>
#define _USE_MATH_DEFINES
#include <cmath>
#include <string.h>
#include <ctime>
#include <sys/time.h>
#include <sys/resource.h>
#define SSE_WIDTH	4

#ifndef ARRSIZE
#define ARRSIZE 32000000
#endif
#ifndef MINSIZE
#define MINSIZE 1000
#endif
#ifndef DATAPOINTS
#define DATAPOINTS 1000
#endif
#ifndef NUM_TRIES
#define NUM_TRIES 10
#endif


void 
Mul(float *a, float *b, float *c, int len) {
	for (int i = 0; i < len; i++) {
		c[i] = a[i] * b[i];
	}
}

float
MulSum(float *a, float*b, int len) {
	float sum = 0.;
	for (int i = 0; i < len; i++) {
		sum += a[i] * b[i];
	}
	return sum;
}

void
SimdMul(float *a, float *b, float *c, int len)
{
	int limit = (len / SSE_WIDTH) * SSE_WIDTH;
	__asm
	(
		".att_syntax\n\t"
		"movq    -24(%rbp), %rbx\n\t"		// a
		"movq    -32(%rbp), %rcx\n\t"		// b
		"movq    -40(%rbp), %rdx\n\t"		// c
		);

	for (int i = 0; i < limit; i += SSE_WIDTH)
	{
		__asm
		(
			".att_syntax\n\t"
			"movups	(%rbx), %xmm0\n\t"	// load the first sse register
			"movups	(%rcx), %xmm1\n\t"	// load the second sse register
			"mulps	%xmm1, %xmm0\n\t"	// do the multiply
			"movups	%xmm0, (%rdx)\n\t"	// store the result
			"addq $16, %rbx\n\t"
			"addq $16, %rcx\n\t"
			"addq $16, %rdx\n\t"
			);
	}

	for (int i = limit; i < len; i++)
	{
		c[i] = a[i] * b[i];
	}
}



float
SimdMulSum(float *a, float *b, int len)
{
	float sum[4] = { 0., 0., 0., 0. };
	int limit = (len / SSE_WIDTH) * SSE_WIDTH;

	__asm
	(
		".att_syntax\n\t"
		"movq    -40(%rbp), %rbx\n\t"		// a
		"movq    -48(%rbp), %rcx\n\t"		// b
		"leaq    -32(%rbp), %rdx\n\t"		// &sum[0]
		"movups	 (%rdx), %xmm2\n\t"		// 4 copies of 0. in xmm2
		);

	for (int i = 0; i < limit; i += SSE_WIDTH)
	{
		__asm
		(
			".att_syntax\n\t"
			"movups	(%rbx), %xmm0\n\t"	// load the first sse register
			"movups	(%rcx), %xmm1\n\t"	// load the second sse register
			"mulps	%xmm1, %xmm0\n\t"	// do the multiply
			"addps	%xmm0, %xmm2\n\t"	// do the add
			"addq $16, %rbx\n\t"
			"addq $16, %rcx\n\t"
			);
	}

	__asm
	(
		".att_syntax\n\t"
		"movups	 %xmm2, (%rdx)\n\t"	// copy the sums back to sum[ ]
		);

	for (int i = limit; i < len; i++)
	{
		sum[i - limit] += a[i] * b[i];
	}

	return sum[0] + sum[1] + sum[2] + sum[3];
}



int
main(int argc, char *argv[])
{
#ifndef _OPENMP
	fprintf(stderr, "OpenMP is not available\n");
	return 1;
#endif
	float *A = new float[ARRSIZE];
	float *B = new float[ARRSIZE];
	float *C = new float[ARRSIZE];
	double time0;
	double time1;
	//1000 runs
	for (int size = MINSIZE; size <= ARRSIZE; size += ((ARRSIZE- MINSIZE)/ DATAPOINTS)) {
		double sumSIMDMul = 0.;
		double sumSIMDMulSum = 0.;
		double sumMul = 0.;
		double sumMulSum = 0;
		for (int i = 0; i < NUM_TRIES; i++) {
			//SIMD Mul
			time0 = omp_get_wtime();
			SimdMul(C, A, B, size);
			time1 = omp_get_wtime();
			sumSIMDMul += time1 - time0;
			//SIMD Redux
			time0 = omp_get_wtime();
			SimdMulSum(A, B, size);
			time1 = omp_get_wtime();
			sumSIMDMulSum += time1 - time0;
			//Mul
			time0 = omp_get_wtime();
			Mul(C, A, B, size);
			time1 = omp_get_wtime();
			sumMul += time1 - time0;
			//Redux
			time0 = omp_get_wtime();
			MulSum(A, B, size);
			time1 = omp_get_wtime();
			sumMulSum += time1 - time0;
		}
		printf("%d,%f,%f,%f,%f\n", size, size / sumSIMDMul / NUM_TRIES / 1000000, size / sumSIMDMulSum / NUM_TRIES / 1000000, size / sumMul / NUM_TRIES / 1000000, size / sumMulSum / NUM_TRIES / 1000000);
	}
	return 0;
}