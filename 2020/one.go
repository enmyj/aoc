package main

import (
	"fmt"
	"io/ioutil"
	"strconv"
	"strings"
)

// Apparently this is how you read a file to integers?
// I miss python
// https://stackoverflow.com/questions/9862443/golang-is-there-a-better-way-read-a-file-of-integers-into-an-array
func readFile(fname string) (nums []int, err error) {
	b, err := ioutil.ReadFile(fname)
	if err != nil {
		return nil, err
	}

	lines := strings.Split(string(b), "\n")
	// Assign cap to avoid resize on every append.
	nums = make([]int, 0, len(lines))

	for _, l := range lines {
		// Empty line occurs at the end of the file when we use Split.
		if len(l) == 0 {
			continue
		}
		// Atoi better suits the job when we know exactly what we're dealing
		// with. Scanf is the more general option.
		n, err := strconv.Atoi(l)
		if err != nil {
			return nil, err
		}
		nums = append(nums, n)
	}

	return nums, nil
}

func questionone(input []int) {
	for _, row := range input {
		for _, r := range input {
			if row+r == 2020 {
				fmt.Println(r * row)
				return
			}
		}
	}
}

func questionTwo(input []int) {
	for _, i := range input {
		for _, j := range input {
			for _, k := range input {
				if i+j+k == 2020 {
					fmt.Println(i * j * k)
					return
				}
			}
		}
	}
}

func main() {
	inputData, _ := readFile("/Users/imyjer/repos/aoc/2020/data/one.input")
	questionone(inputData)
	questionTwo(inputData)
}
