from __future__ import division
from __future__ import print_function

import sys
import argparse
import cv2
import editdistance
from DataLoader import DataLoader, Batch
from Model import Model, DecoderType
from SamplePreprocessor import preprocess
import logging
import tensorflow as tf
tf.get_logger().setLevel(logging.ERROR)
from turtle import *
import random
import pandas as pd
import draw
import socket
import struct



class FilePaths:
    "filenames and paths to data"
    fnCharList = '../model/charList.txt'
    fnAccuracy = '../model/accuracy.txt'
    fnTrain = '../data/'
    fnInfer = '../data/text_image.png'
    fnCorpus = '../data/corpus.txt'



def train(model, loader):
    "train NN"
    epoch = 0 # number of training epochs since start
    bestCharErrorRate = float('inf') # best valdiation character error rate
    noImprovementSince = 0 # number of epochs no improvement of character error rate occured
    earlyStopping = 5 # stop training after this number of epochs without improvement
    while True:
        epoch += 1
        print('Epoch:', epoch)

        # train
        print('Train NN')
        loader.trainSet()
        while loader.hasNext():
            iterInfo = loader.getIteratorInfo()
            batch = loader.getNext()
            loss = model.trainBatch(batch)
            print('Batch:', iterInfo[0],'/', iterInfo[1], 'Loss:', loss)

        # validate
        charErrorRate = validate(model, loader)

        # if best validation accuracy so far, save model parameters
        if charErrorRate < bestCharErrorRate:
            print('Character error rate improved, save model')
            bestCharErrorRate = charErrorRate
            noImprovementSince = 0
            model.save()
            open(FilePaths.fnAccuracy, 'w').write('Validation character error rate of saved model: %f%%' % (charErrorRate*100.0))
        else:
            print('Character error rate not improved')
            noImprovementSince += 1

        # stop training if no more improvement in the last x epochs
        if noImprovementSince >= earlyStopping:
            print('No more improvement since %d epochs. Training stopped.' % earlyStopping)
            break

word=''
probablity=0

def validate(model, loader):
    "validate NN"
    print('Validate NN')
    loader.validationSet()
    numCharErr = 0
    numCharTotal = 0
    numWordOK = 0
    numWordTotal = 0
    while loader.hasNext():
        iterInfo = loader.getIteratorInfo()
        print('Batch:', iterInfo[0],'/', iterInfo[1])
        batch = loader.getNext()
        (recognized, _) = model.inferBatch(batch)
        
        print('Ground truth -> Recognized')	
        for i in range(len(recognized)):
            numWordOK += 1 if batch.gtTexts[i] == recognized[i] else 0
            numWordTotal += 1
            dist = editdistance.eval(recognized[i], batch.gtTexts[i])
            numCharErr += dist
            numCharTotal += len(batch.gtTexts[i])
            print('[OK]' if dist==0 else '[ERR:%d]' % dist,'"' + batch.gtTexts[i] + '"', '->', '"' + recognized[i] + '"')
    
    # print validation result
    charErrorRate = numCharErr / numCharTotal
    wordAccuracy = numWordOK / numWordTotal
    #print('Character error rate: %f%%. Word accuracy: %f%%.' % (charErrorRate*100.0, wordAccuracy*100.0))
    return charErrorRate


def infer(model, fnImg):
    "recognize text in image provided by file path"
    img = preprocess(cv2.imread(fnImg, cv2.IMREAD_GRAYSCALE), Model.imgSize)
    batch = Batch(None, [img])
    model_infer = model.inferBatch(batch, True)
    if len(model_infer) == 3:
        (recognized, probability, _) = model_infer
    else:
        (recognized, probability) = model_infer
    print('Recognized:', '"' + recognized[0] + '"')
    print('Probability:', probability[0])
#<<<<<<< HEAD
    return (recognized[0],probability[0])
#=======
    
    #return recognized, probability
#>>>>>>> dd4c864796fc22fde4e234ed174af7acbc414cb4

def is_loopback(host):
    """
    Checks the server the user is working from
    """
    loopback_checker = {
        socket.AF_INET: lambda x: struct.unpack('!I', socket.inet_aton(x))[0] >> (32-8) == 127,
        socket.AF_INET6: lambda x: x == '::1'
    }
    for family in (socket.AF_INET, socket.AF_INET6):
        try:
            r = socket.getaddrinfo(host, None, family, socket.SOCK_STREAM)
        except socket.gaierror:
            return False
        for family, _, _, _, sockaddr in r:
            if not loopback_checker[family](sockaddr[0]):
                return False
    return True


def main():
    "main function"
    # optional command line args

    parser = argparse.ArgumentParser()
    parser.add_argument('--train', help='train the NN', action='store_true')
    parser.add_argument('--validate', help='validate the NN', action='store_true')
    parser.add_argument('--beamsearch', help='use beam search instead of best path decoding', action='store_true')
    parser.add_argument('--wordbeamsearch', help='use word beam search instead of best path decoding', action='store_true')
    parser.add_argument('--dump', help='dump output of NN to CSV file(s)', action='store_true')

    args = parser.parse_args()

    decoderType = DecoderType.BestPath
    if args.beamsearch:
        decoderType = DecoderType.BeamSearch
    elif args.wordbeamsearch:
        decoderType = DecoderType.WordBeamSearch

    # train or validate on IAM dataset	
    if args.train or args.validate:
        # load training data, create TF model
        loader = DataLoader(FilePaths.fnTrain, Model.batchSize, Model.imgSize, Model.maxTextLen)

        # save characters of model for inference mode
        open(FilePaths.fnCharList, 'w').write(str().join(loader.charList))
        
        # save words contained in dataset into file
        open(FilePaths.fnCorpus, 'w').write(str(' ').join(loader.trainWords + loader.validationWords))

        # execute training or validation
        if args.train:

            model = Model(loader.charList, decoderType)
            train(model, loader)
        elif args.validate:
            model = Model(loader.charList, decoderType, mustRestore=True)
            validate(model, loader)

    # infer text on test image
    else:
        #print(open(FilePaths.fnAccuracy).read())
        tf.compat.v1.reset_default_graph()
        model = Model(open(FilePaths.fnCharList).read(), decoderType, mustRestore=True, dump=args.dump)
#<<<<<<< HEAD
        
        word, probablity=infer(model, FilePaths.fnInfer)
        
        letter_color_map = {'a': 'red', 'b': 'blue', 'c': 'yellow', 
                'd': 'blue', 'e': 'green', 'f': 'green', 
                'g': 'green', 'h': 'orange', 'i': 'yellow', 
                'j': 'orange', 'k': 'orange', 'l': 'yellow', 
                'm': 'red', 'n': 'orange', 'o': 'white', 
                'p': 'purple', 'q': 'purple', 'r': 'red', 
                's': 'yellow', 't': 'blue', 'u': 'orange', 
                'v': 'purple', 'w': 'blue', 'x': 'black', 
                'y': 'yellow', 'z': 'black',
                '0': 'white', '1': 'maroon', '2': 'goldenrod',
                '4': 'firebrick', '5': 'darkblue', '6': 'papayawhip',
                '7': 'midnightblue', '8': 'darkred', '9': 'yellow'}
        word= word.lower()
        letters= list(word)
        colors=list((pd.Series(letters)).map(letter_color_map))
        print(colors)
        if is_loopback('localhost'):
            draw.draw_turtle_localhost(colors)
        else:
            draw.draw_turtle_datahub(colors)
        
    
    
#=======
       # infer(model, FilePaths.fnInfer)
      #  print('done')
    #    return infer
#>>>>>>> dd4c864796fc22fde4e234ed174af7acbc414cb4


if __name__ == '__main__':
    main()
    
    

