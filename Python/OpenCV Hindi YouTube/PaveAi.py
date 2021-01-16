alpha = sorted(input())
print(alpha)

alpha_new = []

def Rev_Alpha(input):
    zero = 0
    len_a = len(alpha)

    for i in input:
        ap = input.copy()
        ap[zero] = ap[len_a - 1]
        alpha_new.append(ap[zero])

        zero = zero + 1
        len_a = len_a - 1

Rev_Alpha(alpha)
print(alpha_new, "-----------Main------------")