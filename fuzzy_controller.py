class FuzzyController:
    """
    #todo
    write all the fuzzify,inference,defuzzify method in this class
    """

    def __init__(self):
        self.inference_results = None

    def decide(self, left_dist,right_dist):
        """
        main method for doin all the phases and returning the final answer for rotation
        """
        # phase 1: fuzzification
        l_memship = self.membership_degree_left(left_dist)
        r_memship = self.membership_degree_right(right_dist)

        # phase 2: inference
        self.inference(l_memship, r_memship)

        # phase 3: defuzzification
        center_of_gravity = self.centroid()

        return center_of_gravity

    def membership_degree_left(self, left_dist):
        return {'close_L': self.close_L(left_dist),
                'moderate_L': self.moderate_L(left_dist),
                'far_L': self.far_L(left_dist)}

    def close_L(self, x):
        if 0 <= x <= 50:
            return (-1/50) * x + 1
        return 0

    def moderate_L(self, x):
        if 35 <= x <= 50:
            return (1/15) * x - (7/3)
        if 50 < x <= 65:
            return (-1/15) * x + (13/3)
        return 0

    def far_L(self, x):
        if 50 <= x <= 100:
            return (1/50) * x - 1
        return 0

    def membership_degree_right(self, right_dist):
        return {'close_R': self.close_R(right_dist),
                'moderate_R': self.moderate_R(right_dist),
                'far_R': self.far_R(right_dist)}

    def close_R(self,x):
        if 0 <= x <= 50:
            return (-1/50) * x + 1
        return 0

    def moderate_R(self, x):
        if 35 <= x <= 50:
            return (1/15) * x - (7/3)
        if 50 < x <= 65:
            return (-1/15) * x + (13/3)
        return 0

    def far_R(self, x):
        if 50 <= x <= 100:
            return (1/50) * x - 1
        return 0

    def inference(self, l_memship, r_memship):

        self.inference_results = {
            'low_right': min(l_memship['close_L'], r_memship['moderate_R']),
            'high_right': min(l_memship['close_L'], r_memship['far_R']),
            'low_left': min(l_memship['moderate_L'], r_memship['close_R']),
            'high_left': min(l_memship['far_L'], r_memship['close_R']),
            'nothing': min(l_memship['moderate_L'], r_memship['moderate_R'])
        }

    def max_rotate(self, x):
        return max(
            min(self.high_right(x), self.inference_results['high_right']),
            min(self.low_right(x), self.inference_results['low_right']),
            min(self.low_left(x), self.inference_results['low_left']),
            min(self.high_left(x), self.inference_results['high_left']),
            min(self.nothing(x), self.inference_results['nothing'])
        )

    def high_right(self, x):
        if -50 <= x <= -20:
            return (1/30) * x + (5/3)
        if -20 < x <= -5:
            return (-1/15) * x - (1/3)
        return 0

    def low_right(self, x):
        if -20 <= x <= -10:
            return (1/10) * x + 2
        if -10 < x <= 0:
            return (-1/10) * x
        return 0

    def nothing(self, x):
        if -10 <= x <= 0:
            return (1/10) * x + 1
        if 0 < x <= 10:
            return (-1/10) * x + 1
        return 0

    def low_left(self, x):
        if 0<= x <= 10:
            return (1/10) * x
        if 10 < x <= 20:
            return (-1/10) * x + 2
        return 0

    def high_left(self, x):
        if 5 <= x <= 20:
            return (1/15) * x - (1/3)
        if 20 < x <= 50:
            return (-1/30)* x + (5/3)
        return 0

    def centroid(self):
        numerator = 0.0
        denominator = 0.0

        step = 100 / 999
        x = [-50 + i * step for i in range(1000)]
        delta = x[1] - x[0]
        for i in x:
            u = self.max_rotate(i)
            numerator += u * i * delta
            denominator += u * delta

        center = 0.0
        if denominator != 0:
            center = 1.0 * float(numerator) / float(denominator)
        return center
