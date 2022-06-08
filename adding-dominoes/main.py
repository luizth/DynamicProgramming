import sys
from typing import List

from model.Domino import Domino
from model.DominoesSet import DominoesSet

from utils.count_file import reset_count, check_count
from utils.validative_algorithms import subset_sum


def main() -> None:

    try:
        if len(sys.argv) > 2:
            print('Incorrect arguments: $ python main.py <test_case>')
            return

        test_case = sys.argv[1]
    except:
        test_case: str = ''

    set_list: List[DominoesSet] = read_set_file(file_name=f'test_cases/in{test_case}')

    for dominoes_set in set_list:

        # Check for highest value dominoes set candidate.
        dominoes_set.sort_by_weight()

        removed_domino = None
        candidate_dominoes_set = None
        if dominoes_set.diff & 1 == 0:  # performatic way of checking if a number is even
            candidate_dominoes_set = dominoes_set
        else:
            # Copying the set of dominoes.
            dominoes_set_temp = DominoesSet(dominoes=dominoes_set.dominoes.copy())

            for i in range(len(dominoes_set.dominoes)):

                # Store if any domino was removed from the set to make it a candidate.
                removed_domino = dominoes_set_temp.remove_domino(index=i)

                if dominoes_set_temp.diff & 1 == 0:
                    candidate_dominoes_set = dominoes_set_temp
                    break

                dominoes_set_temp = DominoesSet(dominoes=dominoes_set.dominoes.copy())

        if candidate_dominoes_set is None:
            print('impossível')
            return

        reset_count()
        dominoes_set_diffs = [domino.diff for domino in candidate_dominoes_set.dominoes]
        target = int(candidate_dominoes_set.diff/2)

        # Validate if it is possible to match the target by flipping dominoes.
        subset_sum(numbers=dominoes_set_diffs, target=target)

        if not check_count():
            print('impossível')
        else:
            set_sum = int(candidate_dominoes_set.weight / 2)

            if removed_domino is None:
                print(str(set_sum) + ' nenhum dominó descartado')
            else:
                str_removed_domino = str(removed_domino.domino[0]) + ' ' + str(removed_domino.domino[1])
                print(str(set_sum) + ' descartado o dominó ' + str_removed_domino)


def read_set_file(file_name: str) -> List[DominoesSet]:
    set_list: List[DominoesSet] = []
    dominoes_set: DominoesSet = DominoesSet()

    try:
        with open(file_name, 'r') as f:
            for line in f:
                splitted_line: list = line.split()

                # Create dominoes set.
                if len(splitted_line) == 1:

                    if dominoes_set.size > 0:

                        if dominoes_set.size != curr_set_size:
                            raise Exception('Set size does not match with input file.')

                        set_list.append(dominoes_set)

                    dominoes_set: DominoesSet = DominoesSet()
                    curr_set_size: int = int(splitted_line[0])  # control variable

                # Append domino to current domino set.
                else:
                    upper: int = int(splitted_line[0])
                    lower: int = int(splitted_line[1])

                    if upper > lower:
                        upper, lower = lower, upper

                    domino: Domino = Domino(upper=upper, lower=lower)
                    dominoes_set.append_domino(domino)

    except Exception as e:
        print(f'[Error] Error during file read: {e}')

    return set_list


main()
