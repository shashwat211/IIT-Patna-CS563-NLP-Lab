from utils import *
from tqdm import tqdm
from viterbi import viterbi
from tabulate import tabulate
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score


def evaluate_metrics(true, pred):
    true = [ch for word in true for ch in word]
    pred = [ch for word in pred for ch in word]
    classes = list(set(true))
    classes.sort()
    # accuracy: (tp + tn) / (p + n)
    acc = accuracy_score(true, pred)
    # precision tp / (tp + fp)
    precision = precision_score(true, pred, average=None)
    # recall: tp / (tp + fn)
    recall = recall_score(true, pred, average=None)
    # f1: 2 tp / (2 tp + fp + fn)
    f1 = f1_score(true, pred, average=None)

    return acc, precision, recall, f1, classes

def print_metrics(test_acc, precision, recall, f1, classes):
    print(f"Accuracy of the model: {test_acc}")
    print(tabulate(zip(classes, precision, recall, f1),
                   headers=['Class', 'Precision', 'Recall', 'F1'],
                   tablefmt='orgtbl'))

def test_and_evaluate(test, true, transition, emission, all_tags, ngram=2, with_context=False):
    pred = []

    for sentence in tqdm(test, total=len(test)):
        pred.append(viterbi(sentence, transition, emission, all_tags, ngram, with_context))
    
    ngram_str = 'trigram' if ngram == 3 else 'bigram'
    context_str = 'with' if with_context else 'without'
    predictions_file = open(f"predictions_{ngram_str}_{context_str}_context.txt", "w")
    for test_sentence, pred_tag_seq in zip(test, pred):
        for word, tag in zip(test_sentence, pred_tag_seq):
            predictions_file.write(f'{word} {tag}\n')
        predictions_file.write('\n')

    accuracy, precision, recall, f1, classes = evaluate_metrics(true, pred)
    print_metrics(accuracy, precision, recall, f1, classes)             

def train_and_test(dataset, ngram=2, with_context=False):
    x_train, y_train, x_test, y_test = dataset

    # Train
    all_tags = ['*'] + list(set(tag for tag_list in y_train for tag in tag_list)) + ['STOP']
    emission_matrix = generate_emission_matrix(x_train, y_train, with_context=with_context)
    transition_matrix = generate_transition_matrix(y_train, ngram=ngram)

    # Test and Evaluate Metrics
    print('-' * 80)
    ngram_str = 'trigram' if ngram == 3 else 'bigram'
    context_str = 'with' if with_context else 'without'
    print(f'Evaluation on {ngram_str} model {context_str} context')

    test_and_evaluate(x_test, y_test, transition_matrix, emission_matrix, all_tags, ngram=ngram, with_context=with_context)
    
    print(f"\nEvaluated {len(x_test)} sentences.\n")


def main():
    data_train = load_sequences('./wnut16/dev.txt')
    data_train.extend(load_sequences('./wnut16/train.txt'))
    data_test = load_sequences('./wnut16/test.txt')

    x_train = [[tagged_token.token for tagged_token in sequence] for sequence in data_train]
    y_train = [[tagged_token.tag for tagged_token in sequence] for sequence in data_train]
    x_test = [[tagged_token.token for tagged_token in sequence] for sequence in data_test] 
    y_test = [[tagged_token.tag for tagged_token in sequence] for sequence in data_test]

    dataset = (x_train, y_train, x_test, y_test)

    train_and_test(dataset, ngram=2, with_context=False)
    train_and_test(dataset, ngram=3, with_context=False)
    train_and_test(dataset, ngram=2, with_context=True)
    train_and_test(dataset, ngram=3, with_context=True)
    

if __name__ == "__main__":
    main()
