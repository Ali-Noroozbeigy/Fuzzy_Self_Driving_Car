class FuzzyGasController:
    """
    # emtiazi todo
    write all the fuzzify,inference,defuzzify method in this class
    """

    def __init__(self):
        self.inference_results = None
        

    def decide(self, center_dist):
        """
        main method for doin all the phases and returning the final answer for gas
        """
        # phase 1: fuzzification
        f_memship = self.membership_degree_front(center_dist)

        # phase 2: inference
        self.inference(f_memship)

        # phase 3: defuzzification
        center_of_gravity = self.centroid()

        return center_of_gravity

    def membership_degree_front(self, front_distance):
        return {
            'close': self.close(front_distance),
            'moderate': self.moderate(front_distance),
            'far': self.far(front_distance)
        }

    def close(self, x):
        if 0 <= x <= 50:
            return (-1/50) * x + 1
        return 0

    def moderate(self, x):
        if 40 <= x <= 50:
            return (1/10) * x - 4
        if 50 < x <= 100:
            return (-1/50) * x + 2
        return 0

    def far(self, x):
        if 90 <= x <= 200:
            return (1/110) * x - (9/11)
        if x > 200:
            return 1
        return 0

    def inference(self, f_memship):
        self.inference_results = {
            'low': f_memship['close'],
            'medium': f_memship['moderate'],
            'high': f_memship['far']
        }

    def max_gas(self, x):
        return max(
            min(self.low(x), self.inference_results['low']),
            min(self.medium(x), self.inference_results['medium']),
            min(self.high(x), self.inference_results['high'])
        )

    def low(self, x):
        if 0 <= x <= 5:
            return (1/5) * x
        if 5 < x <= 10:
            return (-1/5) * x + 2
        return 0

    def medium(self, x):
        if 0 <= x <=15:
            return (1/15) * x
        if 15 < x <= 30:
            return (-1/15) * x + 2
        return 0

    def high(self, x):
        if 25 <= x <= 30:
            return (1/5) * x - 5
        if 30 < x <= 90:
            return (-1/60) * x + 1.5
        return 0

    def centroid(self):
        numerator = 0.0
        denominator = 0.0

        step = 90 / 999
        x = [0 + i * step for i in range(1000)]
        delta = x[1] - x[0]
        for i in x:
            u = self.max_gas(i)
            numerator += u * i * delta
            denominator += u * delta

        center = 0.0
        if denominator != 0:
            center = 1.0 * float(numerator) / float(denominator)
        return center
