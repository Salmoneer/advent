package day4

import (
    "2024/util"
    _ "embed"
)

//go:embed data.txt
var data string

func Part1() int {
    grid := util.ParseGrid(data)

    s := 0

    for start_x := 0; start_x < grid.Width; start_x++ {
        for start_y := 0; start_y < grid.Height; start_y++ {
            for dx := -1; dx <= 1; dx++ {
            delta:
                for dy := -1; dy <= 1; dy++ {
                    for i := 0; i < 4; i++ {
                        x := start_x + i*dx
                        y := start_y + i*dy

                        if x < 0 || x >= grid.Width || y < 0 || y >= grid.Height || grid.Data[grid.Width*y+x] != "XMAS"[i] {
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
    grid := util.ParseGrid(data)

    s := 0

    for start_x := 0; start_x < grid.Width-2; start_x++ {
        for start_y := 0; start_y < grid.Height-2; start_y++ {
            xs := []int{start_x, start_x + 1, start_x + 2}
            ys := []int{start_y, start_y + 1, start_y + 2}

            // grid indices in the following pattern:
            // 0.4
            // .1.
            // 3.2

            indices := []int{ys[0]*grid.Width + xs[0], ys[1]*grid.Width + xs[1], ys[2]*grid.Width + xs[2], ys[2]*grid.Width + xs[0], ys[0]*grid.Width + xs[2]}

            // same indexing as above, but for characters instead of indices

            chars := []uint8{}

            for _, index := range indices {
                chars = append(chars, grid.Data[index])
            }

            if (chars[0] == 'M' || chars[0] == 'S') && chars[1] == 'A' && (chars[2] == 'S' || chars[2] == 'M') && chars[0] != chars[2] && (chars[3] == 'M' || chars[3] == 'S') && (chars[4] == 'S' || chars[4] == 'M') && chars[3] != chars[4] {
                s++
            }
        }
    }

    return s
}
