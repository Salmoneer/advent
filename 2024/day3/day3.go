package day3

import (
	_ "embed"
	"log"
	"strconv"
)

//go:embed data.txt
var data string

type TokenKind int

const (
    mul TokenKind = iota
    do
    dont
    null
)

type Token struct{
    kind TokenKind
    a int
    b int
}

func token_gen() func() Token {
    last_i := 0

    return func() Token {
        a := 0
        num_str := []uint8{}

        mul_state := 0
        do_state := 0
        dont_state := 0

        const mul_start = "mul("
        const do_str = "do()"
        const dont_str = "don't()"

        for i := last_i; i < len(data); i++ {
            c := data[i]

            if mul_state < len(mul_start) && mul_start[mul_state] == c {
                mul_state++
            } else if mul_state == 4 {
                if '0' <= c && c <= '9' {
                    num_str = append(num_str, c)
                } else if c == ',' && len(num_str) != 0 {
                    val, err := strconv.Atoi(string(num_str))
                    if err != nil {
                        log.Fatal(err)
                    }

                    mul_state++
                    a = val

                    num_str = []uint8{}
                } else {
                    a = 0
                    num_str = []uint8{}

                    mul_state = 0
                }
            } else if mul_state == 5 {
                if '0' <= c && c <= '9' {
                    num_str = append(num_str, c)
                } else if c == ')' && len(num_str) != 0 {
                    val, err := strconv.Atoi(string(num_str))
                    if err != nil {
                        log.Fatal(err)
                    }

                    last_i = i + 1

                    return Token{mul, a, val}
                } else {
                    a = 0
                    num_str = []uint8{}

                    mul_state = 0
                }
            } else {
                mul_state = 0
            }

            if do_state < len(do_str) && do_str[do_state] == c {
                do_state += 1

                if do_state == len(do_str) {
                    last_i = i + 1
                    return Token{do, 0, 0}
                }
            } else {
                do_state = 0
            }

            if dont_state < len(dont_str) && dont_str[dont_state] == c {
                dont_state += 1

                if dont_state == len(dont_str) {
                    last_i = i + 1
                    return Token{dont, 0, 0}
                }
            } else {
                dont_state = 0
            }
        }

        return Token{null, 0, 0}
    }
}

func Part1() int {
    s := 0

    gen := token_gen()

    for {
        token := gen()

        if token.kind == null {
            break
        }

        if token.kind == mul {
            s += token.a * token.b
        }
    }

    return s
}

func Part2() int {
    s := 0

    gen := token_gen()

    enable := true

    outer: for {
        token := gen()

        switch token.kind {
        case null:
            break outer
        case mul:
            if enable {
                s += token.a * token.b
            }
        case do:
            enable = true
        case dont:
            enable = false
        }
    }

    return s
}
