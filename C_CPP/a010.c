#include <stdio.h>

int main() {
    int num;
    scanf("%d", &num);

    int ans[100]; // 假設最多有 100 個質因數
    int count[100] = {0}; // 記錄每個質因數的次數
    int index = 0;

    for (int i = 2; i <= num; i++) {
        while (num % i == 0) {
            num /= i;
            ans[index] = i;
            count[index]++;
            index++;
        }
    }

    for (int i = 0; i < index; i++) {
        if (count[i] > 1) {
            printf("%d^%d", ans[i], count[i]);
        } else {
            printf("%d", ans[i]);
        }
        if (i < index - 1) {
            printf(" * ");
        }
    }
    printf("\n");

    return 0;
}
