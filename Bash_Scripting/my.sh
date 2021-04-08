!/bin/bash
# This is a basic bash script
 #ls 

# #echo statement display text to the standrat output. We can use single qupte
#  #double quote. Use escape back slash \ to print quote or variable.
# #if you want to add empty line to your output just time echo & nothing after it.
# greeting="Dash"
# echo #empty line
# echo $greeting, world \(planet\)!
# echo '$greeting, world (planet)'

# echo "\greeting, world (planet)!" 
# echo #empty line

# a=xogirls
# b="vog"
# c=240
# echo $a
# echo $b
# echo $c

# echo "$a are $c"


# echo

# #variabkle substitution
# a=$(ping -c 1 google.com | grep 'bytes from' | cut -d =  -f 4 )
# echo "sever took $a to respond" 

# echo

# # Arithmetic operations
# d=2
# e=$((d+2))
# echo Doing some math :
# echo $e

# ((e++))
# echo $e

# ((e--))
# echo $e

# ((e+=5))
# echo $e

# ((e-=2))
# echo $e

# ((e*=3))
# echo $e

# ((e/=3))
# echo $e

# g=$(echo 1/3 | bc -l)
# echo $g


# #Comparison Operator

# # ---For working with text ----------

# [[ "cat" == "cat" ]]
# echo $? # echo the return value -->$?

# [[ "cat" = "dog" ]] # we can also use single = for equality
# echo $?

# #---------Working with integers --------
# [[ 20 >  100 ]] # yield 0 for success but that's wrong
# echo $?

# [[ 20  -gt 100 ]] # yield 1 for failure but that's correct
# echo $?

# #-------Working with logocal operators --------
# #Using logical operator check if a is null , b is not null
# a=""
# b="cat"

# [[  -z $a  &&  -n $b  ]] # remember to use proper spaces between parenthesis
# echo $?

#============Working with strings---------------
# fruit="apple banana banana cherry"
# echo ${fruit/banana/james}
# echo $fruit

#echo -e "\033[5;33;40mError: \033[0m\033[33;41mWe have been hacked! \033[0m"

echo

# using variables to make it easy on us
# flashred="\033[5;33;41m"
# green="\033[0m"
# none="\033[33;41m"
# echo -e $flashred"ERROR:"$none$green" We have been hacked!"$none


echo


# flashred=$(tput setab 2; tput setaf 1; tput blink)
# green=$(tput setab 0; tput setaf 1)
# none=$(tput sgr0)

# echo -e $flashred"WARNING: "$none$green"Major system failure!"$none

# echo
# -------Formating dates-------

# today=$(date +"%d-%m-%Y")
# time=$(date +"%H:%M:%S")
# printf -v d "Current User:\t%s\nDate:\t\t%s @ %s\n" $USER $today $time
# echo "$d" # we use quote to preserve the new line

# #---------Working with arrays-----------
# b=("apple" "banana" "cherry") #FYi no comma needed
# echo  ${b[1]} 
# b[5]="Kiwi" #adding by using an index
# b+=("mango") #using += to add item to the end of the array
# echo ${b[@]}
# echo ${b[@]: -1} # Grab the last element 

# # -------Key-Pair value in array----------
# # -----Code below  will not work in bash 3 & below --------
# #declare -A myarray
# # myarray[color]=blue
# # myarray["office building"]="HQ West"

# # #access those values by using the keys
# # echo ${myarray["Office Building"]} is ${myarray[color]}

# #-----------Reading & Writing Text File------------#


# # Reading file content
# i=1
# while read f; do
#         echo "Line $i: $f"
#         ((i++))
# done < file.txt 


# #--------- Here Doc------
# # Useful to display long passage of text

# cat <<- EndOfText # << - the dash remove the leading tab make text more readable
# #cat << EndOfText
# This is a 
# multiline
# text string
# EndOfText

echo


#---------testing Truth Conditions -------
# a=5
# if [ $a -gt 4 ]; then
#         echo $a is greater than 4! 
# else
#         echo $a is not greater than 4!
# fi

# echo

# i=0
# while [  $i -le 10  ]; do 
#         echo i:$i #print i & index
#         ((i+=1)) # keep incrementing i by 1 til we done.
# done 

# echo

# # until Loop is the counter part of the while-Loop 
# j=0
# until [ $j -ge 10 ]; do
#         echo j:$j
#         ((j+=1))
# done

# echo

#-------Working with for loop
# for i in 1 2 3
# do
#         echo $i
# done

# echo 

# # list all numbers from 1 to 100
# for j in {1..100}
# do 
#         echo $j
# done

# #----Loop through an array 
# arr=("apple" "banana" "cherry")
# for i in ${arr[@]}
# do
#         echo $i
# done

# echo

#---------working with case-statement for user input & less if-else statements
# a="dog"
# case $a in 
#         cat) echo "Feline";;
#         dog | puppy) echo "Canine";;
#         *)  echo "No match!";;
# esac

# echo

# #---------working with Dash Functions------
# #Use for function for less code repetitions DRY
# function greet {
#     echo "Hi There !"
# }
# echo "And now, a greeting "

# #call the function
# greet

# echo

# function greet2 {
#     echo "Hi $1! what a nice $2"
# }
# echo "And now, a greeting "

# #call the function
# greet2 jldroid25 day

# echo

# function numberthings {
#     i=1
#     for f in $@; do
#             echo $i: $f
#             ((i+=1))
#     done
# }

# numberthings $(ls)
# numberthings cassioppe maya jade syra lola keira 

#-------working with variables-------------

# echo $1

# for i in $@
# do

#         echo $i
# done

# echo "There were $# arguments."

# while getopts u:p: option; do
#         case $option in 
#                 u) user=$OPTARG;; # we are looking for -u
#                 p) pass=$OPTARG;; # we are looking for -p
#         esac
# done

# echo "User: $user / Pass: $pass"

#-------adding a 3rd option :ab

# while getopts u:p:ab option; do
#         case $option in 
#                 u) user=$OPTARG;; # we are looking for -u
#                 p) pass=$OPTARG;; # we are looking for -p
#                 a) echo "Got the A flag";;
#                 b) echo "Got the B flag";;
#         esac
# done

# echo "User: $user / Pass: $pass"

# # adding a colon before :u tells  Bash I want to know about flags
# # used on the terminal that I did not specify
# while getopts :u:p:ab option; do
#         case $option in 
#                 u) user=$OPTARG;; # we are looking for -u
#                 p) pass=$OPTARG;; # we are looking for -p
#                 a) echo "Got the A flag";;
#                 b) echo "Got the B flag";;
#                 ?) echo "I don't know what $OPTARG is !";;
#         esac
# done

# echo "User: $user / Pass: $pass"

# run script with --> ./my.sh -u jldroid25 -p secret -z or -a or -b

# #--------- Getting user input during the execution of the script

# echo "What is your name? "
# read name # "read" pause the script to wait for input & save value in var "name" 

# echo "Waht is your password"
# read -s pass # -s means silent & will not show the characters being typed

# read -p "What's your favorite car ?" car

# #let's print all that out
# echo name: $name, pass: $pass, car: $car

# select option in "Update" "Save" "Quit"
# do 
#         case $option in
#                 Update) echo "for updating existing data";;
#                 Save) echo "for saving your data";;
#                 Quit) break;;
#                 *) echo "I'm not sure what that us.";;
#         esac
# done

# read -p "Favorite animal? " a
# # -z option is to check the variable a is not empty
# while [[ -z "$a" ]]; do
#         read -p "I need an answer ! " a
# done
# echo "$a was selected. "

# 2nd Option - assume an answer if nothing was entered
# read -p "Favorite animal? " a
# # -z option is to check the variable a is not empty
# while [[ -z "$a" ]]; do
#         a="cat"
# done
# echo "$a was selected. "

read -p "what year ? " a
# -z option is to check the variable a is not empty
while [[ ! $a =~ [0-9]{4} ]]; do
        read -p "A year , please! [nnnn] " a
        
done

echo "selected year $a"