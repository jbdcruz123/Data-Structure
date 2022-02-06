//RSM 02-06-2022 BubbleSort.c

#include<stdio.h>

void fBbleSort(int *A, int N){//1 1A 

  int AI=0, BI, T;
  
  while(AI < N -1){//2
    
    BI = 0;
    while(BI < N - AI){//3 
    
      if(A[BI] > A[BI+1]){//4 
        
        T = A[BI];
        A[BI] = A[BI+1];
        A[BI+1] = T;
        
      }//4 
      
      BI++;
    }//3 
    
    
    AI++;
  }//2 

}//1 1A 

void fPrntArry(int *A, int N){//1 1C 

  int AI=0;
  while(AI < N){//2 
  
    if(5== AI){//3 
    
      printf("  ");  
    }//3
    
     
    printf("%d ", A[AI]);
   
    AI++;
   
  }//2 

  printf("\n\n");
}//1 1C 

int main(){//1 1B 


  int A[6]={ 4, 2 ,5, 1, 3,   0};

  printf("\n\nInput:\n");
  
  fPrntArry(A, 6);
  
  fBbleSort(A, 6);

  printf("\n\nInput:\n");
  
  fPrntArry(A, 6);
  
  
}//1 1B 

