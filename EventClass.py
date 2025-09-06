class Event:
    """Event holds the event info, while also holding two different Muon objects"""
    def __init__(self, event:str):
        self.event = event
        self.muon_one = None
        self.muon_two = None
        self.i_mass = None

    def muon_one_setter(self, m1) -> None:
        """sets up the first muon encountered"""
        self.muon_one = m1

    def muon_two_setter(self, m2) -> None:
        """sets up the second muon encountered"""
        self.muon_two = m2

    def i_mass_calc(self) -> None:
        """calculates the invariant mass"""
        self.i_mass = (self.muon_one.mass_getter() ** 2) + (self.muon_two.mass_getter() ** 2) + 2 * ((self.muon_one.energy_getter() * self.muon_two.energy_getter()) - (self.muon_one.momentum_getter() * self.muon_two.momentum_getter()))    
    
    def i_mass_getter(self) -> float:
        """returns the invariant mass"""
        return self.i_mass