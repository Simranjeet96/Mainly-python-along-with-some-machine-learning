// #include <iostream>
// #include <cmath> // for sqrt() function
 
// // A modular square root function
// double mySqrt(double x)
// {
//     // If the user entered a negative number, this is an error condition
//     if (x < 0.0)
//         throw "Can not take sqrt of negative number"; // throw exception of type const char*
 
//     return sqrt(x);
// }
 
// int main()
// {
//     std::cout << "Enter a number: ";
//     double x;
//     std::cin >> x;
 
//     // Look ma, no exception handler!
//     std::cout << "The sqrt of " << x << " is " << mySqrt(x) << '\n';
 
//     return 0;
// }




#include<bits/stdc++.h>
using namespace std;
template <typename T> 
T **AllocateDynamicArray( int nRows, int nCols)
{
      T **dynamicArray;

      dynamicArray = new T*[nRows];
      for( int i = 0 ; i < nRows ; i++ )
      dynamicArray[i] = new T [nCols];

      return dynamicArray;
}

template <typename T>
void FreeDynamicArray(T** dArray)
{
      delete [] *dArray;
      delete [] dArray;
}
template <typename T, typename U>
auto sum( T t, U u ){
    return t+u;
}

template <typename T>
void foo(T arg){
    arg=100;
    cout<<arg;
}
int main()
{
      // int **my2dArr = AllocateDynamicArray<int>(4,4);
      // my2dArr[0][0]=5;
      // my2dArr[2][2]=8;
  
      // FreeDynamicArray<int>(my2dArr);

        // cout<<sum(5,9.1);
//     char const * arr = "simran" "jeet"   "singh";
    // char const * arr=R"(string with \backslash)";
    // cout<<arr;
// int x = int(); // x is an int, initialized to 0
// assert(x == 0);
    int b=10;
    const int& a=b;

    foo(a);


      return 0;
}



PROGRAM 1
#include <stdio.h>
int f1() { printf ("Geeks"); return 3;}
int f2() { printf ("forGeeks"); return 19;}
int main() 
{ 
  int p = (f1(),f2());  
  printf("%d\n",p);
  return 0; 
}


// // #include <stdio.h>
// // int main()
// // {
// //     int b=10;
// //     int a=20;
// //     printf("%d\n",a );
// //         printf("%d\n",b );
// //         b = (a + b)-(a = b);
// //     printf("%d\n",a );
// //         printf("%d\n",b );
// // }

// #include <iostream>
// #include <string>
// #include <sstream>
// using namespace std;

// int main ()
// {
//   // string mystr;
//   // float price=0;
//   // int quantity=0;

//   // cout << "Enter price: ";
//   // getline (cin,mystr);
//   // //stringstream(mystr) >> price;
//   // //stringstream(mystr) >> quantity;
//   // cout<<int(mystr);
//   // cout << "Enter quantity: ";
//   // getline (cin,mystr);
//   // stringstream(mystr) >> quantity;
//   // cout << "Total price: " << price*quantity << endl;
//   // string s="sim";
//   // char * aName = s;
  
//   // cout<<*aName;
//   // // return 0;

// enum class Day { Sunday, Monday, Tuesday };
//     enum  class Month { January, February, March };

//     Day d = Day::Monday;
//     Month m = Month::February;
    
//     // No "==" operator is defined for the object type nor overloaded
//     // So, in C++ 11, this is an compile time error
//     //cout<<d<<m;
//     if(d==m){
//         cout<<"hhh";
//     }
    
// }
