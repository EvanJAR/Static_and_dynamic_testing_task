Testing task 1:
Carry out static testing on the code below.
Comment on any errors that you see below.
Note that we are only looking for errors here.

Not any issues with, i.e.: Thinking that methods should be renamed or should be class level, or using string interpolation etc.

These aren't errors but rather standards that vary from developer to developer.

Only comment on errors that would stop the tests running.

```python

class CardGame:


  def check_for_ace(self, card):
    # line 19 implements the wrong operator to compare values, it should be: if card.value == 1: 
    if card.value = 1:
      return True
    # the else is missing a colon
    else
      return False
   
# should be "def" to define a function
# the arguments being passed into the function should be seperated by commas
  dif highest_card(self, card1 card2):
  #indentation is required for both the if and the else statements below
  if card1.value > card2.value:
    # this should be returning "card1" instead of "card"
    return card
  else:
    return card2
  

# the whole function needs to be indented to be in line with the other two functions
def cards_total(self, cards):
  # total has not been defined, needs to be "total = 0"
  total
  for card in cards:
    total += card.value
    # there should be a space after the word 'of' and the final  quotation mark.
    # total should be converted from an int into a string 
    # the code should therefore be: "You have a total of " + str(total)
    return "You have a total of" + total
  