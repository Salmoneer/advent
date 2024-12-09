package day4

import (
    _ "embed"
    "log"
    "strings"
)

//go:embed data.txt
var data string

type Grid struct {
    data   []uint8
    width  int
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
            delta:
                for dy := -1; dy <= 1; dy++ {
                    for i := 0; i < 4; i++ {
                        x := start_x + i*dx
                        y := start_y + i*dy

                        if x < 0 || x >= grid.width || y < 0 || y >= grid.height || grid.data[grid.width*y+x] != "XMAS"[i] {
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

    for start_x := 0; start_x < grid.width-2; start_x++ {
        for start_y := 0; start_y < grid.height-2; start_y++ {
            xs := []int{start_x, start_x + 1, start_x + 2}
            ys := []int{start_y, start_y + 1, start_y + 2}

            // grid indices in the following pattern:
            // 0.4
            // .1.
            // 3.2

            indices := []int{ys[0]*grid.width + xs[0], ys[1]*grid.width + xs[1], ys[2]*grid.width + xs[2], ys[2]*grid.width + xs[0], ys[0]*grid.width + xs[2]}

            // same indexing as above, but for characters instead of indices

            chars := []uint8{}

            for _, index := range indices {
                chars = append(chars, grid.data[index])
            }

            if (chars[0] == 'M' || chars[0] == 'S') && chars[1] == 'A' && (chars[2] == 'S' || chars[2] == 'M') && chars[0] != chars[2] && (chars[3] == 'M' || chars[3] == 'S') && (chars[4] == 'S' || chars[4] == 'M') && chars[3] != chars[4] {
                s++
            }
        }
    }

    return s
}
