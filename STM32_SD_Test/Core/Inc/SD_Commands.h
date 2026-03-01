#ifndef __SD_COMMANDS_H
#define __SD_COMMANDS_H

#ifdef __cplusplus
	extern "C" {
#endif

#include "stdio.h"
#include "stdlib.h"
#include "main.h"
#include "fatfs.h"
//#include "ff.h"


float * readMeasurementData(FIL fil, char * filename, int * tempsLen);
int WriteMetaData(FIL fil, char * metaData, UINT bytesToWrite);
int writeMeasurements(FIL fil, char * filename, float * temps, int tempsLen, char * metaData, UINT bytesToWrite);

#ifdef __cplusplus
	}
#endif

#endif /* __SD_COMMANDS_H */
