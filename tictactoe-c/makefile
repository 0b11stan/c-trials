TICTACTOE_EXE=tictactoe
TICTACTOE_TEST_EXE=test
SOURCES=core/core.c ihm/ihm.c
TEST_SOURCES=$(SOURCES) core/test.c ihm/test.c
BUILD_DIR=build

RUN_PATH=./$(BUILD_DIR)/$(TICTACTOE_EXE)
TEST_PATH=./$(BUILD_DIR)/$(TICTACTOE_TEST_EXE)

run: build
	$(RUN_PATH)

test: build_tests
	$(TEST_PATH)

build: prepare
	gcc $(SOURCES) main.c -o $(RUN_PATH)

build_tests: prepare
	gcc $(TEST_SOURCES) tests.c -o $(TEST_PATH)

prepare:
	stat $(BUILD_DIR) &> /dev/null || mkdir $(BUILD_DIR)

clean:
	! stat $(BUILD_DIR) &> /dev/null || rm -rf $(BUILD_DIR)
