def read_input():
    with open("/home/ghiles/Documents/projects/advent_of_code/day_1/input") as f:
        content = f.read().rstrip()

    pairs = [list(map(int, c.split())) for c in content.split('\n')]

    return [list(row) for row in zip(*pairs)]

def solve1():
    list1, list2 = read_input()
    list1, list2 = sorted(list1), sorted(list2)

    s = sum(abs(l1 - l2) for l1, l2 in zip(list1, list2))

    print(s)

def solve2():
    list1, list2 = read_input()

    occ = dict()
    
    for e in list2 :
        occ[e] = occ.get(e, 0) + 1

    s = sum(e * occ.get(e, 0) for e in list1)

    print(s)

def main():
    solve1()
    solve2()

if __name__ == "__main__":
    main()
