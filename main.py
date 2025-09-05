"""
formulas

muon : pt = sqrt (px^2 + py^2)
       phi = angle in xy plane
       eta = pseudorapidity
       mass = mass of muon

E (energy) = sqrt (mass ^ 2 + momentum ^ 2)

momentum + energy = lorentz vector

invariant mass = 



todo:
read input file - done
read events in each file - done
find momentum , px, py, pz - in progress
calculate 4 vector for each muon -
calculate the invariant mass of the hyp particle -
writes mass to another file -

format:

line 1 : event
line 2 : ignore
line 3 : info for muon 1
line 4 : info for muon 2


questions:

1. Big M stands for momentum or mass?
2. invariant mass formula?
3. limitations/format that you would want the program to be made
"""
from EventClass import Event
def main():
    file_input = input()

    

def file_sorting(file_name : str) -> list:
    event_objs = []
    with open(file_name, 'r', encoding="utf-8") as data_file:
        new_event = None
        for lines in data_file:
            if lines.startswith("Run"):
                new_event = Event(lines.strip("\n"))
            elif lines.startswith("m1"):
                new_event.muon_one_setter(lines)
            elif lines.startswith("m2"):
                new_event.muon_two_setter(lines)
                event_objs.append(new_event)
    return event_objs
            

if __name__ == "__main__":
    main()