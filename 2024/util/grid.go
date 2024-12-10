package util

import (
    "log"
    "strings"
)

type Grid struct {
    Data   []uint8
    Width  int
    Height int
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
