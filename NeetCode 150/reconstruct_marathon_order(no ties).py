def reconstruct_marathon_order(finished_immediately_before):
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
        print('then', next)
        answer.append(next)
        if not next in pairs:
            break
    return answer
