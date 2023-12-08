def solution(arr, queries):
    answer = []
    if len(arr) < 1 or len(arr) > 1000:
        print(f"arr length Error : {len(arr)}")
        return -1
    if len(queries) < 1or len(queries) > 1000:
        print(f"queries length Error : {len(queries)}")
        return -1

    for (s,e,k) in queries:
        if k == 0:
            print(f"k value Error : {k}")
            continue
            
        for idx in range(s, e+1):
            if idx%k == 0:
                arr[idx] += 1
    answer = arr
    return answer