/**
 * @file calc.h
 * @author Mohamed Ibrahem (mohamed.ibrahem628@gmail.com)
 * @brief 
 * this file implement calculator basic functions 
 * @version 0.1
 * @date 2024-06-26
 * 
 * @copyright Copyright (c) 2024
 * 
 */
#ifndef __CALC_H__
#define __CALC_H__

#include <stdint.h>

/**
 * @brief add
 *  this function to add two numbers 
 * @param num1
 * first number in uint32_t
 * @param num2
 * second number in uint32_t 
 * @return uint64_t 
 * it returns the sum of num1 and num2 
 */
uint64_t add(uint32_t num1 , uint32_t num2);

/**
 * @brief sub
 * this function to subtract two numbers 
 * @param num1 
 *  first number in int32_t
 * @param num2 
 * second number in int32_t
 * @return int64_t 
 *it returns the subtraction of num1 and num2
 */
int64_t sub(int32_t num1 , int32_t num2);

/**
 * @brief mul
 *  this function to multiply two numbers 
 * @param num1 
 *  first number in uint32_t
 * @param num2 
 *  second number in uint32_t
 * @return uint64_t 
 * it returns the multiplication of num1 and num2 
 */
uint64_t mul(uint32_t num1, uint32_t num2);
#endif
