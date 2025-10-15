import sys

# 병합 정렬 함수 정의
def merge_sort(a):
    n = len(a)
    if n <= 1:
        return a
    mid = n // 2
    left = merge_sort(a[:mid])
    right = merge_sort(a[mid:])
    return merge(left, right)

# 병합 과정 정의
def merge(left, right):
    i = j = 0
    result = []
    # 두 리스트를 병합하면서 정렬
    while i < len(left) and j < len(right):
        # 튜플 비교
        if left[i] <= right[j]:
            result.append(left[i]); i += 1
        else:
            result.append(right[j]); j += 1
    if i < len(left):  result.extend(left[i:])
    if j < len(right): result.extend(right[j:])
    return result

def main():
    input = sys.stdin.readline
    n = int(input().strip())
    items = []

    # 각 선수의 정보 입력
    for _ in range(n):
        b, p, q, r = map(int, input().split())
        # b: 선수 등번호, p/q/r: 세 종목 순위
        prod = p * q * r  # 세 종목 순위의 곱
        ssum = p + q + r  # 세 종목 순위의 합
        items.append((prod, ssum, b))

    sorted_items = merge_sort(items)

    # 상위 3명
    top_k = min(3, n)
    ans = [sorted_items[i][2] for i in range(top_k)]  # 등번호만 추출
    print(*ans)

if __name__ == "__main__":
    main()