def nhonhat():
    min = 10
    numbers = [10,1,4,5,2]
    for num in numbers:
        if num < min:
            min = num
    print("Số nhỏ nhất là :", min)
if __name__=="__main__":
    nhonhat()