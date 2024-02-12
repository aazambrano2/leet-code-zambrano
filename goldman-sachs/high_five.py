


def highFive(items):
    from collections import defaultdict
    import heapq

    # Create a dictionary to store the scores of each student
    scores = defaultdict(list)

    # Iterate through each item in items
    for student, score in items:
        # Push the score into the heap of the corresponding student
        heapq.heappush(scores[student], score)
        # If more than 5 scores are stored, remove the smallest one
        if len(scores[student]) > 5:
            heapq.heappop(scores[student])

    # Calculate the average of the top 5 scores for each student
    result = []
    for student in sorted(scores):
        avg = sum(scores[student]) // 5
        result.append([student, avg])

    return result






if __name__ == '__main__':
    items = [[1,100],[7,100],[1,100],[7,100],[1,100],[7,100],[1,100],[7,100],[1,100],[7,100]]
    print(highFive(items))