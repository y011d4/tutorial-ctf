#include <stdio.h>
#include <string.h>

const char data[4] = {0x13, 0x37, 0xc0, 0xd3};
const char result[] = "U{\x81\x94hD\xa9\xbe"
                      "c[\xa5\x8c"
                      "aR\xb6\x8cp_\xa1\xbf\x7fh\xa9\xa0}C\x9f\xbag\x08\xbd";

int main() {
  char input[0x40];
  printf("flag?> ");
  scanf("%63s", input);
  if (strlen(input) != strlen(result)) {
    puts("Wrong...");
    return 1;
  }
  int correct = 1;
  int n = strlen(input);
  for (int i = 0; i < n; i++) {
    if ((input[i] ^ data[i % 4]) != result[i]) {
      correct = 0;
    }
  }
  if (correct) {
    puts("Correct!");
    return 0;
  } else {
    puts("Wrong...");
    return 1;
  }
}
