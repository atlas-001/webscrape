import csv

def Redundant():
    '''an object for removing redundant words like conjunctions from the word list'''
    print('\nremoving redundant words\n')
    #import redundant words into a list
    where_redundant = '../tools/DataCleaning/redundant_words.csv' #at this pnt u shld b using main.py nd /scratch/
    with open(where_redundant,'r') as redundant_csv:
        redundant_list = csv.reader(redundant_csv) #open redundant words file
        scratch_word_file = open('scratch2.txt','r')
        scratch_word_list = scratch_word_file.read().splitlines()
        #print(type(scratch_word_list))
        for redundant_word in redundant_list:
            #redundant_word is now a list of the words
            #now lets open up the word file
            return redundant_word
        for scratch_word in scratch_word_list:
            return scratch_word
        if redundant_word == scratch_word:
            print(redundant_word)
        else:
            print(redundant_word)

def FinalCleaning():
    '''a function for cleaning up all of the scratch files once we are done with them'''
    print('cleaning up scratch files')
    pass
    

    
