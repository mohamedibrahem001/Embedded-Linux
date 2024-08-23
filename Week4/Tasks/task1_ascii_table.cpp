/**
 * @file task1_ascii_table.cpp
 * @author Mohamed Ibrahem (mohamed.ibrahem628@gmail.com)
 * @brief
 * This program prints the ASCII table in a formatted manner.
 * @version 0.1
 * @date 2024-08-17
 *
 * @copyright Copyright (c) 2024
 *
 */
#include <iomanip>
#include <ios>
#include <iostream>
#include <ostream>
int main(int argc, const char **argv) {

  std::cout << std::setw(10) << " ----------------------------" << std::endl;
  std::cout << "|" << std::setw(5) << " HEX" << std::setw(5) << "|"
            << std::setw(5) << " DEC" << std::setw(5) << "|" << std::setw(5)
            << " Char" << std::setw(5) << "|" << std::endl;

  for (auto i = 33; i < 127; i++) {
    std::cout << "|" << std::setw(5) << std::hex << i << std::setw(5) << "|"
              << std::dec << std::setw(5) << i << std::setw(5) << "|"
              << std::setw(5) << static_cast<char>(i) << std::setw(5) << "|"
              << std::endl;
  }

  std::cout << std::setw(10) << " ----------------------------" << std::endl;
  return 0;
}