import string

from sys import argv 

#get our data file name from the command line (*args)

def main(file_name): 
    # script, file_name = argv             

    with open(file_name) as poem_file: 
    
        word_count = {}
    
        nonwords = string.punctuation + string.digits
        # print 1, string.punctuation

        for line in poem_file:


# this removes newline character and the possesive "'s"
            aline = line.rstrip().replace("'s", "").lower()
            
            for ch in nonwords:
                # if ch in aline:
                aline = aline.replace(ch, " ")
            
            aline = aline.split()
            
            total_word_count = 0

            for word in aline:
                # if word not in word_count:
                #     word_count[word] = 1
                # else:
                #     word_count[word] = word_count[word] + 1
                word_count[word] = word_count.get(word, 0 ) + 1
                total_word_count = total_word_count + word_count[word]
        word_count_doc(word_count)

    print "The total words counted was %d." % total_word_count

def word_count_doc(word_count):
    with open("word_count.txt", "w") as out_file:             
        for key in sorted(word_count):
            out_file.write("%s: %d\n" % (key, word_count[key]))


if __name__ == '__main__':
    main(argv[1])