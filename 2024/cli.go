package main

import (
    "flag"
    "fmt"
    "log"
    "os"
    "strconv"
    "strings"
    "time"

    "2024/day1"
    "2024/day2"
    "2024/day3"
    "2024/day4"
    "2024/day5"
    // "2024/day6"
    // "2024/day7"
    // "2024/day8"
    // "2024/day9"
    // "2024/day10"
    // "2024/day11"
    // "2024/day12"
    // "2024/day13"
    // "2024/day14"
    // "2024/day15"
    // "2024/day16"
    // "2024/day17"
    // "2024/day18"
    // "2024/day19"
    // "2024/day20"
    // "2024/day21"
    // "2024/day22"
    // "2024/day23"
    // "2024/day24"
    // "2024/day25"
)

func time_func(f func() int) (int, time.Duration) {
    start := time.Now()

    result := f()

    return result, time.Since(start)
}

func str_to_day(str string) int {
    day_number, err := strconv.Atoi(str)
    if err != nil {
        fmt.Println("Day flag expects a number")
        os.Exit(1)
    }

    if day_number < 1 || day_number > 25 {
        fmt.Println("Day number must be between 1 and 25")
        os.Exit(1)
    }

    return day_number
}


// Print a table using ─ │ ╭ ╮ ╰ ╯ ├ ┤ ┬ ┴ characters
func draw_table(cells []string, width int, height int) {
    if len(cells) > width * height || width <= 0 || height <= 0 {
        log.Fatal("Table size too small for data")
    }

    for len(cells) < width * height {
        cells = append(cells, "")
    }

    var table_data []string

    for i := 0; i < len(cells); i++ {
        table_data = append(table_data, strings.TrimSpace(cells[i]))
    }

    var column_widths []int

    for i := 0; i < width; i++ {
        max_width := 0
        for j := 0; j < height; j++ {
            max_width = max(max_width, len(table_data[width * j + i]))
        }

        column_widths = append(column_widths, max_width)
    }

    table_width := 3 * len(column_widths) - 1

    for i := 0; i < len(column_widths); i++ {
        table_width += column_widths[i]
    }

    top_line := strings.Repeat("─", table_width)
    bottom_line := strings.Repeat("─", table_width)

    index := -1
    for i := 1; i < width; i++ {
        index += column_widths[i - 1] + 3

        temp := []rune(top_line)
        temp[index] = '┬'
        top_line = string(temp)

        temp = []rune(bottom_line)
        temp[index] = '┴'
        bottom_line = string(temp)
    }

    fmt.Print("╭")
    fmt.Print(top_line)
    fmt.Print("╮\n")

    for i := 0; i < height; i++ {
        for j := 0; j < width; j++ {
            fmt.Printf("│ %*s ", column_widths[j], table_data[width * i + j])
        }
        fmt.Print("│\n")
    }

    fmt.Print("╰")
    fmt.Print(bottom_line)
    fmt.Print("╯\n")
}

func main() {
    funcs := []func() int{
        day1.Part1,
        day1.Part2,
        day2.Part1,
        day2.Part2,
        day3.Part1,
        day3.Part2,
        day4.Part1,
        day4.Part2,
        day5.Part1,
        day5.Part2,
        // day6.Part1,
        // day6.Part2,
        // day7.Part1,
        // day7.Part2,
        // day8.Part1,
        // day8.Part2,
        // day9.Part1,
        // day9.Part2,
        // day10.Part1,
        // day10.Part2,
        // day11.Part1,
        // day11.Part2,
        // day12.Part1,
        // day12.Part2,
        // day13.Part1,
        // day13.Part2,
        // day14.Part1,
        // day14.Part2,
        // day15.Part1,
        // day15.Part2,
        // day16.Part1,
        // day16.Part2,
        // day17.Part1,
        // day17.Part2,
        // day18.Part1,
        // day18.Part2,
        // day19.Part1,
        // day19.Part2,
        // day20.Part1,
        // day20.Part2,
        // day21.Part1,
        // day21.Part2,
        // day22.Part1,
        // day22.Part2,
        // day23.Part1,
        // day23.Part2,
        // day24.Part1,
        // day24.Part2,
        // day25.Part1,
        // day25.Part2,
    }

    

    runCmd := flag.NewFlagSet("run", flag.ExitOnError)
    runDay := runCmd.String("day", "", "Day to run (1-25)")

    timeCmd := flag.NewFlagSet("time", flag.ExitOnError)
    timeDay := timeCmd.String("day", "", "Day to time (1-25)")

    command := os.Args[1]

    switch command {
    case "run":
        runCmd.Parse(os.Args[2:])

        day_number := str_to_day(*runDay)

        fmt.Printf("Day %d:\n", day_number)
        fmt.Printf("Part 1: %d\n", funcs[(day_number - 1) * 2 + 0]())
        fmt.Printf("Part 2: %d\n", funcs[(day_number - 1) * 2 + 1]())
    case "time":
        timeCmd.Parse(os.Args[2:])

        if *timeDay == "" {
            fmt.Println("Table for all days not implemented yet")
            os.Exit(1)
        } else {
            day_number := str_to_day(*timeDay)

            _, time1 := time_func(funcs[(day_number - 1) * 2 + 0])
            _, time2 := time_func(funcs[(day_number - 1) * 2 + 1])

            timeTotal := time1 + time2

            time1_s := time1.String()
            time2_s := time2.String()
            timeTotal_s := timeTotal.String()

            draw_table([]string{"Part 1", time1_s, "Part 2", time2_s, "Total", timeTotal_s}, 2, 3)
        }

    default:
        fmt.Printf("Unknown command %s\n", command)
        os.Exit(1)
    }
}
