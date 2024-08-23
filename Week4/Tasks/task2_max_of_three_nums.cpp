
/**
 * @file task2_max_of_three_nums.cpp
 * @author Mohamed Ibrahem (mohamed.ibrahem628@gmail.com)
 * @brief
 *  this file to get the largest number of three entered numbers by user .
 * @version 0.1
 * @date 2024-08-17
 *
 * @copyright Copyright (c) 2024
 *
 */
#include <iostream>
#include <ostream>

int check_max_num(int num1, int num2, int num3) {
  int ret_value = 0;
  if (num1 == num2 && num2 == num3) {
    std::cout << "All numbers are equal and  equal" << std::endl;
    ret_value = num1;
  } else if (num1 == num2) {
    if (num1 > num3) {
      std::cout << "num1 and num2 are equal and  the largest" << std::endl;
      ret_value = num1;
    } else {
      std::cout << "num3 is the largest" << std::endl;
      ret_value = num3;
    }
  } else if (num1 == num3) {
    if (num1 > num2) {
      std::cout << "num1 and num3 are equal and  largest" << std::endl;
      ret_value = num1;
    } else {
      std::cout << "num2 is the largest" << std::endl;
      ret_value = num2;
    }
  } else if (num2 == num3) {
    if (num2 > num1) {
      std::cout << "num2 and num3 are equal and  largest" << std::endl;
      ret_value = num3;
    } else {
      std::cout << "num1 is the largest" << std::endl;
      ret_value = num1;
    }
  } else if (num1 > num2) {
    if (num1 > num3) {
      std::cout << "num1 is the largest" << std::endl;
      ret_value = num1;
    } else {
      std::cout << "num3 is the largest" << std::endl;
      ret_value = num3;
    }
  } else if (num2 > num3) {
    if (num2 > num1) {
      std::cout << "num2 is the largest" << std::endl;
      ret_value = num2;
    } else {
      std::cout << "num1 is the largest" << std::endl;
      ret_value = num1;
    }
  } else if (num3 > num1) {
    if (num2 > num1) {
      std::cout << "num3 is the largest" << std::endl;
      ret_value = num3;
    } else {
      std::cout << "num1 is the largest" << std::endl;
      ret_value = num1;
    }
  }
  return ret_value;
}
int main(int argc, const char **argv) {

  int num1 = 0;
  int num2 = 0;
  int num3 = 0;

  std::cout << "Enter Num1 " << std::endl;
  std::cin >> num1;
  std::cout << "Enter Num2 " << std::endl;
  std::cin >> num2;
  std::cout << "Enter Num3 " << std::endl;
  std::cin >> num3;
  check_max_num(num1, num2, num3);
  return 0;
}