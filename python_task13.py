R1 = float(input('Enter the radius of the circle: '))
R2 = float(input('Enter the radius of the circle: '))
if R1 < R2:
    print('Error: R1 should be greater than or equal to R2.')
else:
    S1 = 3.14 * R1**2
    S2 = 3.14 * R2**2
    S3 = S1 - S2
    print('The area of the larger circle is: ', round(S1, 2))
    print('The area of the smaller circle is: ', round(S2, 2))
    print('The area of the ring is: ', round(S3, 2))