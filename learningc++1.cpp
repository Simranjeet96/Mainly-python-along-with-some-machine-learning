// #include <bits/stdc++.h>
// using namespace std;
// int square(int x) { return x*x;}
// int square(double x)=delete;
// // int square(int x){return x;}
// int main()
// {
    
//  // enum Day {Sunday, Monday, Tuesday};
//  //    enum Month {January, February, March};
//  //    Day d = Monday;
//  //    Month m = February;

//  //    if (d == m)
//  //    std::cout << "Monday == February\n";  // This will be printed out
//  //    else
//  //    std::cout << "Monday != February\n";
//     try{
//     int A=1/0;}
//     catch(...){cout<<"hi";}

//     return 0;
// }



#include <stdio.h>
int x = 20;
int f1() { x = x+10; return x;}
int f2() { x = x-5;  return x;}
int main()
{
  int p = f1() + f2();
  printf ("p = %d", p);
  return 0;
}
