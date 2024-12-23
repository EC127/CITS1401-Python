def netsession(players):
    batsman = []
    bowler = [] 
    keeper = []
    teams = []
    for item in players:
        role = item[1].split('-')
        for x in role:
            if x == 'bat':
                batsman.append(item[0])
            if x == 'bowl':
                bowler.append(item[0])
            if x == 'keeper':
                keeper.append(item[0])
    for i in range(len(batsman)):
        for j in range(len(bowler)):
            for k in range(len(keeper)):
                if batsman[i]==bowler[j] or batsman[i]==keeper[k] or bowler[j]==keeper[k]:
                    continue   
                teams.append(batsman[i] + "-" + bowler[j] + "-" + keeper[k])
    return teams