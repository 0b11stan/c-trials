function test() {
    TEST_DESCRIPTION=$1
    TEST_WORDS=$2
    TEST_EXPECT=$3

    tput setaf 7 && printf "Test %s - " "$TEST_DESCRIPTION"

    if [[ "$(./msort $TEST_WORDS)" == "$TEST_EXPECT" ]]; then
        tput setaf 2 && printf 'SUCCESS\n' 
    else
        tput setaf 1 && printf 'FAILURE\n'
    fi
}

test "empty exection" "" ""
test "sorting 2 unordered words" "aa a" "a aa"
test "sorting 2 ordered words" "a aa" "a aa"
test "sorting 3 ordered words" "a aa aaa" "a aa aaa"
test "sorting 3 unordered words" "aa a aaa" "a aa aaa"
test "sorting 3 unordered words" "aaa aa a" "a aa aaa"
test "sorting 4 unordered words" "aaa aa a aaaa" "a aa aaa aaaa"
test "sorting a sentence" "another one got caught today it s all over the papers" "s it the all got one over today papers caught another"
