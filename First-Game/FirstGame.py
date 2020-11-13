print("Welcome to my first game")
name = input("What is your name? ")
age = int(input("What is your age? "))

health = 10

if age >= 18:
    print("You are old enough to play")

    wants_to_play = input("Do you want to play? ").lower()
    if wants_to_play == "yes":
        print("You are starting with", health, "health")
        print("Let's Play!")

        left_or_right = input("First choice... Left or Right (left/ right)?")
        if left_or_right == "left":
            ans = input("Nice, you follow the path and reach a lake... Do you swim across or go around (across/ around)?")

            if ans == "around":
                print("You went around and reached the other side of the lake")
            elif ans == "across":
                print("You managed to get across, but were bit by a fish and lost 5 health")
                health -= 5
            ans = input("You noticed a house and a river. Which do you go to (river/house)?")
            if ans == "house":
                print("You are greeted by the 3 little pigs. They hit you for trespassing. You lost another 5 healths ")
                health -= 5

                if health <= 0:
                    print("You now have 0 health. You lose the game")
                else:
                    print("you have survived. You win")
            else:
                print("There was a flash flood and you got swept. Lost 5 health.")
                print("You grabbed onto a branch and pulled yourself up. Do you follow the river or out of the forest ")
                ans = input("(follow/ out)?")

                if ans == "out":
                    print("You reached civilization. You win")
                else:
                    print("You got caught in another flash flood and died")

        else:
            print("You stepped onto the road and got hit by a bus. You lost...")
    else:
        print("Good Bye...")

else:
    print("You are not old enough to play...")