package day2

import (
    _ "embed"
    "log"
    "strings"
    "strconv"
)

//go:embed data.txt
var data string

func abs(x int) int {
    if x < 0 {
        return -x
    } else {
        return x
    }
}

func parse() [][]int {
    var reports [][]int

    for _, line := range strings.Split(strings.TrimSpace(data), "\n") {
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

func Part1() int {
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

func Part2() int {
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
