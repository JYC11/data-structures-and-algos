
for test_case in range(1,11):
    floor_count = 0
    building_count = int(input())
    buildings = list(map(int,input().split()))
    
    for i in range(2,building_count-2):
        tallest = max([buildings[i-2],buildings[i-1],buildings[i+1],buildings[i+2]])
        if buildings[i] > tallest:
            floor_count += buildings[i] - tallest

    print(f"#{test_case} {floor_count}")