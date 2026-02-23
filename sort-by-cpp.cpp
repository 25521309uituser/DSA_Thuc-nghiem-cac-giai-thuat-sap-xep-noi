#include <bits/stdc++.h>
using namespace std::chrono;
using namespace std;

vector <float> arr1[6];
vector <int> arr2[6];
vector <int> cnt;

int main()
{
    freopen("data.txt", "r", stdin);
    
    for (int i = 0; i < 5; i++)
    {
        for (int j = 0; j < 1000000; j++)
        {
            int x;
            cin >> x;
            arr1[i].push_back(x);
        }
    }

    for (int i = 0; i < 5; i++)
    {
        for (int j = 0; j < 1000000; j++)
        {
            float x;
            cin >> x;
            arr2[i].push_back(x);
        }
    }

    for (int i = 0; i < 5; i++)
    {
        auto start = high_resolution_clock::now();
        sort(arr1[i].begin(), arr1[i].end());
        auto end = high_resolution_clock::now();
        auto duration = duration_cast<milliseconds>(end - start);
        cnt.push_back(duration.count());
    }

    for (int i = 0; i < 5; i++)
    {
        auto start = high_resolution_clock::now();
        sort(arr2[i].begin(), arr2[i].end());
        auto end = high_resolution_clock::now();
        auto duration = duration_cast<milliseconds>(end - start);
        cnt.push_back(duration.count());
    }

    for (auto x : cnt)
        cout << x << " ";
    return 0;
}