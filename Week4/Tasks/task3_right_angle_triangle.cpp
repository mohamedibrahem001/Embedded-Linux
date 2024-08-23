/**
 * @file task3_right_angle_triangle.cpp
 * @author Mohamed Ibrahem (mohamed.ibrahem628@gmail.com)
 * @brief
 * This program calculates the largest number among three given integers, but it
 * only considers right angle triangles where the sum of the squares of the two
 * shorter sides equals the square of the longest side.
 *
 * @version 0.1
 * @date 2024-08-20
 *
 * @copyright Copyright (c) 2024
 *
 */
#include <cstdint>
#include <iostream>

int check_max_num(int num1, int num2, int num3) {
  int ret_value = 0;
  if (num1 == num2 && num2 == num3) {
    // std::cout << "All numbers are equal and  equal" << std::endl;
    ret_value = num1;
  } else if (num1 == num2) {
    if (num1 > num3) {
      //   std::cout << "num1 and num2 are equal and  the largest" << std::endl;
      ret_value = num1;
    } else {
      // std::cout << "num3 is the largest" << std::endl;
      ret_value = num3;
    }
  } else if (num1 == num3) {
    if (num1 > num2) {
      // std::cout << "num1 and num3 are equal and  largest" << std::endl;
      ret_value = num1;
    } else {
      //  std::cout << "num2 is the largest" << std::endl;
      ret_value = num2;
    }
  } else if (num2 == num3) {
    if (num2 > num1) {
      //  std::cout << "num2 and num3 are equal and  largest" << std::endl;
      ret_value = num3;
    } else {
      // std::cout << "num1 is the largest" << std::endl;
      ret_value = num1;
    }
  } else if (num1 > num2) {
    if (num1 > num3) {
      //  std::cout << "num1 is the largest" << std::endl;
      ret_value = num1;
    } else {
      // std::cout << "num3 is the largest" << std::endl;
      ret_value = num3;
    }
  } else if (num2 > num3) {
    if (num2 > num1) {
      //  std::cout << "num2 is the largest" << std::endl;
      ret_value = num2;
    } else {
      // std::cout << "num1 is the largest" << std::endl;
      ret_value = num1;
    }
  } else if (num3 > num1) {
    if (num2 > num1) {
      //  std::cout << "num3 is the largest" << std::endl;
      ret_value = num3;
    } else {
      //  std::cout << "num1 is the largest" << std::endl;
      ret_value = num1;
    }
  }
  return ret_value;
}
bool isRightTriangle(int a, int b, int c) {
  bool ret_val = false;
  if ((a == 0) || (b == 0) || (c == 0)) {
    ret_val = false;
  } else {

    uint64_t a_square = a * a;
    uint64_t b_square = b * b;
    uint64_t c_square = c * c;
    uint64_t max_num = check_max_num(a, b, c);
    if (max_num == a) {
      if (a_square == (b_square + c_square)) {
        ret_val = true;
      } else {
        ret_val = false;
      }
    } else if (max_num == b) {

      if (b_square == (a_square + c_square)) {
        ret_val = true;
      } else {
        ret_val = false;
      }
    } else {
      if (c_square == (a_square + b_square)) {
        ret_val = true;
      } else {
        ret_val = false;
      }
    }
  }
  return ret_val;
}

// Usage example
int main(int argc, const char **argv) {
  int a = 0;
  int b = 0;
  int c = 0;

  std::cout << "Enter the three sides : " << std::endl;
  std::cout << "first_side : " << std::endl;
  std::cin >> a;
  std::cout << "second_side : " << std::endl;
  std::cin >> b;
  std::cout << "third_side : " << std::endl;
  std::cin >> c;

  if (isRightTriangle(a, b, c))
    std::cout << "The triangle is a right triangle." << std::endl;
  else
    std::cout << "The triangle is not a right triangle." << std::endl;
  return 0;
}