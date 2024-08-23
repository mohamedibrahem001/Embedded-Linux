/**
 * @file task4_is_vowel_letter.cpp
 * @author Mohamed Ibrahem (mohamed.ibrahem628@gmail.com)
 * @brief 
 * A program to check if a given character is a vowel or not.
 * A vowel is a letter that is a member of the set of letters that represent a basic vowel sound.
 *  It includes the letters 'a', 'e', 'i', 'o', and 'u', as well as their respective uppercase counterparts.
 * The program prompts the user to enter a character and then checks if it is a vowel or not.
 * If the character is a vowel, the program displays a message stating that it is a vowel.
 * If the character is not a vowel, the program displays a message stating that it is not a vowel. 
 *
 * @version 0.1
 * @date 2024-08-19
 * 
 * @copyright Copyright (c) 2024
 * 
 */

#include <iostream>
#include <string>

void is_a_vowel(char ch) {
  std::string vowels = "aeiouAEIOU";
  std::string::size_type pos = vowels.find(ch);

  if (pos != std::string::npos) {
    std::cout << ch << " is a vowel." << std::endl;
  } else {
    std::cout << ch << " is not a vowel." << std::endl;
  }
}

int main(int argc, const char **argv) {

  char character = 0;

  std::cout << "enter a charater : " << std::endl;
  std::cin >> character;

  is_a_vowel(character);

  return 0;
}