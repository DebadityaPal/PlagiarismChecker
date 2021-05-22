import mxnet as mx
from mxnet import nd, gluon
import numpy as np
from autocorrect import Speller
import cv2

ctx = mx.cpu()
alphabet_encoding = (
    r' !"#&\'()*+,-./0123456789:;?ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
)
alphabet_dict = {alphabet_encoding[i]: i for i in range(len(alphabet_encoding))}
max_seq_len = 160


def transform(image, label):
    """
    This function resizes the input image and converts so that it could be fed into the network.
    Furthermore, the label (text) is one-hot encoded.
    """
    image = np.expand_dims(image, axis=0).astype(np.float32)
    if image[0, 0, 0] > 1:
        image = image / 255.0
    image = (image - 0.942532484060557) / 0.15926149044640417
    label_encoded = np.zeros(max_seq_len, dtype=np.float32) - 1
    i = 0
    for word in label:
        word = word.replace("&quot", r'"')
        word = word.replace("&amp", r"&")
        word = word.replace('";', '"')
        for letter in word:
            label_encoded[i] = alphabet_dict[letter]
            i += 1
    return image, label_encoded


def decode(prediction):
    """
    Returns the string given one-hot encoded vectors.
    """
    spell = Speller(lang="en")
    results = []
    for word in prediction:
        result = []
        for i, index in enumerate(word):
            if (
                i < len(word) - 1 and word[i] == word[i + 1] and word[-1] != -1
            ):  # Hack to decode label as well
                continue
            if index == len(alphabet_dict) or index == -1:
                continue
            else:
                result.append(spell(alphabet_encoding[int(index)]))
        results.append(result)
    words = ["".join(word) for word in results]
    return words


def predict(lines):

    net = gluon.nn.SymbolBlock.imports(
        symbol_file="../models/iam-ocr-symbol.json",
        input_names=["data"],
        param_file="../models/iam-ocr-0000.params",
        ctx=ctx,
    )

    predictions = []

    for line in lines:
        line = cv2.resize(line, (800, 60))
        line, _ = transform(line, "check")
        line = nd.array(line)
        line = line.as_in_context(ctx)
        line = line.expand_dims(axis=0)
        output = net(line)
        output = output.softmax().topk(axis=2).asnumpy()
        decoded_output = (
            decode(output)[0]
            .replace("&quot", '"')
            .replace("&amp", "&")
            .replace('";', '"')
        )
        predictions.append(decoded_output)

    return " ".join(predictions)
