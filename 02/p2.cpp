#include <fstream>
#include <iostream>
#include <sstream>
#include <string>

using namespace std;

struct pos {
  int horizontal;
  int vertical;
  int aim;
};

int main(int argc, char **argv) {
  pos position{0};
  fstream file;
  file.open(argv[1], ios::in);
  if (!file.is_open()) {
    cout << "Failed to open file!" << argv[1] << endl;
    return -1;
  }

  for (string line; getline(file, line);) {
    int pos = line.find(" ");
    string command(line.substr(0, pos));
    string val_s(line.substr(pos, line.length()));
    int val(stoi(val_s));

    if (command == "forward") {
      position.horizontal += val;
      position.vertical += position.aim * val;
    } else if (command == "down") {
      position.aim += val;
    } else if (command == "up") {
      position.aim -= val;
    } else {
      cerr << "Unrecognized command!" << endl;
    }
  }
  cout << "Result: " << position.vertical * position.horizontal << endl;
  file.close();

  return 0;
}
