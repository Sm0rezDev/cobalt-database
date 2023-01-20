from cobalt import Cobalt


if __name__ == '__main__':
    cbd = Cobalt()
    
    cbd.select_table('devs')

    for data in cbd.fetch('', ''):
        print(data)