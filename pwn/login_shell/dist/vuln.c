#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

void login() { system("/bin/sh"); }

int main() {
  char input[0x20];
  char password[0x20];
  memset(input, 0, 0x20);
  memset(password, 0, 0x20);

  setvbuf(stdin, NULL, _IONBF, 0);
  setvbuf(stdout, NULL, _IONBF, 0);

  FILE *fp = fopen("password.txt", "r");
  if (fp == NULL) {
    puts("File cannot be opened. Please contact admin.");
    return -1;
  }
  fread(&password, 0x20, 1, fp);
  printf("password?> ");
  read(0, input, 0x20);
  printf("password: %s\n", input);
  if (strcmp(input, password) == 0) {
    puts("login succeed!");
    login();
  } else {
    puts("login fail...");
  }
  return 0;
}
