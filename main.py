import math

def main():
    input_file = input()
    events_muons = file_reading(input_file)
    file_writing(events_muons)

def file_read_write(file_name : str) -> None:
    with open(file_name, "r", encoding="utf-8") as data_file, open("masses.txt", "w", encoding="utf-8") as output_file:
        curr_event = []
        for lines in data_file:
            if lines.startswith("Run"):
                curr_event.append(lines.strip("\n"))
            elif lines.startswith("m1") or lines.startswith("m2"):
                begin_index = lines.find("=")
                end_index = lines.find("dptinv")
                extracted_data = lines[begin_index+1:end_index].split()
                if lines.startswith("m1"):
                    curr_event.append(extracted_data)
                else:
                    curr_event.append(extracted_data)

                    
def file_reading(file_name: str) -> list:
    stored_events = []
    with open(file_name, "r", encoding="utf-8") as data_file:
        event_muons = []
        for lines in data_file:
            if lines.startswith("Run"):
                event_muons.append(lines.strip("\n"))
            elif lines.startswith("m1") or lines.startswith("m2"):
                begin_index = lines.find("=")
                end_index = lines.find("dptinv")
                extracted_data = lines[begin_index+1:end_index].split()
                if lines.startswith("m1"):
                    event_muons.append(extracted_data)
                else:
                    event_muons.append(extracted_data)
                    stored_events.append(event_muons)
                    event_muons = []
    return stored_events

def file_writing(event_muons : list) -> None:
    with open("masses.txt", "w", encoding="utf-8") as output_file:
        for events in event_muons:
            momentum_one = momentum_calc(events[1])
            momentum_two = momentum_calc(events[2])
            energy_one = energy_calc(momentum_one, float(events[1][3]))
            energy_two = energy_calc(momentum_two, float(events[2][3]))
            f_vector_one = four_vector_calc(momentum_one, energy_one)
            f_vector_two = four_vector_calc(momentum_two, energy_two)
            invariant_mass = invariant_mass_calc(momentum_one, momentum_two, energy_one, energy_two)
            output_file.write(f"{events[0]} : {invariant_mass}\n")


def momentum_calc(event_data) -> tuple:
    px = float(event_data[0]) * math.cos(float(event_data[2]))
    py = float(event_data[0]) * math.sin(float(event_data[2]))
    pz = float(event_data[0]) * math.sinh(float(event_data[1]))
    return (px, py, pz)

def energy_calc(momentum : tuple, mass : float) -> float:
    momentum_squared = (momentum[0] ** 2) + (momentum[1] ** 2) + (momentum[2] ** 2)
    mass_square = mass * mass
    return math.sqrt(momentum_squared + mass_square)
 
def four_vector_calc(momentum : tuple, energy : float) -> tuple:
    return (energy, momentum[0], momentum[1], momentum[2])

def invariant_mass_calc(m1 : tuple, m2 : tuple, e1 : float, e2 : float) -> float:
    energies = (e1 + e2) ** 2
    combined_m1 = (m1[0] + m2[0]) ** 2
    combined_m2 = (m1[1] + m2[1]) ** 2
    combined_m3 = (m1[2] + m2[2]) ** 2
    total_m = combined_m1 + combined_m2 + combined_m3
    return math.sqrt(energies - total_m)


if __name__ == "__main__":
    main() 