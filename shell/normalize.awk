{
    num1 = split($1, arr1, " ")
    num2 = split($3, arr2, " ")
    print $1"\t"$2/num1"\t"$3"\t"$4/num2
}
