def reconstruct_marathon_order(finished_immediately_before):
    """
    Reconstructs the order of students finishing a marathon based on the given input.

    Args:
        finished_immediately_before: A list where finished_immediately_before[i] = j
        means that student with id j finished just before student with id i.
        finished_immediately_before[k] = -1 means that k is the first student.

    Returns:
        A list of student IDs in the order they finished the marathon.
    """
    #Init new dict pairs
    pairs = {}
    answer = []
    #Set up pairs with placement as key and student id (index of finished_immediately_before) as value
    for i, val in enumerate(finished_immediately_before):
        pairs[val] = i
    print(pairs)
    next = pairs[-1]
    answer.append(next)
    #Reconstruct array in win order
    print(next, 'wins! Followed by')
    while True:
        next = pairs[next]
        print(next, 'then')
        answer.append(next)
        if not next in pairs:
            break
    return answer

from collections import defaultdict

def reconstruct_marathon_order_ties(finished_immediately_before_ties):
    pairs = defaultdict(list)
    answer = []
    for i, val in enumerate(finished_immediately_before_ties):
        pairs[val].append(i)
    print(pairs)

    nextList = pairs.pop(-1)
    answer.append(nextList)

    print(answer)
    while True:
        found = False
        for next in nextList:
            if pairs.get(next):
                nextList = pairs.pop(next)
                answer.append(nextList)
                print(nextList)
                found = True
                continue
        if found == False:
            break

    return answer

from queue import Queue
def reconstruct_marathon_order_queue(finished_immediately_before_ties):
    pairs = defaultdict(list)
    answer = []
    for i, val in enumerate(finished_immediately_before_ties):
        pairs[val].append(i)
    print(pairs)

    #nextList = pairs.pop(-1)
    #answer.append(nextList)

    finish_line = Queue(maxsize=len(finished_immediately_before_ties))
    # Is there a more pythonic way to set up the initial state of the queue
    first = pairs.pop(-1)
    for winners in first:
        finish_line.put(winners)
    while not finish_line.empty():
        finisher = finish_line.get()
        answer.append(finisher)
        runners_up = pairs.get(finisher)
        if runners_up: # Would you recommend a cleaner / implicitly safer way to add the runner-ups to the queue?
            for runner_up in pairs.get(finisher):
                finish_line.put(runner_up)
    return answer


from collections import deque, defaultdict
def reconstruct_marathon_order_dequeue(finished_immediately_before_ties):
    pairs = defaultdict(list)
    answer = []
    for i, val in enumerate(finished_immediately_before_ties):
        pairs[val].append(i)
    print(pairs)

    visited = set()
    finishers = deque()

    winners = pairs.pop(-1)
    finishers.extend(winners)
    while finishers:
        finisher = finishers.popleft()
        answer.append(finisher)
        print(finisher)
        for runner_up in pairs.get(finisher, []):
            if runner_up not in visited:
                finishers.append(runner_up)
                visited.add(runner_up)
    return answer

def main():
    finished_immediately_before = [1, 2, -1, 0]
    finished_immediately_before_ties = [1, 2, -1, 0, 2, -1, 7, 5]
    result = reconstruct_marathon_order_dequeue(finished_immediately_before_ties)
    print(result)

if __name__ == "__main__":
    main()

