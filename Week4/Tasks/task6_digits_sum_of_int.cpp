/**
 * @file task6_digits_sum_of_int.cpp
 * @author Mohamed Ibrahem (mohamed.ibrahem628@gmail.com)
 * @brief 
 * This program calculates the sum of the digits of a given integer.
 * 
 * @version 0.1
 * @date 2024-08-19
 * 
 * @copyright Copyright (c) 2024
 * 
 */
#include <iostream>

int digits_sum(int num) {
  int sum = 0;
  while (num != 0) {
    sum += num % 10;
    num /= 10;
  }
  return sum;
}
int main(int argc, const char **argv) {

  int number = 354;
  std::cout << "enter a number : " << std::endl;
  std::cin >> number;
  std::cout << "sum of the number digits " << number << " is "
            << digits_sum(number) << std::endl;
  return 0;
}