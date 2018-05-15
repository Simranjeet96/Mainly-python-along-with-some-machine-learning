#include<bits/stdc++.h>
using namespace std;
void swap(int * num1,int * num2){
    int temp;
    temp = *num1;
    *num1=*num2;
    *num2=temp;
}
void func(int* arr,int size){
    int zeroOcurredposition =-1;
    for (signed int i = size-1; i >= 0; --i)
    {
        if(arr[i]!=0 && zeroOcurredposition==-1){
            continue;
        }else if(arr[i]==0 && zeroOcurredposition==-1)
        {
            zeroOcurredposition=i;
        }else if(arr[i]!=0){
            swap(&arr[i],&arr[zeroOcurredposition]);
            zeroOcurredposition--;
        }
    }

}
int main(int argc, char const *argv[])
{
    int arr[]={0,2,3,0,1,8,0,2,0};
    func(arr,sizeof(arr)/sizeof(int));
    for (unsigned int i = 0; i < sizeof(arr)/sizeof(int); ++i)
    {
        cout<<arr[i]<<endl;
    }
    unsigned char i=-65;
    cout<<int(i);
   return 0;
}

