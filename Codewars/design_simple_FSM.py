"""
Create a finite automaton that has three states. Finite automatons are the same as finite state machines for our purposes.

Our simple automaton, accepts the language of A, defined as {0, 1} and should have three states: q1, q2, and q3. Here is the description of the states:

q1 is our start state, we begin reading commands from here
q2 is our accept state, we return true if this is our last state
And the transitions:

q1 moves to q2 when given a 1, and stays at q1 when given a 0
q2 moves to q3 when given a 0, and stays at q2 when given a 1
q3 moves to q2 when given a 0 or 1
The automaton should return whether we end in our accepted state (q2), or not (true/false).
"""


class Automation(object):

    def __init__(self) -> None:
        self.cur = "q1"

    def _q1_transit(self, input):
        if input == "1":
            self.cur = "q2"
        return
    
    def _q2_transit(self, input):
        if input == "0":
            self.cur = "q3"
        return

    def _q3_transit(self):
        self.cur = "q2"
        return
    

    def read_commands(self, commands):
        # Return true if we end in our accept state, False otherwise
        for cmd in commands:
            if self.cur == "q1":
                self._q1_transit(cmd)
            elif self.cur == "q2":
                self._q2_transit(cmd)
            else:
                self._q3_transit()
        return self.cur == "q2"

