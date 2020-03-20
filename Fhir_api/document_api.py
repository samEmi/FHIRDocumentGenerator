
from flask import Flask
from flask_restful import  Api, Resource, reqparse
from fhir_parser.fhir import FHIR
from math import floor
app = Flask(__name__)
api = Api(app)

fhir_parser = FHIR()
patients = fhir_parser.get_all_patients()

class FHIRInfo(Resource):
    def __init__(self):
        super(FHIRInfo, self).__init__()
        self.reqParser = reqparse.RequestParser()
        self.reqParser.add_argument("id", type=str)
        self.reqParser.add_argument("graph", type=str)

    def get(self):
        arguments = self.reqParser.parse_args()
        if arguments["graph"]:
            return self.getAgeToObservations()
        return self.getPatientResult(arguments)

    def getAgeToObservations(self):
        result = {"Never Married": dict(), "Married": dict(), "English": dict()}
        for patient in patients:
            status = str(patient.marital_status)
            age = floor(patient.age())
            languages = patient.communications.languages
            for language in languages:
                if language in result:
                    self.addToAgeFreq(result, language, age)
            self.addToAgeFreq(result, status, age)
        return result

    def addToAgeFreq(self, result, category, age):
        ageFrequencyDict = result[category]
        if age in ageFrequencyDict:
            ageFrequencyDict[age] += 1
        else:
            ageFrequencyDict[age] = 1


    def getPatientResult(self, arguments):
        patient = fhir_parser.get_patient(arguments["id"])
        observations = fhir_parser.get_patient_observations(arguments["id"])
        observations = self.assessObservations(observations)
        result = {"full_name": patient.name.full_name, "age": patient.age(), "gender": patient.gender,
                  "observations": observations}
        return result
    def assessObservations(self, observations):
        all_observations = []
        for observation in observations:
            an_observation = self.makeObservation(observation)
            all_observations.append(an_observation)
        return all_observations

    def makeObservation(self, observation):
        an_observation = {}
        an_observation["type"] = observation.type
        an_observation["status"] = observation.status
        an_observation["date"] = str(observation.effective_datetime)
        an_observation["components"] = ', '.join(map(str, observation.components))
        return an_observation

api.add_resource(FHIRInfo, "/api/patients", endpoint="document")

if __name__== "__main__":
    app.run(debug=True, port=5002)