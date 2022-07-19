# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from similarityIndexer import SimilarityIndexer




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    vector1 = [1, 2, 3]
    vector2 = [1, 5, 7]
    vector3 = [100, 250, 300]
    SI = SimilarityIndexer(vector1, vector2)
    SI.calculate_euclidean_distance()
    SI.calculate_cosine_similarity()
    SI.calculate_TSSS_similarity()
    print("cosine similarity: ", SI.get_similarity("cosine"))
    print("TSSS similarity: ", SI.get_similarity("TSSS"))
    print("Euclidean Distance: ", SI.get_similarity("euclidean"))

    SI2 = SimilarityIndexer(vector1, vector3)
    SI2.calculate_cosine_similarity()
    SI2.calculate_TSSS_similarity()
    print("cosine similarity 2: ", SI2.get_similarity("cosine"))
    print("TSSS similarity 2: ", SI2.get_similarity("TSSS"))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
