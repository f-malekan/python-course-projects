def main():

    result = {
        "Spain": {
            "wins": 0,
            "looses": 0,
            "draws": 0,
            "goal_difference": 0,
            "points": 0
        },
        "Iran": {
            "wins": 0,
            "looses": 0,
            "draws": 0,
            "goal_difference": 0,
            "points": 0
        },
        "Portugal": {
            "wins": 0,
            "looses": 0,
            "draws": 0,
            "goal_difference": 0,
            "points": 0
        },
        "Morocco": {
            "wins": 0,
            "looses": 0,
            "draws": 0,
            "goal_difference": 0,
            "points": 0

        }
    }

    matches = [
        ["Iran", "Spain"],
        ["Iran", "Portugal"],
        ["Iran", "Morocco"],
        ["Spain", "Portugal"],
        ["Spain", "Morocco"],
        ["Portugal", "Morocco"]
    ]

    for match in matches:

        match_result = input().split('-')
        goal_diff = abs(int(match_result[0])-int(match_result[1]))
        if (int(match_result[0]) > int(match_result[1])):
            result[match[0]]['wins'] = result[match[0]]['wins'] + 1
            result[match[0]]['points'] = result[match[0]]['points'] + 3
            result[match[0]]['goal_difference'] = result[match[0]]['goal_difference'] + goal_diff

            result[match[1]]["looses"] = result[match[1]]["looses"]+1
            result[match[1]]['goal_difference'] = result[match[1]]['goal_difference'] - goal_diff

        elif (int(match_result[0]) == int(match_result[1])):
            result[match[1]]['draws'] = result[match[1]]['draws'] + 1
            result[match[1]]['points'] = result[match[1]]['points'] + 1

            result[match[0]]['draws'] = result[match[0]]['draws'] + 1
            result[match[0]]['points'] = result[match[0]]['points'] + 1
        else:
            result[match[1]]['wins'] = result[match[1]]['wins'] + 1
            result[match[1]]['points'] = result[match[1]]['points'] + 3
            result[match[1]]['goal_difference'] = result[match[1]]['goal_difference'] + goal_diff

            result[match[0]]["looses"] = result[match[0]]["looses"]+1
            result[match[0]]['goal_difference'] = result[match[0]]['goal_difference'] - goal_diff

    sorted_teams = sort_results(result)

    for team in sorted_teams:
        data = result[team]
        print('{} wins:{} , loses:{} , draws:{} , goal difference:{} , points:{}'.format(team, data['wins'], data['looses'], data['draws'], data['goal_difference'], data['points']))



def sort_results(data):
    country=list(data.keys())
    country.sort(reverse=True)
    n = len(country)

    for i in range(n):
        for j in range(0, n-i-1):

            if data[country[j]]['points'] > data[country[j+1]]['points']:
              country[j], country[j+1] = country[j+1], country[j]
            elif data[country[j]]['points'] == data[country[j+1]]['points']:
                if data[country[j]]['wins'] > data[country[j+1]]['wins']:
                    country[j], country[j+1] = country[j+1], country[j]


                
    return list(reversed(country))

if __name__ == '__main__':
    main()