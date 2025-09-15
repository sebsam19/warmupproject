import ROOT

def main():
    file_open = ROOT.TFile.Open("muons.root")
    tree = file_open.Get("tnt")

    histogram = ROOT.TH1F("eventhisto", "MySecondHisto", 30, 0, 700)

    for events in tree:
        print(events.pt1)

if __name__ == "__main__":
    main()