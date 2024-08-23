/**
 * @file task7_binary_decimal_converter.cpp
 * @author Mohamed Ibrahem (mohamed.ibrahem628@gmail.com)
 * @brief
 * Converts a binary number to decimal and vice versa.
 * @version 0.1
 * @date 2024-08-20
 *
 * @copyright Copyright (c) 2024
 *
 */
#include "iostream"
#include <bitset>
#include <c++/11/bitset>
#include <c++/11/cstdint>
#include <c++/11/iostream>
#include <c++/11/ostream>
#include <c++/11/string>
#include <c++/11/valarray>
#include <cstdint>
#include <iostream>
#include <ostream>
#include <string>
#include <x86_64-linux-gnu/bits/stdint-uintn.h>

typedef enum {
  DECIMAL_TO_BINARY = 1,
  BINARY_TO_DECIMAL,
} CONVERT_t;

std::string converter(CONVERT_t type, uint64_t number) {
  std::string result = "";

  if (type == DECIMAL_TO_BINARY) {
    std::cout << "decimal to binary" << std::endl;

    while (number > 0) {
      int rem = number % 2;
      result = std::to_string(rem) + result;
      number /= 2;
    }
  } else if (type == BINARY_TO_DECIMAL) {
    uint64_t decimal = 0;
    uint64_t i = 0;
    while (number > 0) {

      uint8_t rem = 0;
      rem = number % 10;
      decimal += rem * pow(2, i);
      number /= 10;
      i++;
    }
    result = std::to_string(decimal);
  }
  return result;
}
int main(int argc, const char **argv) {
  // std::cout << converter(DECIMAL_TO_BINARY, 15) << std::endl;

  int select = 0;
  std::cout << "select type : " << std::endl
            << "1. Decimal to binary" << std::endl
            << "2. Binary to decimal" << std::endl;
  std::cin >> select;

  switch (select) {
  case DECIMAL_TO_BINARY: {
    {
      std::cout << "Enter the number " << std::endl;
      uint64_t number = 0;
      std::cin >> number;

      if (number > 0xFFFFFFFF) {
        std::bitset<64> stringBitset(converter(DECIMAL_TO_BINARY, number));
        std::cout << stringBitset << std::endl;
      } else if (number > 0xFFFF) {
        std::bitset<32> stringBitset(converter(DECIMAL_TO_BINARY, number));
        std::cout << stringBitset << std::endl;
      } else if (number > 0xFF) {
        std::bitset<16> stringBitset(converter(DECIMAL_TO_BINARY, number));
        std::cout << stringBitset << std::endl;
      } else {
        std::bitset<8> stringBitset(converter(DECIMAL_TO_BINARY, number));
        std::cout << stringBitset << std::endl;
      }
    }
    break;
  case BINARY_TO_DECIMAL: {
    {
      std::cout << "Enter the binary number " << std::endl;
      int binary;
      std::cin >> binary;

      std::string number = "";

      number = converter(BINARY_TO_DECIMAL, binary);
      std::cout << "Decimal equivalent : " << number << std::endl;
    }
    break;
  } break;
  }
  }
  return 0;
}