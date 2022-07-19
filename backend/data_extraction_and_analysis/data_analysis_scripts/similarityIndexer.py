import math

import numpy as np

# Class which can calculate similarity between two inputted vectors in a variety of ways. USE THE GET_SIMILARITY
# FUNCTION USING KEYWORDS TO GET SIMILARITIES.
class SimilarityIndexer(object):

    def __init__(self, vector1, vector2):
        self.v1 = np.array(vector1)
        self.v2 = np.array(vector2)

        if self.v1.size is not self.v2.size:
            print("size of inputted vectors is not the same")

        # similarity values (for each new one need to add a calculate and a else if in get_similarity)
        self.cosine_similarity = None
        self.percentage_similarity = None
        self.TS = None
        self.SS = None
        self.TSSS_similarity = None
        self.euclidean_distance = None
        self.magnitude_difference = None

    # Calculate the cosine similarity
    def calculate_euclidean_distance(self):
        vec1 = self.v1.copy()
        vec2 = self.v2.copy()
        self.euclidean_distance = np.linalg.norm(vec1 - vec2)

    # Calculate magnitude difference
    def calculate_magnitude_difference(self):
        self.magnitude_difference = abs((np.linalg.norm(self.v1) - np.linalg.norm(self.v2)))

    # calculate sector area score
    def calculate_SS(self):
        euclidean = self.euclidean_distance
        mag_diff = self.magnitude_difference
        theta = self.get_theta()
        self.SS = math.pi * (euclidean + mag_diff)**2 * theta/360

    # calculate TSSS similarity score.
    def calculate_TSSS_similarity(self):
        self.calculate_cosine_similarity()
        theta = self.get_theta()
        self.TS = (np.linalg.norm(self.v1) * np.linalg.norm(self.v2) * np.sin(theta))/2

        self.calculate_euclidean_distance()
        self.calculate_magnitude_difference()
        self.calculate_SS()
        self.TSSS_similarity = self.TS * self.SS

    # get value of theta using cosine similarity
    def get_theta(self):
        return np.arccos(self.cosine_similarity) + np.radians(10)

    # calculate simple percent similarity
    def calculate_percent_similar(self):
        vec1 = np.array(self.v1)
        vec2 = np.array(self.v2)
        self.percentage_similarity = np.mean(vec1 == vec2)

    # calculate cosine similarity
    def calculate_cosine_similarity(self):
        self.cosine_similarity = np.dot(self.v1, self.v2)/(np.linalg.norm(self.v1) * np.linalg.norm(self.v2))

    # get every type of similarity using keywords.
    def get_similarity(self, sim_type):
        if sim_type == "cosine":
            if self.cosine_similarity is None:
                self.calculate_cosine_similarity()
                return self.cosine_similarity
            else:
                return self.cosine_similarity

        elif sim_type == "percent similarity":
            if self.percentage_similarity is None:
                self.calculate_percent_similar()
                return self.percentage_similarity
            else:
                return self.percentage_similarity

        elif sim_type == "euclidean":
            if self.euclidean_distance is None:
                self.calculate_euclidean_distance()
                return self.euclidean_distance
            else:
                return self.euclidean_distance

        elif sim_type == "TSSS":
            if self.TSSS_similarity is None:
                self.calculate_TSSS_similarity()
                return self.TSSS_similarity
            else:
                return self.TSSS_similarity

        else:
            return "not a valid similarity type..."