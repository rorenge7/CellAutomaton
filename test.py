import cell
import automaton
import random

test_type = 1

if(test_type == 0):
    automaton = automaton.Automaton()
    automaton.traffic_flow_setup(ring_size=40, car_num = 21)
    STEP_SIZE = 100
    print(automaton)
    for index in range(STEP_SIZE):
        automaton.step()
        print(automaton)

elif (test_type == 1):
    STEP_SIZE = 10
    automaton = automaton.AutomatonAlt()
    automaton.traffic_flow_setup(
        branch_index=2, connecting_index=5, ring_size=10, alt_size=2, car_num=7)

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
