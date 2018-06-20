if __name__ == '__main__':
    physics_score = []
    for _ in range(int(input())):
        physics_score.append([input(), float(input())])
    sec = (set(marks for name, marks in physics_score))
    sec = sorted(list(sec))
    print('\n'.join([name for name, marks in sorted(physics_score) if marks == sec[1]]))
