# include <iostream>
using namespace std;

int main() {
    int answer = 0;
    int x = 1;
    int y = 1;
    int z = 0;

    while (true) {
        z = x + y;
        x = y;
        y = z;

        if (z > 4000000) {
            break;
        }

        if (z % 2 == 0) {
            answer += z;
        }
    }

    cout << answer << endl;

    int wait = 0;
    cin >> wait;

    return 0;
}