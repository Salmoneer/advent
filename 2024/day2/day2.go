package main

import (
    "os"
    "bufio"
    "fmt"
    "log"
    "strings"
    "strconv"
)

func main() {
    fmt.Printf("Part 1: %d\n", part1())
    fmt.Printf("Part 2: %d\n", part2())
}

func abs(x int) int {
    if x < 0 {
        return -x
    } else {
        return x
    }
}

func parse() [][]int {
    f, err := os.Open("data.txt")
    if err != nil {
        log.Fatal(err)
    }
    defer f.Close()

    scanner := bufio.NewScanner(f)

    var reports [][]int

    for scanner.Scan() {
        line := scanner.Text()

        string_numbers := strings.Split(line, " ")
        var numbers []int

        for i := 0; i < len(string_numbers); i++ {
            num, err := strconv.Atoi(string_numbers[i])
            if err != nil {
                log.Fatal(err)
            }

            numbers = append(numbers, num)
        }

        reports = append(reports, numbers)
    }

    return reports
}

func none_wrong(report []int) bool {
    var diffs []int

    for i := 1; i < len(report); i++ {
        diffs = append(diffs, report[i] - report[i - 1])
    }

    negative := diffs[0] < 0

    valid := true

    for i := 0; i < len(diffs); i++ {
        diff := diffs[i]

        if !(diff < 0 == negative && abs(diff) >= 1 && abs(diff) <= 3) {
            valid = false
            break
        }
    }

    return valid
}

func part1() int {
    reports := parse()

    s := 0

    for r := 0; r < len(reports); r++ {
        report := reports[r]

        if none_wrong(report) {
            s++
        }
    }

    return s
}

func part2() int {
    reports := parse()

    s := 0

    for r := 0; r < len(reports); r++ {
        report := reports[r]

        if none_wrong(report) {
            s++
            continue
        }

        for i := 0; i < len(report); i++ {
            report_copy := make([]int, len(report))
            copy(report_copy, report)
            new_report := append(report_copy[:i], report_copy[i+1:]...)

            if none_wrong(new_report) {
                s++
                break
            }
        }
    }

    return s
}
