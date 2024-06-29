import math

# Öklid mesafesi fonksiyonu
def euclideanDistance(p1, p2):
    return math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)

# Noktaların tanımlanması
points = [(1, 2), (3, 4), (5, 6), (7, 8)]

# Mesafelerin hesaplanması ve minimum mesafenin bulunması
distances = [euclideanDistance(points[i], points[j]) for i in range(len(points)) for j in range(i + 1, len(points))]
min_distance = min(distances)

# Sonucun yazdırılması
print(f"Minimum Öklid mesafesi: {min_distance}")
