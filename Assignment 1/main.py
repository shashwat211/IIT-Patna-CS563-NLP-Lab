from sklearn.model_selection import train_test_split
from utils import *
from viterbi import viterbi_model
from tabulate import tabulate
from tqdm import tqdm


def evaluate_accuracy_metrics(correct, total):
    accuracy = sum(x for x in correct.values()) / sum(x for x in total.values())
    print(f'\nHMM Model Accuracy = {accuracy}\n')

    classwise_accuracy = {}

    for tag in sorted(total.keys()):
        classwise_accuracy[tag] = correct[tag] / total[tag]
    
    print('Class-wise Accuracies \n')
    print(tabulate(zip(classwise_accuracy.keys(), classwise_accuracy.values()),
                   headers=['Class (Tag)', 'Accuracy'],
                   tablefmt='orgtbl'))

def test_and_evaluate(x, y, transition, emission, all_tags):
    correct_predictions = defaultdict(lambda: 0)
    tag_count = defaultdict(lambda: 0)

    print(f'Evaluating {len(x)} sentences.\n')

    for sentence, actual_tag_sequence in tqdm(zip(x, y), total=len(x)):
        pred_tag_sequence = viterbi_model(sentence, transition, emission, all_tags)
        for predicted, actual in zip(pred_tag_sequence, actual_tag_sequence):
            correct_predictions[actual] += predicted == actual
            tag_count[actual] += 1

    evaluate_accuracy_metrics(correct_predictions, tag_count)   

def main():
    data_x, data_y = load_dataset()
    x_train, x_test, y_train, y_test = train_test_split(data_x, data_y, test_size=0.2)

    # For all the tags
    print('-' * 80)
    print('HMM for 36 tags : ')
    all_tags = ['*'] + list(set(tag for tag_list in y_train for tag in tag_list)) + ['STOP']
    emission_matrix = generate_emission_matrix(x_train, y_train)
    transition_matrix = generate_transition_matrix(y_train)

    test_and_evaluate(x_test, y_test, transition_matrix, emission_matrix, all_tags)

    # Collapsing into 4 tags and repeating
    print('-' * 80)
    print('Number of tags reduced to 4. HMM for 4 tags :')
    y_train, y_test = collapse_to_4_tags(y_train, y_test)

    all_tags = ['*'] + list(set(tag for tag_list in y_train for tag in tag_list)) + ['STOP']
    emission_matrix = generate_emission_matrix(x_train, y_train)
    transition_matrix = generate_transition_matrix(y_train)

    test_and_evaluate(x_test, y_test, transition_matrix, emission_matrix, all_tags)
    print('-' * 80)

if __name__ == "__main__":
    main()
