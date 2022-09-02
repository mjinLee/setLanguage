#include <stdio.h>

int main(void)
{
    int num1, num2;
    do
    {
        printf("정수 2개를 입력: ");
        fflush(stdin);
    } while (scanf("%d %d", &num1, &num2) != 2);

    int sum = 0;
    sum = num1 + num2;
    printf("num1 = %d, num2 = %d, sum=%d", num1, num2, sum);

    return 0;
}