/*
Notes:
- dynamic array very easy!
- error handling mandatory (probably for the best)
- reading line by line weirdly hard
*/

package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
)

func main() {
	nums := parseNumFile()

	part1(nums)
	part2(nums)
}

func parseNumFile() []int {
	file, err := os.Open("../inputs/day1.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	nums := make([]int, 0)

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		n, err := strconv.Atoi(scanner.Text())
		if err != nil {
			log.Fatal(err)
		}
		nums = append(nums, n)
	}

	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}
	return nums
}

func part1(nums []int) {
	for _, n1 := range nums {
		for _, n2 := range nums {
			if n1+n2 == 2020 {
				fmt.Printf("Result: %d\n", n1*n2)
				return
			}
		}
	}
}

func part2(nums []int) {
	for _, n1 := range nums {
		for _, n2 := range nums {
			for _, n3 := range nums {
				if n1+n2+n3 == 2020 {
					fmt.Printf("Result: %d\n", n1*n2*n3)
					return
				}
			}
		}
	}
}
