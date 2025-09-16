import ROOT

def main():
    input_file = input()
    file_read_write(input_file)
    # file_writing(events_muons)

def file_read_write(file_name : str) -> None:
    histogram = ROOT.TH1F("histo", "MyFirstHisto", 30, 380, 620)
    with open(file_name, "r", encoding="utf-8") as data_file, open("masses.txt", "w", encoding="utf-8") as output_file:

        curr_event = []
        for lines in data_file:
            if lines.startswith("Run"):
                curr_event.append(lines.strip("\n"))
            elif lines.startswith("m1") or lines.startswith("m2"):
                begin_index = lines.find("=")
                end_index = lines.find("dptinv")
                extracted_data = lines[begin_index+1:end_index].split()
                curr_event.append(extracted_data)
                if lines.startswith("m2"):
                    tvector_one = ROOT.TLorentzVector()
                    tvector_two = ROOT.TLorentzVector()
                    tvector_one.SetPtEtaPhiM(float(curr_event[1][0]), float(curr_event[1][1]), float(curr_event[1][2]), float(curr_event[1][3]))
                    tvector_two.SetPtEtaPhiM(float(curr_event[2][0]), float(curr_event[2][1]), float(curr_event[2][2]), float(curr_event[2][3]))
                    invariant_mass = (tvector_one + tvector_two).M()
                    output_file.write(f"{curr_event[0]} : {invariant_mass}\n")
                    histogram.Fill(invariant_mass)
                    curr_event = []
    
    with ROOT.TFile.Open("histooutput.root", "RECREATE") as histo_file:
        histo_file.WriteObject(histogram, histogram.GetName())

if __name__ == "__main__":
    main() 