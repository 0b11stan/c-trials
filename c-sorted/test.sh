function test() {
    TEST_DESCRIPTION=$1
    TEST_WORDS=$2
    TEST_EXPECT=$3

    tput setaf 7 && printf "Test %s - " "$TEST_DESCRIPTION"

    ./sorted $TEST_WORDS
    if [[ $? -eq $TEST_EXPECT ]]; then
        tput setaf 2 && printf 'SUCCESS\n' 
    else
        tput setaf 1 && printf 'FAILURE\n'
    fi
}

test "empty exection" "" 0
test "2 unordered words" "aa a" 1
test "3 unordered words" "aa a aaa" 1
test "3 unordered words" "aaa aa a" 1
test "4 unordered words" "aaa aa a aaaa" 1
test "unordered sentence" "another one got caught today it s all over the papers" 1
test "2 ordered words" "a aa" 0
test "3 ordered words" "a aa aaa" 0
test "4 ordered words" "a aa aaa aaa" 0
test "ordered sentence" "s it the all got one over today papers caught another" 0
