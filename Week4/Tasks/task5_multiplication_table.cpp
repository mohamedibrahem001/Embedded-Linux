/**
 * @file task5_multiplication_table.cpp
 * @author Mohamed Ibrahem (mohamed.ibrahem628@gmail.com)
 * @brief 
 * This program generates and prints multiplication tables for a given range of numbers.
 * @version 0.1
 * @date 2024-08-19
 * 
 * @copyright Copyright (c) 2024
 * 
 */
#include <iostream>

void multiplication_table(int n) {
  for (int i = 1; i <= 12; i++) {
    std::cout<<n<<" x "<<i<<" = "<<n*i<<std::endl;
  }
}

void multiplication_tables(int from_n, int to_n) {
  for (int i = from_n; i <= to_n; i++) {
    //printf("Multiplication table for %d:\n", i);
     std::cout<<"Multiplication table for "<< i <<std::endl;
    multiplication_table(i);
      std::cout<<std::endl;
  }
}
int main(int argc, const char **argv) {

  multiplication_tables(1, 10);

  return 0;
}