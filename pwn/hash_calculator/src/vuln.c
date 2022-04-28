#include <openssl/sha.h>
#include <stdio.h>
#include <string.h>

void print_hash(char *s) {
  unsigned char digest[SHA256_DIGEST_LENGTH];
  SHA256_CTX sha_ctx;
  SHA256_Init(&sha_ctx);
  SHA256_Update(&sha_ctx, s, strlen(s));
  SHA256_Final(digest, &sha_ctx);
  for (int i = 0; i < SHA256_DIGEST_LENGTH; i++) {
    printf("%02x", digest[i]);
  }
  puts("");
}

int main() {
  setvbuf(stdin, NULL, _IONBF, 0);
  setvbuf(stdout, NULL, _IONBF, 0);
  char input[0x100];
  char content[0x100];
  while (1) {
    printf("filename?> ");
    scanf("%255s", input);
    if (strcmp(input, "exit") == 0) {
      return 0;
    }
    printf(input);
    puts("");
    FILE *fp = fopen(input, "r");
    if (fp == NULL) {
      printf("File cannot be opened.");
      puts("");
      continue;
    }
    memset(content, 0, 0x100);
    fread(&content, 0xff, 1, fp);
    fclose(fp);
    print_hash(content);
  }
}
