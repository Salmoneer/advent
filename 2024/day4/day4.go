package day4

import (
    _ "embed"
    "log"
    "strings"
)

//go:embed data.txt
var data string

type Grid struct{
    data []uint8
    width int
    height int
}

func ParseGrid(grid_data string) Grid {
    lines := strings.Split(strings.TrimSpace(grid_data), "\n")

    final_data := ""

    line_length := len(lines[0])

    for i := 0; i < len(lines); i++ {
        line := lines[i]

        if len(line) != line_length {
            log.Fatal("Line in grid data is of a different length")
        }

        final_data += line
    }

    return Grid{[]uint8(final_data), line_length, len(lines)}
}

func Part1() int {
    grid := ParseGrid(data)

    s := 0

    for start_x := 0; start_x < grid.width; start_x++ {
        for start_y := 0; start_y < grid.height; start_y++ {
            for dx := -1; dx <= 1; dx++ {
                delta: for dy := -1; dy <= 1; dy++ {
                    for i := 0; i < 4; i++ {
                        x := start_x + i * dx
                        y := start_y + i * dy

                        if x < 0 || x >= grid.width || y < 0 || y >= grid.height || grid.data[grid.width * y + x] != "XMAS"[i] {
                            continue delta
                        }
                    }

                    s++
                }
            }
        }
    }

    return s
}

func Part2() int {
    grid := ParseGrid(data)

    s := 0

    for start_x := 0; start_x < grid.width - 2; start_x++ {
        for start_y := 0; start_y < grid.height - 2; start_y++ {
            backslash := []uint8{}
            forwardslash := []uint8{}

            for i := 0; i < 3; i++ {
                backslash = append(backslash, grid.data[(start_y + i) * grid.width + (start_x + i)])
                forwardslash = append(forwardslash, grid.data[(start_y + 2 - i) * grid.width + (start_x + i)])
            }

            if (string(backslash) == "MAS" || string(backslash) == "SAM") && (string(forwardslash) == "MAS" || string(forwardslash) == "SAM") {
                s++
            }
        }
    }

    return s
}
