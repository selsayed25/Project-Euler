# include <iostream>
using namespace std;

int main() {
    int answer = 0;

    for (int index = 1; index < 1000; index++) {
        if (index % 3 == 0 || index % 5 == 0) {
            answer += index;
        }
    }

    cout << answer << endl;

    int wait = 0;
    cin >> wait;

    return 0;
}