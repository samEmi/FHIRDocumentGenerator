from GUI import GUI
from Model import Model


class DocumentGenerator:
    """
    Creates a popup window.

    Input a valid patient id and click generate patient record. This creates a word document in the same
    directory

    Click all patient graph and a graph that plots the frequency of the people that are married or not or speak
    english per age is plotted
    """
    def __init__(self, filePath="patientData"):
        self.model = Model(filePath)
        self.view = GUI(self.model)

c = DocumentGenerator()