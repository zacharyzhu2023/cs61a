"""Typing test implementation"""

from utils import *
from ucb import main, interact, trace
from datetime import datetime
#import string


###########
# Phase 1 #
###########


def choose(paragraphs, select, k):
    """Return the Kth paragraph from PARAGRAPHS for which SELECT called on the
    paragraph returns true. If there are fewer than K such paragraphs, return
    the empty string.
    """
    # BEGIN PROBLEM 1
    "*** YOUR CODE HERE ***"
    # END PROBLEM 1
    for paragraph in paragraphs:
        if k != 0:
            if select(paragraph):
                k -= 1
        else:
            if select(paragraph):
                return paragraph
    return ''


def about(topic):
    """Return a select function that returns whether a paragraph contains one
    of the words in TOPIC.

    >>> about_dogs = about(['dog', 'dogs', 'pup', 'puppy'])
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup!'], about_dogs, 0)
    'Cute Dog!'
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup.'], about_dogs, 1)
    'Nice pup.'
    """
    assert all([lower(x) == x for x in topic]), 'topics should be lowercase.'
    # BEGIN PROBLEM 2
    "*** YOUR CODE HERE ***"

    def select(paragraph):
        for punc in string.punctuation:
            paragraph = paragraph.replace(punc, '')
        paragraph = paragraph.lower().split(' ')
        for word in topic:
            for wrd in paragraph:
                if wrd == word:
                    return True
        return False
    return select
    # END PROBLEM 2


def accuracy(typed, reference):
    """Return the accuracy (percentage of words typed correctly) of TYPED
    when compared to the prefix of REFERENCE that was typed.

    >>> accuracy('Cute Dog!', 'Cute Dog.')
    50.0
    >>> accuracy('A Cute Dog!', 'Cute Dog.')
    0.0
    >>> accuracy('cute Dog.', 'Cute Dog.')
    50.0
    >>> accuracy('Cute Dog. I say!', 'Cute Dog.')
    50.0
    >>> accuracy('Cute', 'Cute Dog.')
    100.0
    >>> accuracy('', 'Cute Dog.')
    0.0
    """
    typed_words = split(typed)
    reference_words = split(reference)
    # BEGIN PROBLEM 3
    "*** YOUR CODE HERE ***"
    if len(typed_words) == 0 or len(reference_words) == 0:
        return 0.0
    total = 0
    for i in range(len(reference_words)):
        if i + 1 <= len(typed_words):
            if reference_words[i] == typed_words[i]:
                total += 1
    return total/len(typed_words)*100

    # END PROBLEM 3


def wpm(typed, elapsed):
    """Return the words-per-minute (WPM) of the TYPED string."""
    assert elapsed > 0, 'Elapsed time must be positive'
    # BEGIN PROBLEM 4
    "*** YOUR CODE HERE ***"
    return 60 * (len(typed)/5) / elapsed
    # END PROBLEM 4


def autocorrect(user_word, valid_words, diff_function, limit):
    """Returns the element of VALID_WORDS that has the smallest difference
    from USER_WORD. Instead returns USER_WORD if that difference is greater
    than LIMIT.
    """
    # BEGIN PROBLEM 5
    "*** YOUR CODE HERE ***"
    lowest_word = valid_words[0]
    lowest_difference = diff_function(user_word, lowest_word, limit)
    for word in valid_words:
        if word == user_word:
            return user_word
        elif diff_function(user_word, word, limit) < lowest_difference:
            lowest_difference = diff_function(user_word, word, limit)
            lowest_word = word
    if lowest_difference > limit:
        return user_word
    return lowest_word
    # END PROBLEM 5


def swap_diff(start, goal, limit):
    """A diff function for autocorrect that determines how many letters
    in START need to be substituted to create GOAL, then adds the difference in
    their lengths.
    """
    # BEGIN PROBLEM 6
    #assert False, 'Remove this line'
    if len(start) != 0 and len(goal) != 0:
        if limit < 0:
            return 0
        if start[0] == goal[0]:
            return swap_diff(start[1:], goal[1:], limit)
        else:
            return 1 + swap_diff(start[1:], goal[1:], limit-1)
    return abs(len(start) - len(goal))


    # END PROBLEM 6

def edit_diff(start, goal, limit):
    """A diff function that computes the edit distance from START to GOAL."""

    if start == goal:
        return 0

    if limit < 0: # Feel free to remove or add additional cases
        # BEGIN
        "*** YOUR CODE HERE ***"
        return 0
        # END
    elif len(start) == 0:
        return len(goal)

    elif len(goal) == 0:
        return len(start)

    elif start[0] == goal[0]: # Fill in the condition
        # BEGIN
        "*** YOUR CODE HERE ***"
        return edit_diff(start[1:], goal[1:], limit)
        # END

    else:
        #add_diff =  1 + edit_diff(goal[0] + start, goal,limit-1)
        add_diff =  1 + edit_diff(start, goal[1:],limit-1)
        remove_diff = 1 + edit_diff(start[1:], goal, limit-1)
        substitute_diff = 1 + edit_diff(start[1:], goal[1:],limit-1)
        # BEGIN
        "*** YOUR CODE HERE ***"
        return min(add_diff, remove_diff, substitute_diff)
        # END


def final_diff(start, goal, limit):
    """A diff function. If you implement this function, it will be used."""
    assert False, 'Remove this line to use your final_diff function'




###########
# Phase 3 #
###########


def report_progress(typed, prompt, id, send):
    """Send a report of your id and progress so far to the multiplayer server."""
    # BEGIN PROBLEM 8
    "*** YOUR CODE HERE ***"
    total_right, counter = 0, 0
    while counter < len(typed) and counter < len(prompt) and typed[counter] == prompt[counter]:
        total_right += 1
        counter += 1
    send({'id': id, 'progress': total_right/len(prompt)})
    return total_right/len(prompt)
    # END PROBLEM 8


def fastest_words_report(word_times):
    """Return a text description of the fastest words typed by each player."""
    fastest = fastest_words(word_times)
    report = ''
    for i in range(len(fastest)):
        words = ','.join(fastest[i])
        report += 'Player {} typed these fastest: {}\n'.format(i + 1, words)
    return report


def fastest_words(word_times, margin=1e-5):
    """A list of which words each player typed fastest."""
    n_players = len(word_times)
    n_words = len(word_times[0]) - 1
    assert all(len(times) == n_words + 1 for times in word_times)
    assert margin > 0
    # BEGIN PROBLEM 9
    "*** YOUR CODE HERE ***"
    # Get the actual time elapsed
    time_elapsed = []

    for i in range(len(word_times)):
        player_time = []
        for j in range(1, len(word_times[i])):
            second_length = float(elapsed_time(word_times[i][j]))
            first_length = float(elapsed_time(word_times[i][j-1]))
            player_time.append(second_length-first_length)
        time_elapsed.append(player_time)


        #time_elapsed.append(player_times)


    # Generate a list of the words
    word_list = []
    for wrd in word_times[0]:
        if str(word(wrd)) != 'START':
            word_list.append(str(word(wrd)))

    #print(word_list)
    '''
    Sample list that we're working with:
    [[0.2, 0.2, 0.4],[0.6,0.2,0.39]]
    '''

    '''
    p0 = [word_time('START', 0), word_time('What', 0.2), word_time('great', 0.4), word_time('luck', 0.8)]
    p1 = [word_time('START', 0), word_time('What', 0.6), word_time('great', 0.8), word_time('luck', 1.19)]
    fastest_words([p0, p1])
    '''


    # Find the list of 'fastest' times for each word

    '''
    Sample list that we're working with:
    [[0.2, 0.2, 0.4],[0.6,0.2,0.39]]

    Margin = 0
    '''
    word_fastest_positions = []
    for i in range(len(time_elapsed[0])):
        index_times = []
        for j in range(len(time_elapsed)):
            index_times.append(time_elapsed[j][i])
        min_time_index = min(index_times)
        fastest_index_list = []
        for k in range(len(index_times)):
            if index_times[k] - min_time_index <= margin:
                fastest_index_list.append(k)
        word_fastest_positions.append(fastest_index_list)

    '''
    Result of the previous piece of code:
    [[0,1],[2],[1,2],[1,2,3]]
    word1, word2, word3, word4
    '''
    # Find the actual words relative to players

    '''
    Newest result:
    [[0],[0,1][1]]
    '''

    #print(word_fastest_positions)

    # Make a list of lists for player's words to go into
    player_times = []
    for i in range(len(time_elapsed)):
        player_times.append([])

    # Append the words to the player's respective lists
    for i in range(len(word_fastest_positions)):
        for j in range(len(word_fastest_positions[i])):
            index = word_fastest_positions[i][j]
            player_times[index].append(word_list[i])
    return player_times








    # END PROBLEM 9


def word_time(word, elapsed_time):
    """A data abstrction for the elapsed time that a player finished a word."""
    return [word, elapsed_time]


def word(word_time):
    """An accessor function for the word of a word_time."""
    return word_time[0]


def elapsed_time(word_time):
    """An accessor function for the elapsed time of a word_time."""
    return word_time[1]


enable_multiplayer = False  # Change to True when you


##########################
# Command Line Interface #
##########################


def run_typing_test(topics):
    """Measure typing speed and accuracy on the command line."""
    paragraphs = lines_from_file('data/sample_paragraphs.txt')
    select = lambda p: True
    if topics:
        select = about(topics)
    i = 0
    while True:
        reference = choose(paragraphs, select, i)
        if not reference:
            print('No more paragraphs about', topics, 'are available.')
            return
        print('Type the following paragraph and then press enter/return.')
        print('If you only type part of it, you will be scored only on that part.\n')
        print(reference)
        print()

        start = datetime.now()
        typed = input()
        if not typed:
            print('Goodbye.')
            return
        print()

        elapsed = (datetime.now() - start).total_seconds()
        print("Nice work!")
        print('Words per minute:', wpm(typed, elapsed))
        print('Accuracy:        ', accuracy(typed, reference))

        print('\nPress enter/return for the next paragraph or type q to quit.')
        if input().strip() == 'q':
            return
        i += 1


@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions."""
    import argparse
    parser = argparse.ArgumentParser(description="Typing Test")
    parser.add_argument('topic', help="Topic word", nargs='*')
    parser.add_argument('-t', help="Run typing test", action='store_true')

    args = parser.parse_args()
    if args.t:
        run_typing_test(args.topic)
