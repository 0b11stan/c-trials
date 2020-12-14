import unittest
import main
import numpy


def get_test_weight_matrix():
    return [
        [
            [None],
            [None]
        ], [
            [0.5, 0.5],
            [0.5, 0.5],
            [0.5, 0.5],
            [0.5, 0.5],
            [0.5, 0.5]
        ], [
            [0.5, 0.5, 0.5, 0.5, 0.5]
        ]
    ]


def get_test_prediction_matrix():
    return [
        [
            0,
            0
        ], [
            0.2,
            0.2,
            0.2,
            0.2,
            0.2
        ], [
            0.1
        ]
    ]


class NeuralNetworkTester(unittest.TestCase):

    def test_build_random_weight_matrix(self):
        description = [2, 10, 1]
        weights = main.build_weight_matrix(description)
        random_verification = []
        self.assertEqual(len(description), len(weights))
        for layer in range(len(weights)):
            self.assertEqual(description[layer], len(weights[layer]))
            for neuron in range(len(weights[layer])):
                self.assertEqual(description[layer - 1], len(weights[layer][neuron]))
                for weight in weights[layer][neuron]:
                    self.assertNotIn(weight, random_verification)

    def test_compute_neuron(self):
        inputs, weights = [1, 1], [1, 1]
        expect = "0.88079707"
        result = str(main.compute_neuron(inputs, weights))[:10]
        self.assertEqual(expect, result)

    def test_prediction_raise_error_on_malformed_weight_matrix(self):
        weights = get_test_weight_matrix()
        del weights[1][-1][-1]
        with self.assertRaises(AssertionError) as error: main.predict([2, 3, 4], weights)
        self.assertEqual(str(error.exception), "Weight matrix is malformed.")

    def test_prediction_raise_error_on_wrong_inputs_number(self):
        weights = get_test_weight_matrix()
        with self.assertRaises(AssertionError) as error: main.predict([2], weights)
        self.assertEqual(str(error.exception), "Inputs length conflict with weight matrix.")

    def test_prediction_output_vector_same_length_as_weight_matrix_describe(self):
        weights = get_test_weight_matrix()
        result = main.predict([0, 0], weights)
        self.assertEqual(len(weights), len(result))

    def test_learn_raise_error_on_malformed_weight_matrix(self):
        weights = get_test_weight_matrix()
        predictions = get_test_prediction_matrix()
        del weights[1][-1][-1]
        with self.assertRaises(AssertionError) as error: main.learn(weights, [0, 0], predictions)
        self.assertEqual(str(error.exception), "Weight matrix is malformed.")

    def test_learn_raise_error_on_wrong_prediction_length(self):
        weights = get_test_weight_matrix()
        predictions = get_test_prediction_matrix()
        del predictions[1][-1]
        with self.assertRaises(AssertionError) as error: main.learn(weights, [0, 0], predictions)
        self.assertEqual(str(error.exception), "Prediction matrix malformed.")

    def test_sigmoid_derivative(self):
        expect = "0.1966119"
        result = str(main.sigmoid_derivative(1))[:9]
        self.assertEqual(expect, result)

    def test_learn_return_same_dimension_matrix(self):
        weights = get_test_weight_matrix()
        predictions = get_test_prediction_matrix()
        result = main.learn(weights, [1], 1, predictions)
        self.assertEqual(len(weights), len(result))
        for layer in range(len(weights)):
            self.assertEqual(len(weights[layer]), len(result[layer]))
            for neuron in range(len(weights[layer])):
                self.assertEqual(len(weights[layer][neuron]), len(result[layer][neuron]))

    def test_learn_modify_weight_matrix_when_needed(self):
        weights = get_test_weight_matrix()
        predictions = get_test_prediction_matrix()
        main.learn(weights, [1], predictions)
        with self.assertRaises(AssertionError):
            numpy.testing.assert_array_equal(weights, get_test_weight_matrix())

    def test_learn_do_not_modify_weight_matrix_when_needed(self):
        weights = get_test_weight_matrix()
        predictions = get_test_prediction_matrix()
        expectations = predictions[-1]
        result = main.learn(weights, expectations, predictions)
        self.assertEqual(weights, result)
