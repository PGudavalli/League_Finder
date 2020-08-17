from riotwatcher import LolWatcher, ApiError
import pandas as pd
import csv

api_key = 'RGAPI-1a2fc345-2d9b-4d05-97c4-72dabcf03782'
watcher = LolWatcher(api_key)
my_region = 'na1'

username = input('Username: ')
check = input('Which user do you want to check? ')

me = watcher.summoner.by_name(my_region, username)
my_matches = watcher.match.matchlist_by_account(my_region, me['accountId'], begin_index=0, end_index=200)
#print(my_matches)
match_c = my_matches['matches']
endpoint = 100
print(len(match_c))
def find_matches(player_match, reference, endpoint):
    boi = 0
    for x in range(0,endpoint+1):
        ok = False
        current_match = watcher.match.by_id(my_region, player_match[x]['gameId'])
        #print(x)
        for player in current_match['participantIdentities']:
            if player['player']['summonerName'] == reference:
                #return True
                ok = True
            else:
                pass
        if ok:
            boi += 1
    if(boi >= 1):
        print('You have played with ' f'{reference}' ' this many times: ' f'{boi}' ' in the past ' f'{endpoint}' ' games.')
    else:
        print('Sorry but nope')
    
#find_matches(match_c, check, endpoint)




