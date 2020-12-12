from calculator import Calculator
from random import choice

if __name__ == "__main__":
    # Show time
    c = Calculator()
    print('Welcome to Calculator :)\n')

    while(True):

        try:
            pharse = input(
                choice(
                    [
                        'What should i calculate? ',
                        "Ok what's next? ",
                        "Yeah i'm readyy: ",
                        "Come on... give me something: "
                    ]
                )
            )

            if pharse.lower() == 'exit':
                print('\n' + c.show_results)
                break

            if pharse.lower() == 'cancel':
                print('\nOk!\n')
                continue

            if pharse.lower() == 'results':
                print('\n' + c.show_results + '\n')
                continue

            if pharse.lower() == 'clear':
                c.clear()
                print('\nResults Cleared!\n')
                continue

            if pharse.lower().startswith('result'):
                index = int(pharse.split(' ')[-1])
                print(f'\n{c.get_result(index)["result"]}\n')
                continue

            if pharse.lower().startswith('append'):
                index = int(pharse.split(' ')[-1])
                appened = str(c.get_result(index)["result"])
                pharse = appened + input(f'\nOk keep going: {appened}')  
                try:
                    print('\nResult:', c.direct_calculate(pharse), '\n')
                except Exception as e:
                    print('\nFailed please try again\n', e)  
                continue            

            try:
                print('\nResult:', c.direct_calculate(pharse), '\n')
            except Exception as e:
                print('\nFailed please try again\n', e)
        except KeyboardInterrupt:
            print('\nExited!')
            break
