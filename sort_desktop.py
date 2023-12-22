def solution(wallpaper):
    a = []
    b = []
    for row in range(len(wallpaper)):
        for col in range(len(wallpaper[row])):
            if  wallpaper[row][col] == '#':
                a.append(row)
                b.append(col)
                
    answer = [min(a) , min(b) , max(a)+1 , max(b)+1]
    return answer

wallpaper = [".#...", "..#..", "...#."]
print(solution(wallpaper))