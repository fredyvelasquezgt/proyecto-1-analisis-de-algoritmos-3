import sys

def turing_machine():
    # Load components of Turing machine from file
    with open('fibonacci.tm') as f:
        components = [line.strip().split(' ') for line in f.readlines()]

    # Load configuration of Turing machine from file
    with open('config.txt') as f:
        configuration = [line.strip().split(' ') for line in f.readlines()]

    # Initialize tape and head position
    tape = list(configuration[1][0])
    head = 0

    # Set initial state
    state = configuration[0][0]

    # Loop until halting state is reached
    while state != configuration[3][0]:
        # Search for current state and current symbol in components
        for i, component in enumerate(components):
            if component[0] == state and component[1] == tape[head]:
                # Update tape symbol
                tape[head] = component[3]

                # Move head position
                if component[4] == 'R':
                    head += 1
                else:
                    head -= 1

                # Update state
                state = component[2]

                # Print current configuration
                print(f'{state} {" " * head}{"V"}')
                print(f'{" " * (len(state) + head)}{"^"}')
                print(' '.join(tape))

                break
        else:
            # No matching component found
            print('Error: Invalid input.')
            sys.exit(1)

    # Print final tape contents
    print('Result: ' + ''.join(tape))

if __name__ == '__main__':
    turing_machine()
