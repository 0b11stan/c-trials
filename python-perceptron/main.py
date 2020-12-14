import numpy
import matplotlib.pyplot as plt
import samples_carre as sc


def build_weight_matrix(network_description):
    weights = [numpy.random.uniform(-0.25, 0.25, (
        network_description[layer_index],
        network_description[layer_index - 1]
    )) for layer_index in range(1, len(network_description))]
    weights.insert(0, [[None], [None]])
    return weights


def initiate_delta_matrix(weights, value=0):
    return [numpy.random.uniform(value, value, len(layer)) for layer in weights]


def compute_neuron(inputs, weights):
    return 1 / (1 + numpy.exp(- numpy.dot(inputs, weights)))


def sigmoid_derivative(x):
    return numpy.exp(-x) / ((1 + numpy.exp(-x)) ** 2)


def predict(inputs, weights):
    if len(inputs) != len(weights[0]):
        raise AssertionError("Inputs length conflict with weight matrix.")

    predictions = [inputs]
    for layer_index in range(1, len(weights)):
        predictions.append([])
        for neuron_index in range(len(weights[layer_index])):
            predictions[-1].append(
                compute_neuron(
                    inputs, weights[layer_index][neuron_index]
                )
            )
        inputs = predictions[-1]

    return predictions


def update_weights(weights, deltas, predictions, learning_rate=0.01):
    for layer_index in range(1, len(weights)):
        for neuron_index in range(len(weights[layer_index])):
            for weight_index in range(len(weights[layer_index][neuron_index])):
                weight_input = predictions[layer_index - 1][weight_index]
                delta = deltas[layer_index][neuron_index]
                weights[layer_index][neuron_index][weight_index] += learning_rate * delta * weight_input


def learn(weights, inputs, expectation, predictions):
    network_error = expectation - predictions[-1][0]
    deltas = initiate_delta_matrix(weights)

    deltas[-1] = [network_error * sigmoid_derivative(predictions[-1][0])]

    for layer_index in range(len(weights) - 1, 1, -1):
        for neuron_index in range(len(weights[layer_index - 1])):
            responsibility = sum([
                weights[layer_index][k][neuron_index] * deltas[layer_index][k]
                for k in range(len(weights[layer_index]))
            ])
            deltas[layer_index - 1][neuron_index] = sigmoid_derivative(sum(inputs)) * responsibility

    update_weights(weights, deltas, predictions)

    return weights


def displayForm(liste_sample_in, liste_sample_out):
    print('    Display')
    x, y = [], []
    for i in range(len(liste_sample_in)):
        x.append(liste_sample_in[i][0][0])
        y.append(liste_sample_in[i][0][1])
        plt.plot(x, y, 'bx')

    x, y = [], []

    for i in range(len(liste_sample_out)):
        x.append(liste_sample_out[i][0][0])
        y.append(liste_sample_out[i][0][1])
        plt.plot(x, y, 'rx')

    plt.axis([-6, 6, -6, 6])
    plt.grid()
    plt.show()


def display_error(errors):
    plt.plot([x for x in range(len(errors))], errors)
    plt.show()


# def train(weights, dataset, epoch):
#     errors = []
#     for x in range(epoch):
#         example = numpy.random.choice(dataset, 1)[0]
#         predictions = predict(example["pattern"], weights)
#         errors.append(example["expect"][0] - predictions[-1][0])
#         print("EXPECTATION : {} ; PREDICTION : {} ; ERROR : {}".format(
#             example["expect"][0],
#             predictions[-1][0],
#             errors[-1])
#         )
#         learn(weights, example["pattern"], example["expect"][0], predictions)
# display_error(errors)

def generate_square_samples(number):
    samples = numpy.zeros(2 * number, dtype=[('input', float, 2), ('output', float, 1)])
    square = sc.samples(number)
    square.create_samples()
    for i in range(square.nb_samples):
        samples[i] = square.samples[i]
    return samples


def train_carre():
    print("Learning the carre")
    samples = generate_square_samples(1000)

    # Etape 1 : Déclarer un réseau MLP avec une stucture répondant à la tache demandé
    weights = build_weight_matrix([2, 10, 10, 1])

    # Etape 2 : réalisé l'apprentissage
    errors = []
    epoch = 100
    for x in range(epoch):
        epoch_errors = []
        for sample in samples:
            inputs = sample[0]
            expect = sample[1]
            predictions = predict(inputs, weights)
            learn(weights, inputs, expect, predictions)
            epoch_errors.append(((expect - predictions[-1][0]) ** 2).sum())
        error = numpy.mean(epoch_errors)
        errors.append(error)
        print("layer n°{} error : {}".format(x, error))
    display_error(errors)

    # Etape 3 : Réalisé la phase de test
    samples = generate_square_samples(10)
    for sample in samples:
        inputs = sample[0]
        expect = sample[1]
        predictions = predict(inputs, weights)
        print("INPUT : {} ; EXPECT : {} ; PREDICT : {}".format(inputs, expect, predictions[-1][0]))


def main():
    train_carre()


# weights = build_weight_matrix([2, 10, 1])
# dataset = [
#     {"pattern": [1, 1], "expect": [1]},
#     {"pattern": [0, 1], "expect": [1]},
#     {"pattern": [1, 0], "expect": [1]},
#     {"pattern": [0, 0], "expect": [0]},
# ]
# train(weights, dataset, 10000)
# print(weights)


if __name__ == '__main__':
    main()
