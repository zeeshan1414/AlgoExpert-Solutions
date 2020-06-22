def getAllPeaks(arr):
    peaks = []
    n = len(arr)
    if n == 1:
        peaks.append(arr[0])
        return peaks
    elif n == 2:
        peaks.append(max(arr[0], arr[1]))
        return peaks

    for i in range(1, n - 1):
        if arr[i - 1] < arr[i] > arr[i + 1]:
            peaks.append(arr[i])

    return peaks


# O(N) time | O(1) space
def longestPeak(arr):
    longest = 0
    i = 1
    while i < len(arr) - 1:
        isPeak = arr[i - 1] < arr[i] and arr[i] > arr[i + 1]
        if not isPeak:
            i += 1
            continue

        leftIdx = i - 2
        while leftIdx >= 0 and arr[leftIdx] < arr[leftIdx + 1]:
            leftIdx -= 1
        rightIdx = i + 2
        while rightIdx < len(arr) and arr[rightIdx] < arr[rightIdx - 1]:
            rightIdx += 1

        currentPeakLen = rightIdx - leftIdx - 1
        longest = max(currentPeakLen, longest)
        i = rightIdx
    return longest


if __name__ == "__main__":
    arr = [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]
    print(longestPeak(arr))
