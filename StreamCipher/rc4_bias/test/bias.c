#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <stdlib.h>
#include <sys/time.h>

#define KEY_LENGTH 16
#define ITERATIONS 16777216

void ksa(unsigned char state[], unsigned char key[]) {
    int i,j=0,t; 
    for (i=0; i<256; ++i)
        state[i] = i; 
    for (i=0; i<256; ++i) {
        j = (j + state[i] + key[i % KEY_LENGTH]) % 256; 
        t = state[i]; 
        state[i] = state[j]; 
        state[j] = t; 
    }
}

void prga(unsigned char state[], unsigned char out[]) {  
    int i=0,j=0,x,t; 
    unsigned char key; 
    for (x=0; x<256; ++x) {
        i = (i + 1) % 256; 
        j = (j + state[i]) % 256; 
        t = state[i];
        state[i] = state[j];
        state[j] = t;
        out[x] = state[(state[i] + state[j]) % 256];
    }
}

void makeRandomKey(unsigned char key[]) {
    int i;
    for (i=0; i<KEY_LENGTH; ++i) 
        key[i] = rand() % 256;
} 

int main(int argc, char *argv[]) {

    struct timeval time_started, time_now, time_diff;
    gettimeofday(&time_started, NULL);

    unsigned char state[256];
    unsigned char out[256];
    unsigned char key[KEY_LENGTH];
    int occurances[256][256];
    int i,j,bytePosition,charOccurance;

    for (i=0; i<256; ++i) 
        for (j=0; j<256; ++j)
            occurances[i][j] = 0;

    srand(time(NULL));
    for (i=0; i<ITERATIONS; ++i) {
        makeRandomKey(key);
        ksa(state, key);
        prga(state, out);

        for (j=0; j<256; ++j)
            ++occurances[j][out[j]];
    }

    for (bytePosition=0; bytePosition<256; ++bytePosition) {
        printf("%d,", bytePosition);
    }
    printf("\n");
    for (charOccurance=0; charOccurance<256; ++charOccurance) {
        for (bytePosition=0; bytePosition<256; ++bytePosition) {
            printf("%d,", occurances[charOccurance][bytePosition]);
        }
        printf("\n");
    }

    gettimeofday(&time_now, NULL);
    timersub(&time_now, &time_started, &time_diff);
    printf("Time taken,%ld.%.6ld s\n", time_diff.tv_sec, time_diff.tv_usec);

    return 0;
}