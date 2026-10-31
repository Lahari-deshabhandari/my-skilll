#include<stdio.h>
int main(){
    int rev=0,rem,num;
    while(num!=0){
        rem=num%10;
        rev=rev*10+rem;
        num=num/10;

    }
    printf("Reverse of the number is: %d", rev);
    return 0;
}