from copy import deepcopy
from random import choice


candidates = {'Borussia Dortmund':
				{'Country': 'Germany',
				 'Group': 'A',
				 'Rank': 1
				},
			 'Atlético Madrid':
				{'Country': 'Spain',
				 'Group': 'A',
				 'Rank': 2
				},
			 'Barcelona':
				{'Country': 'Spain',
				 'Group': 'B',
				 'Rank': 1
				},
			 'Tottenham Hotspur':
				{'Country': 'England',
				 'Group': 'B',
				 'Rank': 2
				},
			 'Paris Saint-Germain':
				{'Country': 'France',
				 'Group': 'C',
				 'Rank': 1
				},
			 'Liverpool':
				{'Country': 'England',
				 'Group': 'C',
				 'Rank': 2
				},
			 'Porto':
				{'Country': 'Portugal',
				 'Group': 'D',
				 'Rank': 1
				},
			 'Schalke 04':
				{'Country': 'Germany',
				 'Group': 'D',
				 'Rank': 2
				},
			 'Bayern Munich':
				{'Country': 'Germany',
				 'Group': 'E',
				 'Rank': 1
				},
			 'Ajax':
				{'Country': 'Netherlands',
				 'Group': 'E',
				 'Rank': 2
				},
			 'Manchester City':
				{'Country': 'England',
				 'Group': 'F',
				 'Rank': 1
				},
			 'Lyon':
				{'Country': 'France',
				 'Group': 'F',
				 'Rank': 2
				},
			 'Real Madrid':
				{'Country': 'Spain',
				 'Group': 'G',
				 'Rank': 1
				},
			 'Roma':
				{'Country': 'Italy',
				 'Group': 'G',
				 'Rank': 2
				},
			 'Juventus':
				{'Country': 'Italy',
				 'Group': 'H',
				 'Rank': 1
				},
			 'Manchester United':
				{'Country': 'England',
				 'Group': 'H',
				 'Rank': 2
				},
			}

winners = [t for t in candidates if candidates[t]['Rank'] == 1]
runners_up = [t for t in candidates if candidates[t]['Rank'] == 2]


def draw_opponent(team, remaining_winners):
	legal_draws = [t for t in remaining_winners if (candidates[t]['Country'] != candidates[team]['Country'] and candidates[t]['Group'] != candidates[team]['Group'])]
	opponent = choice(legal_draws)

	return opponent


def main():
	this_winners = deepcopy(winners)
	this_runners_up = deepcopy(runners_up)
	while this_runners_up:
		team = choice(this_runners_up)
		this_runners_up.remove(team)
		opponent = draw_opponent(team=team, remaining_winners=this_winners)
		this_winners.remove(opponent)
		print(f'{team} vs. {opponent}')


if __name__ == '__main__':
	main()
