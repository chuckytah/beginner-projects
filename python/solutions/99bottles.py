TOTAL_BOTTLES_OF_BEER = 99

def bottle_vs_bottles(n):
    if n == 0:
        return "no more bottles"
    elif n == 1:
        return str(n) + " bottle"
    else:
        return str(n) + " bottles"

def print_song():
    for x in range(TOTAL_BOTTLES_OF_BEER, -1, -1):
        if x == 0:
            print(bottle_vs_bottles(x).capitalize(),"of beer on the wall,",bottle_vs_bottles(x),"of beer.\nGo to the store and buy some more,",bottle_vs_bottles(TOTAL_BOTTLES_OF_BEER),"of beer on the wall.")
        else:
            print(bottle_vs_bottles(x),"of beer on the wall,",bottle_vs_bottles(x),"of beer.\nTake one down and pass it around,",bottle_vs_bottles(x-1),"of beer on the wall.\n")

if __name__ == "__main__":
    print_song()