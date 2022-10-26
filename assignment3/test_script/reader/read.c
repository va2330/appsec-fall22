// C program to illustrate 
// open system call 
#include<stdio.h> 
#include<fcntl.h> 
#include<errno.h> 
extern int errno; 
int main() 
{     
    // open or create haha.txt is created. 
    int fd = open("./reader/haha.txt", O_RDONLY | O_CREAT);
    // open p123.txt twice created.  
    int fd1 = open("./reader/p123.txt", O_RDONLY);
    int fd2 = open("./reader/p123.txt", O_RDONLY);
    // open two other p-files.
    int fd3 = open("./reader/protobuf123.txt", O_RDONLY);
    int fd4 = open("./reader/protobuf345.txt", O_RDONLY);
      
    printf("fd = %d/n", fd); 
      
    if (fd ==-1) 
    { 
        // print which type of error have in a code 
        printf("Error Number % d\n", errno); 
          
        // print program detail "Success or failure" 
        perror("Program");                 
    } 
    return 0; 
} 
