package day5

import (
	_ "embed"
	"log"
	"strconv"
	"strings"
)

//go:embed data.txt
var data string

func parse() (map[int]map[int]bool, [][]int) {
    updating := false

    rules := map[int]map[int]bool{}
    updates := [][]int{}

    for _, line := range strings.Split(data, "\n") {
        if line == "" {
            updating = true
            continue
        }

        if !updating {
            left, err := strconv.Atoi(line[:2])
            if err != nil {
                log.Fatal(err)
            }

            right, err := strconv.Atoi(line[3:])
            if err != nil {
                log.Fatal(err)
            }

            if rules[right] == nil {
                rules[right] = map[int]bool{}
            }
            rules[right][left] = true
        } else {
            num_strs := strings.Split(line, ",")
            update := []int{}

            for _, str := range num_strs {
                num, err := strconv.Atoi(str)
                if err != nil {
                    log.Fatal(err)
                }
                update = append(update, num)
            }

            updates = append(updates, update)
        }
    }

    return rules, updates
}

// Can first be followed by second according to rules?
func allowed(first int, second int, rules map[int]map[int]bool) bool {
    return !rules[first][second]
}

// Is an entire update allowed according to rules?
func validUpdate(update []int, rules map[int]map[int]bool) bool {
    for i, second := range update {
        for _, first := range update[:i] {
            if !allowed(first, second, rules) {
                return false
            }
        }
    }

    return true
}

func Part1() int {
    rules, updates := parse()

    total := 0

    for _, update := range updates {
        if validUpdate(update, rules) {
            total += update[(len(update) - 1) / 2]
        }
    }

    return total
}

// Reorder update such that it is valid according to rules
func reorderUpdate(update []int, rules map[int]map[int]bool) []int {
    reordered := make([]int, len(update))
    copy(reordered, update)

    // loop done manually to allow going back to a certain point
    // without having to loop over the entire start of the update again
    outer:
    for i := 0; i < len(reordered); i++ {
        second := reordered[i]

        for j, first := range reordered[:i] {
            if !allowed(first, second, rules) {
                reordered[i] = first
                reordered[j] = second

                // go back to the number we just swapped and continue from there
                // -1 accounts for the i++ in the outer loop when we continue
                i = j - 1

                continue outer
            }
        }
    }

    return reordered
}

func Part2() int {
    rules, updates := parse()

    total := 0

    for _, update := range updates {
        if validUpdate(update, rules) {
            continue
        }

        reordered := reorderUpdate(update, rules)

        total += reordered[(len(reordered) - 1) / 2]
    }

    return total
}
