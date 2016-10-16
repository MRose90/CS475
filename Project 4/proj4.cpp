#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <omp.h>
#define _USE_MATH_DEFINES
#include <cmath>

#ifndef ENDYEAR 
#define ENDYEAR 2021
#endif
int	NowYear = 2016;		// 2016 - ENDYEAR
int	NowMonth = 0;		// 0 - 11

float	NowPrecip;		// inches of rain per month
float	NowTemp;		// temperature this month
float	NowHeight = 40.;		// grain height in inches
int	NowNumDeer = 40;		// number of deer in the current population
int NowVelociraptors = 1;

const float GRAIN_GROWS_PER_MONTH = 10.0;
const float ONE_DEER_EATS_PER_MONTH = 0.5;
const float ONE_VELOCIRAPTOR_EATS_PER_MONTH = .25;

const float AVG_PRECIP_PER_MONTH = 6.0;
const float AMP_PRECIP_PER_MONTH = 6.0;
const float RANDOM_PRECIP = 2.0;

const float AVG_TEMP = 50.0;
const float AMP_TEMP = 20.0;
const float RANDOM_TEMP = 10.0;


float
Ranf(float low, float high)
{
	float r = (float)rand();               // 0 - RAND_MAX

	return(low + r * (high - low) / (float)RAND_MAX);
}


int
Ranf(int ilow, int ihigh)
{
	float low = (float)ilow;
	float high = (float)ihigh + 0.9999f;

	return (int)(Ranf(low, high));
}

void
TandP() {
	float ang = (30.*(float)NowMonth + 15.) * (M_PI / 180.);

	float temp = AVG_TEMP - AMP_TEMP * cos(ang);
	NowTemp = temp + Ranf(-RANDOM_TEMP, RANDOM_TEMP);

	float precip = AVG_PRECIP_PER_MONTH + AMP_PRECIP_PER_MONTH * sin(ang);
	NowPrecip = precip + Ranf(-RANDOM_PRECIP, RANDOM_PRECIP);
	if (NowPrecip < 0.)
		NowPrecip = 0.;
}

void
GrainDeer() {
	
	while (NowYear <= ENDYEAR) {
		int tempNumDeer = NowNumDeer;
		tempNumDeer -= (int)((float)NowVelociraptors * ONE_VELOCIRAPTOR_EATS_PER_MONTH);
		if (NowNumDeer*ONE_DEER_EATS_PER_MONTH > NowHeight) {
			int popDec = (int)((float)NowNumDeer*.05);
			if (popDec < 1)
				popDec = 1;
			tempNumDeer -= popDec;
		}
		if (NowNumDeer*ONE_DEER_EATS_PER_MONTH < NowHeight) {
			int popInc = (int)((float)NowNumDeer*.1);
			if (popInc < 1)
				popInc = 1;
			tempNumDeer += popInc;
		}
		if (tempNumDeer < 0)
			tempNumDeer = 0;
#pragma omp barrier
		NowNumDeer = tempNumDeer;
#pragma omp barrier
#pragma omp barrier
	}
}

void
Grain() {
	
	while (NowYear <= ENDYEAR) {
		float tempFactor =exp(-1*pow((NowTemp-AVG_TEMP)/10.,2));
		float precipFactor = exp(-1 * pow((NowPrecip - AVG_PRECIP_PER_MONTH) / 10., 2));;
		float tempHeight = NowHeight;
		tempHeight += tempFactor * precipFactor * GRAIN_GROWS_PER_MONTH;
		tempHeight -= (float)NowNumDeer * ONE_DEER_EATS_PER_MONTH;
		if (tempHeight < 0.)
			tempHeight = 0.;
#pragma omp barrier
		NowHeight = tempHeight;
#pragma omp barrier
#pragma omp barrier
	}

}
void
Watcher() {
	while (NowYear <= ENDYEAR) {
#pragma omp barrier
#pragma omp barrier
		printf("%d,%d,%f,%f,%f\n",NowNumDeer,NowVelociraptors,NowHeight,NowTemp,NowPrecip);
		if (NowMonth == 11) {
			NowMonth = -1;
			NowYear++;
		}
		NowMonth++;
		TandP();
#pragma omp barrier
	}
}
void
MyAgent() {
	while (NowYear <= ENDYEAR) {
		int tempVelociraptor = NowVelociraptors;
		if (NowVelociraptors*ONE_VELOCIRAPTOR_EATS_PER_MONTH > NowNumDeer)
			tempVelociraptor--;
		if (NowNumDeer*ONE_VELOCIRAPTOR_EATS_PER_MONTH < NowNumDeer && NowMonth > 5 && NowMonth < 8)
			tempVelociraptor++;
		if (tempVelociraptor < 0)
			tempVelociraptor = 0;
#pragma omp barrier
		NowVelociraptors = tempVelociraptor;
#pragma omp barrier
#pragma omp barrier
	}
}

int
main(int argc, char *argv[])
{
#ifndef _OPENMP
	fprintf(stderr, "OpenMP is not available\n");
	return 1;
#endif
	TandP();
	omp_set_num_threads(4);
#pragma omp parallel sections
	{
#pragma omp section
		{
			GrainDeer();
		}

#pragma omp section
		{
			Grain();
		}

#pragma omp section
		{
			Watcher();
		}

#pragma omp section
		{
			MyAgent();
		}
	}       // implied barrier -- all functions must return in order to allow any of them to get past here
	return 0;
}