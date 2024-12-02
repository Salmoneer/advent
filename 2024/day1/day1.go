package day1

import (
    "os"
    "bufio"
    "fmt"
    "log"
    "strings"
    "strconv"
    "sort"
)

func main() {
    fmt.Printf("Part 1: %d\n", part1())
    fmt.Printf("Part 2: %d\n", part2())
}

func parse() ([]int, []int) {
    f, err := os.Open("data.txt")
    if err != nil {
        log.Fatal(err)
    }
    defer f.Close()

    scanner := bufio.NewScanner(f)

    var left_list []int
    var right_list []int

    for scanner.Scan() {
        line := scanner.Text()
        nums := strings.SplitN(line, "   ", 2)

        left_num, err := strconv.Atoi(nums[0])
        if err != nil {
            log.Fatal(err)
        }

        right_num, err := strconv.Atoi(nums[1])
        if err != nil {
            log.Fatal(err)
        }

        left_list = append(left_list, left_num)
        right_list = append(right_list, right_num)
    }

    return left_list, right_list
}

func part1() int {
    left_list, right_list := parse()

    sort.Slice(left_list, func(i, j int) bool { return left_list[i] < left_list[j] })
    sort.Slice(right_list, func(i, j int) bool { return right_list[i] < right_list[j] })

    s := 0

    for i := 0; i < len(left_list); i++ {
        diff := left_list[i] - right_list[i]
        if diff > 0 {
            s += diff
        } else {
            s -= diff
        }
    }

    return s
}

func part2() int {
    left_list, right_list := parse()

    right_freqs := make(map[int]int)

    for i := 0; i < len(left_list); i++ {
        right_freqs[right_list[i]] += 1
    }

    s := 0

    for i := 0; i < len(left_list); i++ {
        s += left_list[i] * right_freqs[left_list[i]]
    }

    return s
}
