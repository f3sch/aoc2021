#include <stdio.h>
#include <stdlib.h>

int main(int argc, char **argv) {
  int map[1000][1000] = {0};

  FILE *f = fopen("in1.txt", "r");

  char *buffer;
  size_t len = 30;
  buffer = malloc(sizeof(char) * 30);

  int x1;
  int y1;
  int x2;
  int y2;

  while (getline(&buffer, &len, f) != -1) {
    sscanf(buffer, "%d,%d -> %d,%d\n", &x1, &y1, &x2, &y2);
    if (x1 == x2) {
      int start = (y1 > y2) ? y2 : y1;
      int end = (y1 > y2) ? y1 : y2;

      for (; start < end + 1; start++) {
        map[x1][start]++;
      }

    } else if (y1 == y2) {
      int start = (x1 > x2) ? x2 : x1;
      int end = (x1 > x2) ? x1 : x2;

      for (; start < end + 1; start++) {
        map[start][y1]++;
      }
    } else {

      int xdir = x2 - x1;
      int ydir = y2 - y1;

      int xstep = (0 < xdir) - (xdir < 0);
      int ystep = (0 < ydir) - (ydir < 0);

      for (int x = x1, y = y1; x != x2 && y != y2; x += xstep, y += ystep) {
        map[x][y] += 1;
      }

      map[x2][y2] += 1;
    }
  }

  int points = 0;
  for (int x = 0; x != 1000; x++) {
    for (int y = 0; y != 1000; y++) {
      if (map[x][y] > 1)
        points += 1;
    }
  }
  printf("Points: %d", points);

  return 0;
}
