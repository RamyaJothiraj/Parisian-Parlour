def equilateral(sides):
    a,b,c = sides

    return a == b == c and a > 0 


def isosceles(sides):
    a,b,c = sides

    if a<=0 or b<=0 or c<=0:
        return False
    if a+b<c or b+c<a or a+c<b:
        return False

    return a==b or b==c or a==c


def scalene(sides):
    a,b,c = sides

    if a<=0 or b<=0 or c<=0:
        return False
    if a+b<c or b+c<a or a+c<b:
        return False

    if a==b or b==c or a==c:
        return False

    return True

    
