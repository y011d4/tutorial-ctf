#include <stdio.h>
#include <string.h>

int main() {
  char input[0x40];
  printf("flag?> ");
  scanf("%63s", input);
  if (strcmp(input, "FLAG{you_can_see_this_only_by_strings_command}") == 0) {
    puts("Correct!");
  } else {
    puts("Wrong...");
  }
}
