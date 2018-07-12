import cell
import automaton
import random

test_type = 0

if(test_type == 0):
    automaton = automaton.Automaton()
    automaton.traffic_flow_setup(ring_size=10, car_num = 6)
    STEP_SIZE = 10
    print(automaton)
    for index in range(STEP_SIZE):
        automaton.step()
        print(automaton)

elif (test_type == 1):
    STEP_SIZE = 10
    automaton = automaton.AutomatonAlt()
    automaton.traffic_flow_setup(
        branch_index=2, connecting_index=4, ring_size=5, alt_size=1, car_num=4)

    printtype = 'all'
    print(automaton)
    print('\n\n')

    for index in range(STEP_SIZE):
        if (printtype == 'all'):
            print(automaton)
            print()
        elif (printtype == 'main'):
            print(automaton.strMain())
        elif (printtype == 'alt'):
            print(automaton.strAlt())
        automaton.step()
