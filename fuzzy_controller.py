class FuzzyController:
    """
    #todo
    write all the fuzzify,inference,defuzzify method in this class
    """

    def __init__(self):
        pass


    def decide(self, left_dist,right_dist):
        """
        main method for doin all the phases and returning the final answer for rotation
        """
        return 0

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
