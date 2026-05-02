while True:
       cmd2 = input('>').lower()
       if cmd2 == 'help':
        print('start - to start the car')
        print('stop - to stop the car')
        print('quit - to exit')
       elif cmd2 == 'start':
        print('Car started...Ready to go!')
       elif cmd2 == 'stop':
        print('car stopped.')
       elif cmd2 == 'quit':
        print('Exiting...')
        break
       else:
        print(' I don\'t understand that command.')
       